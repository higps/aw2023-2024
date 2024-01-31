1. Definer kort «Cloud Computing» (skyprosessering) med dine egne ord.
Cloud computing er i hovedsak noen andre sin datamaskin. Ofte da selskaper som har en datapark med mye datakraft som du kan leie og dette er som oftest tilgjengelig fra nettet.

2. Hva mener vi med «Platform-as-a-Service»? Kan du gi et eksempel på en «PaaS»?
Platform som en service er en tjeneste du leier der du får diverse tilganger og funksjonalitet. Azure og AWS er platformer som har en rekke forskjellige tjenester som kan utføre forskjellige ting, som feks kode eksekvering og databaser

3. Hva er de fire hoved-grupperingene skytjenester? Kan du nevne ett par eksempler for hver tjeneste? (enten generelt eller i Azure)
Husker ikke helt navnene men i hovedsak har du følgende:

Machine as a service: Der du leier en hel fysisk maskin, ingen andre deler noe med deg. Du har tilgang til platformen som kjører og kan sette opp ting selv.

Virtual machine as a service: Du leier en virituell maskin, der andre deler hardwaren med deg. Maskinen og dine data er isolert, men CPU og nettverk er delt av andre som også bruker virituelle maskiner på samme fysiske maskin. Her kan du velge mer selv hva som skal kjøres at tjenester som man setter opp selv. Du får allokert datakraft på samme maskinvare

Platform as a service: Du får tilgang til en platform, som feks Azure som har en rekke ting man kan gjøre som å ha databaser eller compilere som kjører forskjellige scripts og kodei skyen, men du har lite å gjøre med oppsettet av nettverk og softwaren som gjør at platformen kan kjøre selv, siden dette er fastsatt fra før av. Andre har også kontoer og data "ved siden av" din data, men separat og sikret.

Software as a serivce: Der du leier kun applikasjonen som du bruker og operativ system og nettverk som trengs er allerede satt opp for deg. Lite fleksibelt om man ønsker å gjøre andre ting enn det softwaren er låst til å gjøre.

4. Hva mener vi når vi sier en tjeneste er «elastisk»?
Det betyr at du kan skalere etter hva du bruker. Som feks at du har flere servere kjørende med applikasjoner som noen ganger trenger mer båndbredde eller CPU kraft pga en periode med høyere volum

5. Hva er availability zones og regions i Azure?
Det er forskjellige fysiske steder hvor dataen din blir lagret. Dette gjelder ofte lovgitte data som krever at dataen ikke forlater landet.

6. Hva mener vi med at en tjeneste er «serverless»? Kan du gi eksempel på en «serverless» tjeneste i Azure?
Container-apps er serverless, som betyr at selve tjenesten er ikke knyttet til en spesifikk server, men kan kjøre hvor som helst i clouden.

7. Du skal opprette en SQL Database og en Azure Container App i Azure Portalen. Hvordan velger du å gruppere tjenestene? Forklar.
Jeg ville gruppert tjenestene etter behovet for databasen og container appen. Hvis ikke databasen og container appen er direkte relatert så ville jeg hatt de hver for seg.

8. Du skal deploye en container i Azure. Hvordan går du frem? Er det for øvrig noen alternative tjenester du kunne brukt?
Først ville jeg lest dokumentasjonen på hva som støttes i Azure av containere og brukt noe som støttes.
Deretter ville jeg brukt noe lokalt for å teste at containerene før jeg laster de opp i Azure.
Hvis jeg skal deploye i Azure så finnes det vel tjenester som har enkle pipelines for å lage containere til Azure, som docker desktop hvor man kan deploye rett i Azure så lenge man får logget inn.

9. Hva er forskjellen på en Virtuell Maskin (VM) og en Container?
En virituell maskin har ofte mye mer enn man trenger, det kan være store operativ systemer med alle programmene som følger med.
En container er det minste mininum som kan kjøre, og bør ikke inneholde mer enn det den trenger. Så lenge en container er laget rett så skal den kunne kjøre alle steder som støtter containere

10. Dockerfil, image, container, registry og repository nevnes ofte når man jobber med Docker. Hva er sammenhengen mellom disse? Forklar.
Dockerfil: Filen som brukes for å definere oppskriften på et image, denne er avhengig av filtilganger til den som kjører docker filen så den er ikke lik for alle siden noen kan feks mangle filer eller tilganger som den originale brukeren har
Image: Filen som blir laget av oppskriften, denne er lik slik at folk med samme image vil få samme fil
Container: Det er et minimalt operativ system med det minste minimum som trengs og fungerer selvstendig. Dette betyr at man trenger ikke installere tillegspakker og slikt for å kjøre containeren ettersom denne skal inneholde dette fra før av.
Registry: Dette er registeret over hvilke containere man har
Repository: Dette er et sted som det kan lagres containere og registere på som gjør at dette lett oppdateres og kan deles med andre

11. Hvorfor er Docker ansett som svært praktisk av utviklere?
Det minimerer knoting med tillegspakker og andre avhengigheter som trengs for å kjøre applikasjonen som ligger i containere. Så lenge man har laget et godt docker image skal dette kunne kjøre og eksekvere helt likt uansett hvor det er satt opp.

12. Hvorfor bruker vi pySpark fremfor «vanlig python»?
I databricks så er pySpark tilpasset notebook formatet i cloud og gjør det lettere å bruke SQL spørringer og python kode om hverandre uten å måtte trenge ulike python tilegg og standarder, ettersom det finnes en rekke bilbiotek som kan kjøre forskjellige ting i python som sql spørringer og maskin læring

13. Hva gjør en magic command i Databricks? Har du et eksempel?
En magic command spesiferer hva slags kode som skal kjøres.
Eksempel: Man ha noe kode som gjør noe i python først, så trenger det noe fra SQL, istedet for å ha en tekst streng i python for å gjøre SQL spørringene, kan man endre programeringsspråket til SQL gjøre SQL spørringen, for å så bruke denne samme spørringen som en dataframe i neste kodeblokk som kjører python igjen.

14. Hva trenger du for å kunne «kjøre» kode i Databricks?
Du trenger at syntaksen er korrekt og datakraft for å eksekvere koden, samt tilgang til platformen for å få gjort noe som helst.
