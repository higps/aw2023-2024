import random

#damage values
health = 100
dmg_lowest = 20
dmg_highest = 30
number_of_attacks = 2

print("You are an healthy adventurer with", health, "health")
# For loop where we add the damage to total_damage for each number of attack
# As we want the random number to be different for repeated attacks
total_damage = 0
for _ in range(number_of_attacks):
    
    damage = random.randint(dmg_lowest, dmg_highest)
    print("You got attacked and took", damage ,"damage")
    total_damage += damage

#Heal values
heal_base = 10
heal_min = 10
heal_max = 15
heal = heal_base + random.randint(heal_min, heal_max)

print("You drank a health potion and healed for", heal, "health points")

#COMBAT
health = health - total_damage + heal

print("After this adventure your health is", health)



