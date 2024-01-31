/**
 * Sourcemod 1.7 Plugin Template
 */
#pragma semicolon 1
#include <sourcemod>

#include <sdkhooks>
#include <tf2_stocks>
#include <tf_custom_attributes>
#include <dhooks>

#pragma newdecls required

#include <stocksoup/var_strings>
#include <stocksoup/tf/client>
#include <stocksoup/tf/econ>
#include <stocksoup/tf/entity_prop_stocks>
#include <stocksoup/tf/tempents_stocks>

#include <tf2utils>

#define PLUGIN_VERSION "0.0.0"
public Plugin myinfo = {
	name = "[TF2CA] Medigun Uber: Group Overheal",
	author = "Author!",
	description = "Description!",
	version = PLUGIN_VERSION,
	url = "localhost"
}

#define DISPENSER_RANGE 64.0

Handle g_DHookUpdateOnRemove;

Handle g_SDKCallFindEntityInSphere, g_SDKCallPlayerSharedStartHealing,
		g_SDKCallPlayerSharedStopHealing;
ArrayList g_RadiusHealRecipients[MAXPLAYERS + 1];

float g_flLastHealthParticleDisplayTime[MAXPLAYERS + 1];

enum struct GroupOverhealAttributes {
	float flHealRate;
	float flOverhealRatio;
	float flOverhealTimeScale;
	bool bFixedHealRate;
	float flHealRange;
}

public void OnPluginStart() {
	Handle hGameConf = LoadGameConfigFile("tf2.cattr_starterpack");
	if (!hGameConf) {
		SetFailState("Failed to load gamedata (tf2.cattr_starterpack).");
	}
	
	StartPrepSDKCall(SDKCall_EntityList);
	PrepSDKCall_SetFromConf(hGameConf, SDKConf_Signature,
			"CGlobalEntityList::FindEntityInSphere()");
	PrepSDKCall_SetReturnInfo(SDKType_CBaseEntity, SDKPass_Pointer);
	PrepSDKCall_AddParameter(SDKType_CBaseEntity, SDKPass_Pointer,
			VDECODE_FLAG_ALLOWNULL | VDECODE_FLAG_ALLOWWORLD);
	PrepSDKCall_AddParameter(SDKType_Vector, SDKPass_ByRef);
	PrepSDKCall_AddParameter(SDKType_Float, SDKPass_Plain);
	PrepSDKCall_AddParameter(SDKType_PlainOldData, SDKPass_Plain);
	g_SDKCallFindEntityInSphere = EndPrepSDKCall();
	
	StartPrepSDKCall(SDKCall_Raw);
	PrepSDKCall_SetFromConf(hGameConf, SDKConf_Signature, "CTFPlayerShared::Heal()");
	PrepSDKCall_AddParameter(SDKType_CBaseEntity, SDKPass_Pointer); // inflictor entity
	PrepSDKCall_AddParameter(SDKType_Float, SDKPass_Plain); // float ??
	PrepSDKCall_AddParameter(SDKType_Float, SDKPass_Plain); // float ??
	PrepSDKCall_AddParameter(SDKType_Float, SDKPass_Plain); // float ??
	PrepSDKCall_AddParameter(SDKType_Bool, SDKPass_Plain); // bool dispenser ??
	PrepSDKCall_AddParameter(SDKType_CBasePlayer, SDKPass_Pointer); // healing player
	g_SDKCallPlayerSharedStartHealing = EndPrepSDKCall();
	
	StartPrepSDKCall(SDKCall_Raw);
	PrepSDKCall_SetFromConf(hGameConf, SDKConf_Signature, "CTFPlayerShared::StopHealing()");
	PrepSDKCall_AddParameter(SDKType_CBaseEntity, SDKPass_Pointer);
	g_SDKCallPlayerSharedStopHealing = EndPrepSDKCall();
	
	g_DHookUpdateOnRemove = DHookCreateFromConf(hGameConf, "CBaseEntity::UpdateOnRemove()");
	if (!g_DHookUpdateOnRemove) {
		SetFailState("Failed to create detour %s", "CBaseEntity::UpdateOnRemove()");
	}
	
	Handle dtGetChargeType = DHookCreateFromConf(hGameConf,
			"CTFPlayer::GetChargeEffectBeingProvided()");
	DHookEnableDetour(dtGetChargeType, false, OnGetPlayerProvidedCharge);
	
	delete hGameConf;
}

public void OnMapStart() {
	for (int i; i < MAXPLAYERS + 1; i++) {
		delete g_RadiusHealRecipients[i];
	}
	
	for (int i = 1; i <= MaxClients; i++) {
		if (IsClientInGame(i)) {
			OnClientPutInServer(i);
		}
		g_RadiusHealRecipients[i] = new ArrayList();
	}
	
	int entity = -1;
	while ((entity = FindEntityByClassname(entity, "*")) != -1) {
		if (TF2Util_IsEntityWeapon(entity) && TF2Util_GetWeaponID(entity) == 50) {
			DHookEntity(g_DHookUpdateOnRemove, false, entity, .callback = OnMedigunRemoved);
		}
	}
}

public void OnClientPutInServer(int client) {
	g_flLastHealthParticleDisplayTime[client] = 0.0;
}

public void OnEntityCreated(int entity, const char[] classname) {
	if (TF2Util_IsEntityWeapon(entity) && TF2Util_GetWeaponID(entity) == 50) {
		DHookEntity(g_DHookUpdateOnRemove, false, entity, .callback = OnMedigunRemoved);
	}
}

MRESReturn OnMedigunRemoved(int medigun) {
	// avoid issue where medigun is killed on class change and we can't detach healing
	// why doesn't CTFPlayerShared::Heal() perform entity validation??  thought it did
	int owner = TF2_GetEntityOwner(medigun);
	if (1 <= owner <= MaxClients) {
		DetachGroupOverheal(medigun);
	}
}

public void OnGameFrame() {
	for (int i = 1; i <= MaxClients; i++) {
		if (!IsClientInGame(i)) {
			continue;
		}
		OnPlayerPostThinkPost(i);
	}
}

void OnPlayerPostThinkPost(int client) {
	int activeWeapon = GetEntPropEnt(client, Prop_Send, "m_hActiveWeapon");
	int secondary = GetPlayerWeaponSlot(client, TFWeaponSlot_Secondary);
	
	// TODO: can we just keep ubercharge state somewhere so we know if they need to be detached?
	
	// drop overheal from medigun if it's not active or ubercharge wore off
	if (!IsPlayerAlive(client) || secondary != activeWeapon
			|| !IsUberchargeDeployed(secondary)) {
		if (IsValidEntity(secondary) && TF2Util_IsEntityWeapon(secondary)
				&& TF2Util_GetWeaponID(secondary) == TF_WEAPON_MEDIGUN) {
			DetachGroupOverheal(secondary);
		}
		return;
	}
	
	GroupOverhealAttributes healprops;
	
	// not the correct medigun
	if (TF2Util_GetWeaponID(secondary) != TF_WEAPON_MEDIGUN
			|| !IsGroupOverhealMedigun(activeWeapon, healprops)) {
		return;
	}
	
	float vecOrigin[3];
	GetClientAbsOrigin(client, vecOrigin);
	
	TFTeam team = TF2_GetClientTeam(client);
	
	// radius check to see which friendly players are in range
	bool bInGroupOverhealRange[MAXPLAYERS + 1];
	int target = -1;
	while ((target = FindEntityInSphere(target, vecOrigin, healprops.flHealRange)) != -1) {
		if (target > 0 && target <= MaxClients
				&& TF2_GetClientTeamFromClient(target, client) == team) {
			bInGroupOverhealRange[target] = true;
		}
	}
	
	for (int i = 1; i <= MaxClients; i++) {
		if (!IsClientInGame(i)) {
			continue;
		}
		
		int iHealRecipientIndex =
				g_RadiusHealRecipients[client].FindValue(GetClientSerial(i));
		bool bIsKnownHealRecipient = iHealRecipientIndex != -1;
		
		if (bInGroupOverhealRange[i] && g_flLastHealthParticleDisplayTime[i] < GetGameTime()) {
			float vecParticleOrigin[3];
			GetClientEyePosition(i, vecParticleOrigin);
			vecParticleOrigin[2] += 32.0;
			
			TE_SetupTFParticleEffect(TF2_GetClientTeamFromClient(i, client) == TFTeam_Red?
					"healthgained_red_giant" : "healthgained_blu_giant", vecParticleOrigin,
					.entity = i, .attachType = PATTACH_CUSTOMORIGIN);
			TE_SendToAll();
			
			g_flLastHealthParticleDisplayTime[i] = GetGameTime() + 0.5;
		}
		
		// not a new state, don't add / remove healing
		if (bInGroupOverhealRange[i] == bIsKnownHealRecipient) {
			continue;
		}
		
		switch (bInGroupOverhealRange[i]) {
			case true: {
				// in range now, add healer
				g_RadiusHealRecipients[client].Push(GetClientSerial(i));
				StartHealing(i, activeWeapon, client, healprops.flHealRate,
						healprops.flOverhealRatio, healprops.flOverhealTimeScale,
						healprops.bFixedHealRate);
				
				TF2_SetClientUberchargeOverlay(i);
				
				if (i == client) {
					EmitGameSoundToAll("Halloween.spell_overheal", .entity = i);
				}
			}
			case false: {
				// not in range anymore, remove healer
				g_RadiusHealRecipients[client].Erase(iHealRecipientIndex);
				StopHealing(i, activeWeapon);
				SetClientScreenOverlay(i, "");
			}
		}
	}
}

MRESReturn OnGetPlayerProvidedCharge(int client, Handle hReturn) {
	if (!IsClientInGame(client)) {
		return MRES_Ignored;
	}
	
	int activeWeapon = GetEntPropEnt(client, Prop_Send, "m_hActiveWeapon");
	GroupOverhealAttributes healprops;
	if (IsUberchargeDeployed(activeWeapon) && IsGroupOverhealMedigun(activeWeapon, healprops)) {
		DHookSetReturn(hReturn, -1);
		return MRES_Supercede;
	}
	return MRES_Ignored;
}

void DetachGroupOverheal(int medigun) {
	int client = TF2_GetEntityOwner(medigun);
	// stop healing all players in g_RadiusHealRecipients[client] if there are any
	while (g_RadiusHealRecipients[client].Length) {
		int target = GetClientFromSerial(g_RadiusHealRecipients[client].Get(0));
		if (target) {
			StopHealing(target, medigun);
			SetClientScreenOverlay(target, "");
		}
		g_RadiusHealRecipients[client].Erase(0);
	}
	return;
}

bool IsUberchargeDeployed(int weapon) {
	if (!IsValidEntity(weapon) || !TF2Util_IsEntityWeapon(weapon)
			|| TF2Util_GetWeaponID(weapon) != TF_WEAPON_MEDIGUN) {
		return false;
	}
	
	return GetEntProp(weapon, Prop_Send, "m_bChargeRelease") != 0;
}

bool IsGroupOverhealMedigun(int weapon, GroupOverhealAttributes healprops) {
	char attr[256];
	
	if (!TF2CustAttr_GetString(weapon, "medigun charge is group overheal",
			attr, sizeof(attr))) {
		return false;
	}
	
	healprops.flHealRange = ReadFloatVar(attr, "range", DISPENSER_RANGE * 5.0);
	healprops.flHealRate = ReadFloatVar(attr, "heal_rate", 30.0);
	healprops.flOverhealRatio = ReadFloatVar(attr, "overheal_ratio", 1.5);
	healprops.flOverhealTimeScale = ReadFloatVar(attr, "overheal_duration_mult", 2.0);
	healprops.bFixedHealRate = !!ReadIntVar(attr, "fixed_heal_rate", true);
	
	return true;
}

int FindEntityInSphere(int startEntity, const float vecPosition[3], float flRadius) {
	return SDKCall(g_SDKCallFindEntityInSphere, startEntity, vecPosition, flRadius, Address_Null);
}

/**
 * 
 * @param target				The client that is receiving healing.
 * @param inflictor				The entity providing the healing (e.g., Dispenser, Medigun).
 * 								If this entity is removed, the healing stops.
 * @param healer				The client that is providing healing.
 * @param flHealRate			Base amount of healing per second.
 * @param flOverhealRatio		Determines the multiplier of maximum health that this heal is
 * 								allowed to heal to.
 * @param flOverhealTimeMult	Rate at which overhealed health decays, as a time scalar (i.e.,
 * 								larger numbers mean longer overheal time and slower decay).
 * @param bFixedHealRate		Determines if the heal rate is boosted if the player wasn't in
 * 								combat recently.
 */
void StartHealing(int target, int inflictor, int healer, float flHealRate,
		float flOverhealRatio, float flOverhealDecayRate, bool bFixedHealRate) {
	SDKCall(g_SDKCallPlayerSharedStartHealing, GetPlayerSharedPointer(target), inflictor,
			flHealRate, flOverhealRatio, flOverhealDecayRate, bFixedHealRate, healer);
}

void StopHealing(int target, int inflictor) {
	SDKCall(g_SDKCallPlayerSharedStopHealing, GetPlayerSharedPointer(target), inflictor);
}

Address GetPlayerSharedPointer(int client) {
	if (!IsClientInGame(client)) {
		ThrowError("Invalid client entity");
	}
	int sharedoffs = FindSendPropInfo("CTFPlayer", "m_Shared");
	return GetEntityAddress(client) + view_as<Address>(sharedoffs);
}