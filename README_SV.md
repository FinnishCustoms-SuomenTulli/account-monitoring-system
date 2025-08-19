
# Centraliserat informationssystem för saldo och kontotransaktioner

*Dokumentversion 0.2*

Detta dokument är en del av dokumentationen av övervakningssystemet för bank- och betalkonton och instruerar uppgiftslämnare och användare av information i förmedling av uppgifter om saldo och kontotransaktioner i övervakningssystemet för bank- och betalkonton. Detta dokument beskriver kraven för implementering av systemet, flödet av information om saldo och kontotransaktioner i systemet samt fråge- och svarsmeddelanden om saldo och kontotransaktioner.

Övervakningssystemet för bank- och betalkonton förmedlar information om medborgares, företags och enheters bank- och betalkonton till användare av informationen, dvs. till lagstadgade myndigheter. Systemet grundas på lagen om ett övervakningssystem för bank- och betalkonton. Lagändringen om centralisering av förfrågningar om saldo och kontotransaktioner samt om värdepapper till övervakningssystemet för bank- och betalkonton träder i kraft i december 2025.

Uppgiftslämnare, dvs. kreditinstitut, betalningsinstitut, institut för elektroniska pengar och leverantörer av kryptotillgångstjänster, överlåter sina kunders bank- och betalkontouppgifter antingen via bank- och betalkontoregistret eller genom sitt eget datasöksystem. Tullen upprätthåller ett sammanställningsprogram som förmedlar myndigheters begäranden om uppgifter till bank- och betalkontoregistret samt överför de mottagna uppgifterna till myndigheten. Förfrågningar om saldo och kontotransaktioner skickas antingen till uppgiftslämnarens datasöksystem eller via skyddad e-post till kontoregistrets operatörer. Förfrågningar besvaras antingen genom ett system för utlämnande av uppgifter eller genom ett eget datasöksystem.

### Innehållsförteckning

[1. Kontaktuppgifter](#luku1)  
[2. Ordlista & förkortningar](#luku2)  
[3. Certifikat](#luku3)  
[4. Informationsflöde i förfrågan om saldo och kontotransaktioner](#luku4)  
[5. Business Application Header](#luku5)  
[6. Frågemeddelande](#luku6)  
[7. Svarsmeddelandea](#luku7)  
[8. Felsituationer](#luku8)  

## 1. Kontaktuppgifter <a name="luku1"></a>

E-post: [tilirekisteri@tulli.fi](mailto:tilirekisteri@tulli.fi).

## 2. Ordlista & förkortningar <a name="luku2"></a>

| Term    | Förklaring |
| -------- | ------- |
| Övervakningssystem för bank- och betalkonton | Det nationella övervakningssystemet för bank- och betalkonton, som består av ett kontoregister, datasöksystem och från och med 1.11.2022 ett sammanställningsprogram, grundas på lagen om ett övervakningssystem för bank- och betalkonton 571/2019 och på Europaparlamentets och rådets direktiv (EU) 2018/843 av den 30 maj 2018 om förhindrande av användning av det finansiella systemet för penningtvätt eller finansiering av terrorism.|
| Centraliserat informationssystem för saldo och kontotransaktioner | Förfarande för hantering av uppgifter om saldo och kontotransaktioner från övervakningssystemet för bank- och betalkonton samt uppgifter om värdepapper, vilket baseras på elektronisk informationshantering. |
| Bank- och betalkontoregister/Kontoregister| Bank- och betalkontoregistret (kontoregistret) är ett system som byggts upp av Tullen, som består av applikationen Kontoregister och dess uppdaterings- och frågegränssnitt. Kontoregistret samlar in uppgifter om kunder som har bank- och betalkonton hos betalningsinstitut och institut för elektroniska pengar samt hos kreditinstitut som beviljats dispens av Finansinspektionen, samt kunduppgifter från leverantörer av kryptotillgångstjänster.  |
| Sammanställningsprogram | En automatiserad teknisk lösning som upprätthålls av Tullen, med vilken man förmedlar uppgifter om bank- och betalkonton, bankfack, saldo och kontotransaktioner samt om värdepapper via övervakningssystemet för bank- och betalkonton.    |
| Datasöksystem | Datasöksystem avser ett elektroniskt datasöksystem för bank- och betalkonton som administreras av uppgiftslämnaren, och med vilken uppgiftslämnaren direkt och utan hinder av sekretessbestämmelserna förmedlar information om sina kunder, som avses i lagen om ett övervakningssystem för bank- och betalkonton 4 § 2 mom. till behörig myndighet. Enligt lagen bestämmer Tullen de tekniska kraven på datasöksystemet och varje uppgiftslämnare realiserar sitt eget datasöksystem, så det finns alltså många datasöksystem.  |
| Användare av information | Lagen om ett övervakningssystem för bank- och betalkonton fastställer behörig myndighet samt advokatförening, vilka har rätt att begära information från övervakningssystemet för bank- och betalkonton. Behörighet definieras i gällande lagstiftning.  |
| Uppgiftslämnare | Uppgiftslämnare avser betalningsinstitut, institut för elektroniska pengar, kreditinstitut eller leverantör av kryptotillgångstjänster som tillhandahåller uppgifter som definieras i lagen om övervakningssystemet för bank- och betalkonton via kontoregistrets uppdateringsgränssnitt som upprätthålls av Tullen eller förmedlar motsvarande uppgifter via datasöksystemet som den upprätthåller. Uppgiftslämnare avser också filialkontor i Finland som innehas av ett utländskt betalningsinstitut, institut för elektroniska pengar, kreditinstitut och tillhandahållare av virtuella valutor. |
| System för utlämnande av uppgifter | System till vilket uppgiftslämnare som uppdaterar kontoregistret skickar svarsmeddelande på förfrågan om saldo och kontotransaktioner.  |
| Saldo |  Belopp på bank- och betalkonto vid tidpunkten när förfrågan besvaras, där man har dragit av eventuell täckningsreservering.  |
| Uppgifter om kontotransaktioner | Detaljerad information om transaktioner som utförts under en viss tidsperiod via ett specifikt betalkonto eller bankkonto som identifieras med ett IBAN-kontonummer eller detaljerad information om överföringar av kryptotillgångar (se lagen om övervakningssystemet för bank- och betalkonton 2 § mom. 15). |
| Begäran om ytterligare information | Uppgiftslämnaren begär ytterligare information av myndigheten som lämnade förfrågan före utlämnandet av uppgifter.  |
| (Ytterligare) information som begärs separat | Uppgifter som uppgiftslämnaren inte returnerar i svarsmeddelandet om myndigheten inte specifikt begär det i sitt frågemeddelande.  |


## 3. Certifikat <a name="luku3"></a>

I övervakningssystemet för bank- och betalkonton skyddas externa anslutningar med certifikat. Uppgiftslämnaren ska meddela Tullen vilka certifikat som används. Certifikaten ska följa Tullens anvisningar. Uppgiftslämnaren ska skaffa server- och systemsigneringscertifikat som uppfyller certifikatkraven och installera dem i sina system. Dessutom krävs ett signeringscertifikat för signering av meddelanden. Tekniskt kan samma certifikat fungera som både server- och systemsigneringscertifikat, eller certifikaten kan vara separata. Vanligen installeras servercertifikatet på frontservern som hanterar datatrafikanslutningar och signeringscertifikatet på backservern som skapar svaren.

<details>
<summary>Datasöksystemets certifikat</summary>
<br>

| Standard    | Certifikatets namn |  Avsedd användning  |    
| -------- | ------- | ------- |  
| X.509 (versio 3) | Datasöksystemets datatrafikcertifikat |  Autentisera användaren av gränssnittet och uppgiftslämnaren eller instans som uppgiftslämnaren auktoriserat  |  
| X.509 (versio 3) | 	Datasöksystemets signeringscertifikat  | Signera meddelande, säkerställa att meddelandet förblir oförändrat, autentisera uppgiftslämnaren  |  

Användare av datasöksystemets frågegränssnitt samt uppgiftslämnare  eller instanser som uppgiftslämnaren auktoriserat identifieras med X.509-certifikat (Datatrafikcertifikat). Fråge- och svarsmeddelanden i frågegränssnittet signeras med en XML-signatur (Signeringscertifikat).
</details>

### 3.1 Uppgiftslämnarens signeringscertifikat <a name="3-1"></a>

Uppgiftslämnaren måste signera sina avsända meddelanden med x.509-servercertifikat som anger FO-nummer eller momsnummer för uppgiftslämnaren i fråga. De som implementerar datasöksystem måste också kontrollera signaturen i inkommande meddelanden. Mottagaren får inte godkänna meddelandet utan en godtagbar signatur. Godkänd signatur förutsätter att XML-signaturen är valid (när det gäller datasöksystem) och att certifikatet antingen:
a) utfärdats av Myndigheten för digitalisering och befolkningsdata (MDB) och inte förekommer på spärrlistan som administreras av MDB och att serialNumber-attribut för certifikatets objekt är ifrågavarande uppgiftslämnares FO-nummer eller momsnummer
eller
b) är ett giltigt eIDAS-godkänt autentiseringscertifikat på webbplatser och inte förekommer på en uppdaterad spärrlista som administreras av certifikatleverantören och att organizationIdentifier-attribut för certifikatets objekt är ifrågavarande uppgiftslämnares FO-nummer eller momsnummer.

OBS! För att signaturerna av meddelandena ska uppfylla Cybersäkerhetscentrets krav på informationssäkerhet, ska certifikatets offentliga nyckel (RSA public key) som används för signaturerna vara minst 3 072 bitar. Syftet med certifikat som används för signaturer ska även omfatta "digital signatur". Dessa faktorer ska beaktas vid beställning av certifikat.

<details>
<summary>Signeringscertifikat från behörig myndighet</summary>
<br> 

Den behöriga myndigheten måste signera meddelanden som skickas med x.509-servercertifikat där FO-nummer för myndigheten i fråga framgår. Signaturen på inkommande meddelanden måste kontrolleras. Mottagaren får inte godkänna ett meddelande utan en godtagbar signatur. Godkännande av behörig myndighets signering kräver att XML-signaturen är valid och att
a) certifikatet utfärdats av MDB, giltigt och inte förekommer på spärrlistan som administreras av MDB
b) serialNumber-attributet för certifikatobjektet är FO-nummer eller kod för den behöriga myndigheten som skickar meddelandet, och utgörs av bokstäverna "FI" och FO-numrets numeriska del utan bindestreck (kod i momsnummerformat).

</details>

<details>
<summary> Kontakttagarens datatrafikcertifikat i datasöksystemet </summary>
<br> 

Uppgiftslämnaren eller den instans som uppgiftslämnaren har auktoriserat autentiserar med hjälp av servercertifikatet den behöriga myndighet som tar kontakt med datasöksystemets gränssnitt. Anslutning från behörig myndighet måste godkännas på följande villkor:
a) Den behöriga myndighetens certifikat har utfärdats av MDB
b) certifikatet är giltigt och förekommer inte på MDB:s spärrlista
c) serialNumber-attributet för certifikatets objekt är FO-nummer eller kod som bildas av bokstäverna ”FI” och FO-numrets numeriska del utan bindestreck (kod i momsnummerformat) för den behöriga myndigheten eller det statliga servicecentret som agerar för dess räkning.

OBS! För att skyddet av datatrafiken ska uppfylla Cybersäkerhetscentrets krav på informationssäkerhet som hänvisas till nedan ska certifikatets offentliga nyckel (RSA public key) vara minst 3 072 bitar. Dessutom ska certifikatet vara ett servercertifikat av typ QWAC (Quality Website Authentication Certificate) som innehåller expansioner (X509v3 Extended Key Usage: TLS Web Client Authentication, TLS Web Server Authentication). Dessa ska beaktas vid beställning av certifikat.

</details>

### 3.2 Datatrafikcertifikat för uppgiftslämnaren eller instans som uppgiftslämnaren auktoriserat <a name="3-2"></a>

Datatrafiken måste skyddas (kryptering och identifiering av motpart) med certifikat x.509 (version 3). När det gäller ett datasöksystem autentiseras uppgiftslämnaren eller instans som uppgiftslämnaren auktoriserat av den behöriga myndigheten som tar kontakt med frågegränssnittet med hjälp av servercertifikat.

För att upprätta anslutningen måste ett servercertifikat användas som anger FO-nummer eller momsnummer för uppgiftslämnaren i fråga eller instans som uppgiftslämnaren auktoriserat. Instans som uppgiftslämnaren auktoriserat avser till exempel ett servicecenter som uppgiftslämnaren har auktoriserat att för dess räkning ta hand om att skapa och/eller skicka meddelanden. Auktorisering som gäller detta ska skickas skriftligen till Tullen.

Godkännande av signatur kräver antingen att:
a) servercertifikatet utfärdats av MDB, certifikatet är giltigt och inte förekommer på MDB:s spärrlista, serialNumber-attributet för certifikatets objekt är FO-nummer eller momsnummer för uppgiftslämnaren i fråga eller instans som uppgiftslämnaren auktoriserat
eller
b) servercertifikatet är ett giltigt och eIDAS-godkänt autentiseringscertifikat för webbplatser och inte förekommer på en uppdaterad spärrlista som upprätthålls av certifikatleverantören och organizationIdentifier-attribut för certifikatets objekt är FO-nummer eller momsnummer för uppgiftslämnaren i fråga eller instans som uppgiftslämnaren auktoriserat. Om samma FO-nummer eller momsnummer används på uppgiftslämnarens servercertifikat och på signaturcertifikatet på det utgående meddelandet kan samma certifikat användas för båda ändamålen.

OBS! För att skyddet av datatrafiken ska uppfylla Cybersäkerhetscentrets krav på informationssäkerhet som hänvisas till nedan, ska certifikatets offentliga nyckel (RSA public key) vara minst 3 072 bitar. Dessutom ska certifikatet vara ett servercertifikat av typ QWAC (Quality Website Authentication Certificate) som innehåller expansioner (X509v3 Extended Key Usage: TLS Web Client Authentication, TLS Web Server Authentication). Dessa bör beaktas vid beställning av certifikat.

<details>
<summary>Skapa en XML-signatur för datasöksystem <a name="xml-allekirjoitus"></a></summary>
<br>

Signaturtypen är enveloped signature. Signature-elementet placeras under Sgntr-elementet i [BAH](#luku5).

Exempel SignedInfo
![esimerkki SignedInfon käytöstä](diagrams/image.png) 

Signaturalgoritmen är RSA-SHA256 eller RSA-SHA512 och C14N är Exclusive XML Canonicalization. Reference URI är antingen ”#applicationRequest” eller ”#applicationResponse”, beroende på om det är ett fråge- eller ett svarsmeddelande. Alltså signeras endast elementet "ApplicationRequest" eller "ApplicationResponse". När signering skapas ska Algoritmen SHA256 eller SHA512 användas för att skapa beräknade sammandrag (Digest). OBS! När det gäller ett svarsmeddelande ska det innehålla det anknytande frågemeddelandet BusinessApplicationHeader (Rltd element) som även ska vara signerad.

De kryptografiska algoritmerna som används i signaturen måste minst uppfylla de krav på kryptografisk styrka som anges av Kommunikationsverket för den nationella skyddsnivån TL IV. Gällande krav på styrka beskrivs i dokumentet https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/regulation/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf (på finska) (Dnr: 190/651/2015).

</details>

### 3.3 Skydd av anslutningar <a name="3-3"></a>

Anslutningar mellan kontoregistrets uppdateringsgränssnitt och datasöksystemets frågegränssnitt måste skyddas med TLS-kryptering med TLS-protokollversion 1.2 eller senare. Båda ändarna av anslutningen autentiseras med de servercertifikat som beskrivs ovan genom en tvåvägs handskakning. Anslutningen måste upprättas med nyckelutbytet ephemeral Diffie-Hellman (DHE), där en ny unik privat krypteringsnyckel skapas för varje session. Syftet med detta förfarande är att säkerställa funktionen forward secrecy för krypteringen, så att ett avslöjande av krypteringsnyckeln i efterhand inte skulle leda till avslöjande av krypterad information. Kryptografiska algoritmer som används för TLS-kryptering måste uppfylla minst de krav på kryptografisk styrka som Traficom definierar för nationell skyddsnivå TL IV. Aktuella styrkekrav beskrivs i dokumentet https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/regulation/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf (på finska) (Dnr: 190/651/2015).

### 3.4 Tillåten HTTP-version <a name="3-4"></a>

Anslutningarna mellan kontoregistrets gränssnitt för uppdatering och datasöksystemets frågegränssnitt använder HTTP-protokollversion 1.1.

### 3.5 Skaffa certifikat <a name="3-5"></a>

Certifikaten söks av den instans som genererar och förmedlar svaren på förfrågningar från användare av information. Om man använder en tjänsteleverantör som skapar och förmedlar meddelanden för den anmälningsskyldiges räkning, söker tjänsteleverantören servercertifikat. Då måste den anmälningsskyldige auktorisera tjänsteleverantören att signera meddelanden som ska skickas. Om den privata nyckeln som är kopplad till certifikatet avslöjas eller misstänks ha hamnat i fel händer, ska certifikatinnehavaren se till att certifikatet stängs omedelbart och detta rapporteras till Tullen utan dröjsmål. Om certifikatet utfärdas av misstag eller bedrägligt till fel instans ska certifikatets korrekta objekt säkerställa att certifikatet stängs och detta rapporteras till Tullen omedelbart efter att certifikatets korrekta objekt har fått kännedom om saken.

### 3.6 Uppdatering av certifikat <a name="3-6"></a>

Uppgiftslämnaren ska förnya certifikatet i god tid innan det går ut. Utgånget certifikat kan inte användas. Om annat inte avtalats ska det nya eller förnyade certifikatet levereras till Tullen elektroniskt med hjälp av en obestridd och datasäker dataöverföringsmetod senast en månad före dess införande. Certifikatet ska skickas via Tullens säkra e-posttjänst (https://turvaviesti.tulli.fi/) till adressen tilirekisteri@tulli.fi. Enligt lagen om ett övervakningssystem för bank- och betalkonton 8 § har Tullen rätt att få informationen kostnadsfritt och därför svarar uppgiftslämnaren för kostnaderna för certifikatet som denne använder.

### 3.7 Anmälningsskyldighet om  informationssäkerhetsincidenter <a name="3-7"></a>

Användaren av kontoregistrets gränssnitt är skyldig att utan dröjsmål anmäla om certifikat eller certifikatens hemliga nycklar som denne använder äventyras, både till den som utfärdat certifikatet och till Tullen. Användaren av gränssnittet är också skyldig att utan dröjsmål meddela Tullen om en informationssäkerhetsincident upptäcks i informationssystemet som använder gränssnittet. Om certifikaten för den som implementerar datasöksystemet eller certifikatens hemliga nycklar äventyras måste detta omedelbart rapporteras till den som utfärdat certifikatet och till de behöriga myndigheterna som använder datasöksystemet. Behöriga myndigheter måste också underrättas om en informationssäkerhetsincident upptäcks i datasöksystemet. Om certifikaten för den behöriga myndigheten som använder datasöksystemet eller certifikatens hemliga nycklar äventyras måste detta omedelbart meddelas till den som utfärdat certifikatet och till dem som implementerar datasöksystemet, vars implementering av datasöksystemet den behöriga myndigheten använder.

## 4. Informationsflöde i förfrågan om saldo och kontotransaktioner <a name="luku4"></a>

Bilden nedan visar en översikt över informationsflödet i förfrågan om saldo och kontotransaktioner i övervakningssystemet för bank- och betalkonton.

![Pankki- ja maksutilien valvontajärjestelmä](diagrams/tilitap_tiedonkulku_fi.png "Pankki- ja maksutilien valvontajärjestelmä")  

| Viranomaisten järjestelmät    | Myndigheternas system |
| -------- | ------- |
| 1.	Saldo- ja tilitapahtumatietokysely | Förfrågan om saldo och kontotransaktioner|
| 5.	Saldo- ja tilitapahtumatietokyselyn vastauksen haku | Sökning av svar på förfrågan om saldo och kontotransaktioner |
| Koostava sovellus | Sammanställningsprogram  |
| 4.	Vastaus: Saldo- ja tilitapahtumatiedot | Svar: Uppgifter om saldo och kontotransaktioner   |
| Tiedonluovutusjärjestelmä | System för utlämnande av information |
| 2.	Saldo- ja tilitapahtumatietokysely | Förfrågan om saldo och kontotransaktioner  |
| 3.	Vastaus: Saldo- ja tilitapahtumatiedot | Svar: Uppgifter om saldo och kontotransaktioner   |
| 2.	Saldo- ja tilitapahtumatietokysely | 2. Förfrågan om saldo och kontotransaktioner  |
| 3.	Vastaus: Saldo- ja tilitapahtumatiedot | Svar: Uppgifter om saldo och kontotransaktioner   |
| Tiedonluovuttajien tiedonhakujärjestelmät | Uppgiftslämnarens datasöksystem |
| Tilirekisteriin päivittävät tiedonluovuttajat | Uppgiftslämnare som uppdaterar kontoregistret |

1. Myndighetens system skickar en förfrågan om saldo och kontotransaktioner till sammanställningsprogrammets [frågegränssnitt](https://github.com/FinnishCustoms-SuomenTulli/account-register-aggregating-application/blob/main/index_sv.md#4-2). Innehållet i frågemeddelandet beskrivs i kapitlet [Frågemeddelande](#luku6). 
2. Sammanställningsprogrammet förmedlar förfrågan om saldo och kontotransaktioner till den operatör som förfrågan riktas till, antingen via gränssnittet till datasöksystemet eller med säker e-post till kontoregistrets operatör.  
3. Uppgiftslämnaren svarar på förfrågan om saldo och kontotransaktioner senast nästa bankdag. Om förfrågan riktas till den operatör som implementerade datasöksystemet, skickar datasöksystemet ett svarsmeddelande till sammanställningsprogrammet via gränssnittet. Om förfrågan riktas till en operatör som använder kontoregistret, skickar denne svarsmeddelandet till systemet som utlämnar information.    
4. Svarsmeddelandet förmedlas från systemet som utlämnar information till sammanställningsprogrammet.
5. Myndigheten hämtar svaret på sin förfrågan om saldo och kontotransaktioner i sammanställningsprogrammets gränssnitt. I sökningen av svar används sammanställningsprogrammets  [status](https://github.com/FinnishCustoms-SuomenTulli/account-register-aggregating-application/blob/main/index_sv.md#4-3) ja [resultatgränssnitt](https://github.com/FinnishCustoms-SuomenTulli/account-register-aggregating-application/blob/main/index_sv.md#4-4).

### 4.1 Anvisningar för uppgiftslämnare <a name="4-1"></a>

Förfrågningar om saldo och kontotransaktioner måste besvaras utan dröjsmål, men senast under kontorstid nästa bankdag, alltså före kl. 16.15 (EET). Om förfrågan inte kommer under kontorstid, dvs. kl. 8.00–16.15, börjar tidsfristen räknas följande bankdag. Om myndigheten till exempel skickar förfrågan på fredag kl. 18.00 ska svaret skickas senast kl. 16.15 följande tisdag.

När förfrågan endast gäller saldo ska man sträva efter att skicka svar omedelbart. Svaret ska skickas senast vid slutet av nästa bankdag. Saldouppgiften som lämnas måste gälla uppgiftslämnarens saldo vid tidpunkten för svar. Svar som gäller saldouppgiften ska ha en tidsstämpel som preciserar tidpunkten för saldot. I saldoförfrågan begär man som standard kontonumret, summan pengar på kontot samt datum och klockslag för kontots saldo (Lag om ett övervakningssystem för bank- och betalkonton, 17 b §). Kontots saldo måste beakta eventuella täckningsreserveringar på kontot, vilka måste dras av från kontots saldouppgift. Vid avvikande omständigheter kan man även begära ytterligare information. Om saldoförfrågan innehåller en begäran om ytterligare information, ska den behandlas separat för att tillhandahålla all begärd information.

När det gäller en advokats kundmedelskonton lämnas inte uppgifter om saldo och kontotransaktioner. Kundmedelskonto avser finanskonton och konton för andra tillgångar som förvaltas av advokat eller dennes kontor, men som innehas av någon annan än advokaten eller dennes kontor. Uppgifter om saldo och kontotransaktioner avseende en advokats kundmedelskonton får inte lämnas ut via det centraliserade elektroniska systemet för transaktions- och saldouppgifter (Lag om ett övervakningssystem för bank- och betalkonton, § 17 b och § 17 d). För att utreda kundmedelskontots saldo och transaktionsuppgifter bör den behöriga myndigheten vara i kontakt med den advokat som fungerar som kontoinnehavare.

Förfrågningar om saldo och kontotransaktioner kan inte göras som internationella förfrågningar.

#### Aktörer som rapporterar till systemet för utlämnande av information

För uppgiftslämnare som uppdaterar kontoregistret skickas förfrågan om uppgifter om saldo och kontotransaktioner via säker e-post (se [exempel på e -post](assets/Example_email.png)). Meddelandet med begäran finns som bilaga till e-posten i XML-format. Om det uppstår fel i behandlingen av förfrågan om saldo och kontotransaktioner, uppgifterna inte kan hittas av någon anledning eller förfrågan går till begäran om ytterligare redogörelse, ska ett svar skickas till gränssnittet och informationen meddelas enligt gällande situation. Svar på förfrågan ska tillhandahållas som ett meddelande i XML-format till Tullens gränssnitt.

Om uppgifter om objektet för sökningen av någon anledning inte kan hittas, måste uppgiftslämnaren svara på förfrågan med statuskoden NFOU.

### 4.2 Begäran om ytterligare redogörelse <a name="4-2"></a>

Om uppgiftslämnaren anser att en mottagen förfrågan behöver utredas ytterligare kan uppgiftslämnaren återställa statuskod NRES i förfrågan (under behandling) och ta direkt kontakt med myndigheten som skickat förfrågan för ytterligare information. För begäran om ytterligare redogörelse skickar myndigheten alltid kontaktuppgifter (namn, telefonnummer, e-post) i frågemeddelandets header-element Fr/OrgId/CtctDtls.

Uppgiftslämnaren svarar på den ursprungliga förfrågan efter behandling av ytterligare redogörelse, om det är möjligt inom tidsramen. Om man inte hinner besvara förfrågan inom tidsfristen kan myndigheten vid behov göra en ny förfrågan som uppgiftslämnaren besvarar enligt överenskommelse. Om uppgiftslämnaren har besvarat förfrågan NRES försöker sammanställningsprogrammet hämta svaret på nytt från uppgiftslämnaren fram till tidsgränsens slut. När tidsgränsen för utlämnande av uppgifter löper ut stängs förfrågan.

Exempel på förmedling av kontaktuppgifter: [Exempel på meddelande](examples/general/example_passing_contact_details.xml)

## 5. Business Application Header <a name="luku5"></a>

ISO 20022 standardin mukainen BusinessApplicationHeaderV01 [head.001.001.01](https://github.com/FinnishCustoms-SuomenTulli/account-register-information-query/blob/master/schemas/head.001.001.01.xsd) sanoma liitetään sekä kysely- että vastaussanomaan. Kenttien käyttö on muutoin samanlaista kysely- ja vastaussanomassa, paitsi kyselysanomassa tulee lähettää yhteystiedot mahdollista lisäselvityspyyntöä varten.

Sanoman Fr-kentän lähettäjätiedoissa on viranomaisen lähettämässä sanomassa viranomaisen tiedot, tiedonluovuttajan lähettämässä sanomassa tiedonluovuttajan tiedot ja Tullin välittämissä sanomissa Tullin tiedot. Vastaavasti To-kentän vastaanottajatiedoissa on Tullin tiedot, kun lähetetään sanoma koostavaan sovellukseen, ja sanoman vastaanottavan viranomaisen tai tiedonluovuttajan tiedot, kun koostava sovellus välittää sanoman eteenpäin.

<table>
  <colgroup><col /><col /><col /><col /></colgroup>
  <tbody>
    <tr>
      <th>Elementin nimi</th>
      <th >min..max</th>
      <th >Tyyppi</th>
      <th >Kuvaus</th>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01</td>
      <td >1..1</td>
      <td ></td>
      <td ></td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Charset
      </td>
      <td >0..1</td>
      <td >UnicodeChartsCode</td>
      <td >"UTF-8"</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Fr<br>
      ++OrgId<br>
      +++Id<br>
      ++++OrgId<br>
      +++++Othr<br>
      ++++++Id
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Lähettäjän Y-tunnus. Kun tunnusta verrataan sanoman allekirjoitusvarmenteeseen, tulee ottaa huomioon, että varmenteen sisältämä tunnus voi olla joko Y- tai ALV-tunnuksen muodossa.</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Fr<br>
      ++OrgId<br>
      +++Id<br>
      ++++OrgId<br>
      +++++Othr<br>
      ++++++SchmeNm<br>
      +++++++Cd
      </td>
      <td >1..1</td>
      <td >ExternalOrganisationIdentification1Code</td>
      <td >"Y", organisaatiotunnuksen tyyppi</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Fr<br>
      ++OrgId<br>
      +++CtctDtls<br>
      ++++Nm
      </td>
      <td >0..1</td>
      <td >Max140Text</td>
      <td >Vain viranomaisen kyselysanomassa: Henkilön nimi mahdollista lisäselvityspyyntöä varten</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Fr<br>
      ++OrgId<br>
      +++CtctDtls<br>
      ++++PhneNb
      </td>
      <td >0..1</td>
      <td >PhoneNumber</td>
      <td >Vain viranomaisen kyselysanomassa: Puhelinnumero mahdollista lisäselvityspyyntöä varten</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Fr<br>
      ++OrgId<br>
      +++CtctDtls<br>
      ++++EmailAdr
      </td>
      <td >0..1</td>
      <td >Max2048Text</td>
      <td >Vain viranomaisen kyselysanomassa: Sähköpostiosoite mahdollista lisäselvityspyyntöä varten</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +To<br>
      ++OrgId<br>
      +++Id<br>
      ++++OrgId<br>
      +++++Othr<br>
      ++++++Id
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Vastaanottajan Y-tunnus</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +To<br>
      ++OrgId<br>
      +++Id<br>
      ++++OrgId<br>
      +++++Othr<br>
      ++++++SchmeNm<br>
      +++++++Cd
      </td>
      <td >1..1</td>
      <td >ExternalOrganisationIdentification1Code</td>
      <td >"Y", organisaatiotunnuksen tyyppi</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +BizMsgIdr
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Käyttö standardin mukaisesti</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +MsgDefIdr
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Sanoma-id, kyselysanomassa "auth.001.001.01" ja vastaussanomassa "auth.002.001.01"</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +CreDt
      </td>
      <td >1..1</td>
      <td >ISONormalisedDateTime</td>
      <td >Luomispäivämäärä ja aika. Normalisoitava Z-notaatiolla (UTC)</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Sgntr
      </td>
      <td >0..1</td>
      <td >SignatureEnvelope</td>
      <td >
        
Lähettäjän muodostama [XML-allekirjoitus](#xml-allekirjoitus)        
      </td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Sgntr<br>
      ++Signature<br>
      +++SignatureValue
      </td>
      <td >1..1</td>
      <td >SignatureValueType</td>
      <td >Allekirjoitus</td>
    </tr>
    <tr>
      <td >BusinessApplicationHeaderV01<br>
      +Sgntr<br>
      ++Signature<br>
      +++KeyInfo<br>
      ++++X509Data<br>
      +++++X509Certificate
      </td>
      <td >1..1</td>
      <td >base64Binary</td>
      <td >Sertifikaatti</td>
    </tr>
  </tbody>
</table>

## 6. Kyselysanoma <a name="luku6"></a>

Kyselysanomassa käytetään ISO 20022 sanomaa InformationRequestOpeningV01 [auth.001.001.01](https://github.com/FinnishCustoms-SuomenTulli/account-register-information-query/blob/master/assets/iso20022org/auth.001.001.01.xsd). InformationRequestOpeningV01 sanoman supplementary data -osiossa käytetään kansallista InformationRequestFIN012 (fin.012.001.04) sanomalaajennosta.

Alla luvussa 6.2 on kuvattu, mitä kenttiä käytetään kyselysanomassa. Alisanoman [fin.012.001.04](schemas/fin.012.001.04.xsd) skeema. Esimerkkejä [kyselysanomasta](examples/queries).

### 6.1 Erityyppisten tietojen hakeminen <a name="6-1"></a>

Keskitetystä saldo- ja tilitapahtumatietojärjestelmästä on mahdollista hakea pelkkiä saldotietoja, pelkkiä tilitapahtumatietoja, tai molempia.

[Esimerkkisanoma](examples/general/example_requesting_only_bal_or_entry_or_both.xml) saldo- ja tilitapahtumatietojen kyselystä.

#### Pelkkien tilitapahtumatietojen haku

Käytetään ajantasaisten tilitapahtumatietojen noutamiseen. Sisältää myös keskeneräiset tapahtumat [Tapahtuman tila: "kesken"]

Vastauksen mukana välitetään aina kaikki muut tiedot, paitsi saldoon (bal-elementti) kuuluvat kentät ja erikseen pyydettävät tiedot.

Pelkkiä tilitapahtumatietoja kyseltäessä sanomaan sisällytetään investigationTypeCode: TRAN. 

#### Pelkkien saldotietojen haku

Käytetään luovutushetken saldotietojen noutamiseen. 

Vastauksen mukana välitetään aina kaikki muut tiedot, paitsi tilitapahtumatietoja (entry-elementti) sisältävät kentät ja erikseen pyydettävät tiedot.

Pelkkiä saldotietoja kyseltäessä sanomaan sisällytetään investigationTypeCode: BALN.

#### Saldo- ja tilitapahtumatietojen haku

Käytetään hakuaikavälin tilitapahtumatietojen sekä aikavälin alku- ja loppuhetken saldotiedon noutamiseen. Sisältää myös keskeneräiset tapahtumat [Tapahtuman tila: "kesken"]

Vastauksen mukana välitetään aina kaikki muut tiedot paitsi erikseen pyydettävät tiedot.

Saldo- ja tilitaphtumatietoja kyseltäessä sanomaan sisällytetään erillisinä elementteinä investigationTypeCode: TRAN ja investigationTypeCode: BALN.

### 6.2 InformationRequestOpeningV01 sanoman sisältö <a name="6-2"></a>

<table>
  <colgroup><col /><col /><col /><col /></colgroup>
  <tbody>
    <tr>
      <th>Elementin nimi</th>
      <th >min..max</th>
      <th >Tyyppi</th>
      <th >Kuvaus</th>
    </tr>
    <tr>
      <td >InformationRequestOpeningV01</td>
      <td >1..1</td>
      <td ></td>
      <td ></td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +InvstgtnId
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Tapauksen tunniste</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +LglMndBsis<br>
        ++Prgrph
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Laillisuusperuste</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +CnfdtltySts
      </td>
      <td >1..1</td>
      <td >YesNoIndicator</td>
      <td >aina "true"</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +InvstgtnPrd<br>
        ++Dt<br>
        +++FrDt
      </td>
      <td >1..1</td>
      <td >ISODate</td>
      <td >Hakuaikavälin alkamispäivä</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +InvstgtnPrd<br>
        ++Dt<br>
        +++ToDt
      </td>
      <td >1..1</td>
      <td >ISODate</td>
      <td >Hakuaikavälin päättymispäivä</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SchCrit<br>
        ++Acct<br>
        +++Id<br>
        ++++Id<br>
        +++++IBAN
      </td>
      <td >0..1</td>
      <td >IBAN2007Identifier</td>
      <td >Haettavan tilin IBAN-muotoinen tilinumero.<br>
      Käytetään kun hakukohteena olevalla tilillä on IBAN-muotoinen tilinumero.
      </td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SchCrit<br>
        ++Acct<br>
        +++Id<br>
        ++++Id<br>
        +++++Othr<br>
        ++++++Id
      </td>
      <td >1..1</td>
      <td >Max34Text</td>
      <td >Haettavan tilin tilinumero, jos kyseessä ei ole IBAN-tili.</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SchCrit<br>
        ++Acct<br>
        +++Id<br>
        ++++Id<br>
        +++++Othr<br>
        ++++++SchmeNm<br>
        +++++++Cd
      </td>
      <td >1..1</td>
      <td >ExternalAccountIdentification1Code</td>
      <td >"OTHR", jos hakukohteena ei ole IBAN-tili</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SchCrit<br>
        ++Acct<br>
        +++InvstgtdPties<br>
        ++++Cd
      </td>
      <td >1..1</td>
      <td >InvestigatedParties1Choice</td>
      <td >"ALLP"</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SchCrit<br>
        ++Acct<br>
        +++AuthrtyReqTp<br>
        ++++MsgNmId
      </td>
      <td >1..1</td>
      <td >Max35Text</td>
      <td >Halutun vastaussanoman tunniste. Tilitapahtuma- ja saldotietoja haettaessa camt.052.001.08.</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AuthorityInquiry<br>
        ++++++OfficialId
      </td>
      <td >1..1</td>
      <td >Max140Text</td>
      <td >Kyselyn lähettävän viranomaisen tunniste</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AuthorityInquiry<br>
        ++++++OfficialSuperiorId
      </td>
      <td >1..1</td>
      <td >Max140Text</td>
      <td >Kyselyn hyväksyvän viranomaisen tunniste</td>
    </tr>
        <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AuthorityInquiry<br>
        ++++++OfficialOrgId
      </td>
      <td >1..1</td>
      <td >Max140Text</td>
      <td >Kyselevän viranomaisen organisaation tunniste</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AdditionalSearchCriteria<br>
        ++++++RequestedDataSources
      </td>
      <td >0..*</td>
      <td >Max35Text</td>
      <td >Tiedonluovuttaja, jolle kysely on osoitettu (Y-tunnus)</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AdditionalSearchCriteria<br>
        ++++++InvestigationType
      </td>
      <td >0..2</td>
      <td >InvestigationTypeCode</td>
      <td >Jos haetaan tilitapahtumia, lähetetään elementti arvolla "TRAN". <br>Jos haetaan saldotietoja, lähetetään elementti arvolla "BALN". <br>Jos haetaan sekä tilitapahtuma- että saldotiedot, lähetetään elementti kahdesti, kerran kummallakin arvolla.</td>
    </tr>
    <tr>
      <td >
        InformationRequestOpeningV01<br>
        +SplmtryData<br>
        ++Envlp<br>
        +++Document<br>
        ++++InfReqFin012<br>
        +++++AdditionalTransactionInformation<br>
        ++++++TransactionFieldCode
      </td>
      <td >0..*</td>
      <td >TransactionFieldCode</td>
      <td >
        
Käytetään, jos vastauksessa halutaan palautettavan erikseen pyydettäviä lisätietoja perustietojen lisäksi. Lista hakuun tarvittaessa sisällytettävistä erikseen pyydettävistä tiedoista: [TransactionFieldCode](#6-3) </td>
    </tr>
  </tbody>
</table>

### 6.3 TransactionFieldCode: erikseen pyydettävät lisätiedot <a name="6-3"></a>

| Kuvaus                                | Tietue                                  | Koodi            |
|:--------------------------------------|:----------------------------------------|:-----------------|
| Ilmaisin sisältääkö saldo luottorajan | `BkToCstmrAcctRpt/Rpt/Bal/CdtLine/Incl` | BAL_CDTLINE_INCL |
| Käytettävissä oleva luottoraja        | `BkToCstmrAcctRpt/Rpt/Bal/CdtLine/Amt`  | BAL_CDTLINE_AMT  |

[Esimerkkisanoma](examples/general/example_request_additional_info.xml) erikseen pyydettävistä lisätiedoista.


## 7. Vastaussanoma <a name="luku7"></a>

Vastaussanomassa käytetään ISO 20022 sanomaa InformationRequestResponseV01 [auth.002.001.01](https://github.com/FinnishCustoms-SuomenTulli/account-register-information-query/blob/master/assets/iso20022org/auth.002.001.01.xsd). InformationRequestResponseV01 sanoman supplementary data -osiossa palautetaan ISO 20022 sanoma camt.052.001.08.

Alla luvussa 7.1 on kuvattu, mitä kenttiä käytetään vastaussanoman alisanomassa camt.052.001.08. Alisanoman [camt.052.001.08](schemas/camt.052.001.08.xsd) skeema. Esimerkkejä [vastaussanomasta](examples/queries). 

Vastaussanoman sisältö on samanlainen kaikilla tiedonluovuttajilla riippumatta siitä, onko tiedonluovuttaja toteuttanut tiedonhakujärjestelmän vai rajapinnan tilirekisteriin. Ainoastaan vastaussanoman toimitustavat eroavat toisistaan. 

### 7.1 Alisanoman camt.052.001.08 sisältö <a name="7-1"></a>


<table>
  <colgroup><col /><col /><col /></colgroup>
  <tbody>
    <tr>
      <th>Elementin nimi</th>
      <th>Tyyppi</th>
      <th>Kuvaus</th>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +GrpHdr<br>
        ++MsgId
      </td>
      <td>Max35Text</td>
      <td>Viestin yksilöllinen tunniste.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +GrpHdr<br>
        ++CreDtTm
      </td>
      <td>ISODateTime</td>
      <td>Viestin luontipäivämäärä ja -aika.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +GrpHdr<br>
        ++AddtlInf
      </td>
      <td>Max500Text</td>
      <td>Lähettäjän antamat lisätiedot.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +Rpt<br>
        ++Id
      </td>
      <td>Max35Text</td>
      <td>Raportin yksilöllinen tunniste.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +Rpt<br>
        ++CreDtTm
      </td>
      <td>ISODateTime</td>
      <td>Raportin luontipäivämäärä ja -aika.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +Rpt<br>
        ++FrToDt<br>
        +++FrDtTm
      </td>
      <td>ISODateTime</td>
      <td>Raportin kattaman aikavälin alkupäivä.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +Rpt<br>
        ++FrToDt<br>
        +++ToDtTm
      </td>
      <td>ISODateTime</td>
      <td>Raportin kattaman aikavälin päättymispäivä.</td>
    </tr>
    <tr>
      <td>
        BkToCstmrAcctRpt<br>
        +Rpt<br>
        ++Acct<br>
        +++Id<br>
        ++++IBAN
      </td>
      <td>IBAN2007Identifier</td>
      <td>Tilin IBAN, josta raportti on laadittu.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Acct<br>+++Othr<br>++++Id</td>
      <td>Max34Text</td>
      <td>Tilinumero muu kuin IBAN, josta raportti on laadittu.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++CdtDbtInd</td>
      <td>CreditDebitCode</td>
      <td>Ilmaisee, onko tapahtuma kredit tai debit.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++RvslInd</td>
      <td>TrueFalseIndicator</td>
      <td>Ilmaisee, onko tapahtuma korjaus.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++BookgDt<br>++++Dt</td>
      <td>ISODate</td>
      <td>Päivämäärä, jolloin tapahtuma kirjattiin tilille.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++Amt</td>
      <td>ActiveOrHistoricCurrencyAndAmount</td>
      <td>Tapahtuman rahamäärä ja valuutta.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++ValDt<br>++++ValDt (Dt)</td>
      <td>ISODate</td>
      <td>Tapahtuman arvopäivä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++AcctSvcrRef</td>
      <td>Max35Text</td>
      <td>Tiliä hoitavan laitoksen antama viite.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++BkTxCd<br>++++Prtry<br>+++++Cd</td>
      <td>Max35Text</td>
      <td>Pankin sisäinen tapahtumakoodi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++BkTxCd<br>++++Domm<br>+++++Cd</td>
      <td>ExternalBankTransactionDomain1Code</td>
      <td>Pankkitapahtuman standardoitu koodiperhe.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++sts<br>++++Cd</td>
      <td>ExternalEntryStatus1Code</td>
      <td>Tapahtuman tila (esim. kirjattu, kesken).</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++Btch<br>+++++MsgId</td>
      <td>Max35Text</td>
      <td>Koontitapahtuman tunniste.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++Btch<br>+++PmtInfId</td>
      <td>Max35Text</td>
      <td>Maksutiedon tunniste.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++Btch<br>+++NbOfTxs</td>
      <td>Max15NumericText</td>
      <td>Koontitapahtumien lukumäärä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++Btch<br>+++TtlAmt</td>
      <td>ActiveOrHistoricCurrencyAndAmount</td>
      <td>Koontitapahtumien kokonaissumma.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>++NtryDtls<br>+++AmtDtls<br>++++TxAmt<br>+++++Amt</td>
      <td>ActiveOrHistoricCurrencyAndAmount</td>
      <td>Tapahtuman summa.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++TxDtls<br>+++AmtDtls<br>++++TxAmt<br>+++++CcyXchg<br>++++++UnitCcy</td>
      <td>ActiveOrHistoricCurrencyCode</td>
      <td>Tapahtuman alkuperäinen valuutta.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++AmtDtls<br>++++++TxAmt<br>+++++++CcyXchg<br>++++++++XchgRate</td>
      <td>BaseOneRate</td>
      <td>Käytetty valuuttakurssi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RmtInf<br>++++++Ustrd</td>
      <td>Max140Text</td>
      <td>Rakenteeton viestitieto.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RmtInf<br>++++++Strd<br>+++++++CdtrRefInf<br>++++++++Ref</td>
      <td>Max35Text</td>
      <td>Saajan viitetiedot.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++Refs<br>++++++InstrId</td>
      <td>Max35Text</td>
      <td>Alkuperäisen osapuolen antama tunniste.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++Purp<br>++++++(Cd/Prtry)</td>
      <td>ExternalPurpose1Code</td>
      <td>Tapahtuman syy tai tarkoitus.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++DbtrAcct<br>+++++++Id<br>++++++++IBAN</td>
      <td>IBAN2007Identifier</td>
      <td>Maksajan tilin IBAN.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++CdtrAcct<br>+++++++Id<br>++++++++IBAN</td>
      <td>IBAN2007Identifier</td>
      <td>Saajan tilin IBAN.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++Dbtr<br>+++++++Pty<br>++++++++Nm</td>
      <td>Max140Text</td>
      <td>Maksajan nimi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++Cdtr<br>+++++++Pty<br>++++++++Nm</td>
      <td>Max140Text</td>
      <td>Saajan nimi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++CdtrAcct<br>+++++++Tp<br>++++++++Cd</td>
      <td>ExternalCashAccountType1Code</td>
      <td>Saajan tilin tyypin koodi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdPties<br>++++++CdtrAcct<br>+++++++Tp<br>++++++++Prtry</td>
      <td>Max35Text</td>
      <td>Saajan tilin tyypin kuvaus.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdAgts<br>++++++DbtrAgt<br>+++++++FinInstnId<br>++++++++BICFI</td>
      <td>BICFIDec2014Identifier</td>
      <td>Maksajan pankin BIC-koodi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Ntry<br>+++NtryDtls<br>++++TxDtls<br>+++++RltdAgts<br>++++++CdtrAgt<br>+++++++FinInstnId<br>++++++++BICFI</td>
      <td>BICFIDec2014Identifier</td>
      <td>Saajan pankin BIC-koodi.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++TxsSummry<br>+++TtlNtries<br>++++NbOfNtries</td>
      <td>Max15NumericText</td>
      <td>Tapahtumien kokonaismäärä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++TxsSummry<br>+++TtlNtries<br>++++TtlNetNtry<br>+++++Amt</td>
      <td>NonNegativeDecimalNumber</td>
      <td>Tapahtumien nettosumma.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++TxsSummry<br>+++TtlCdtNtries<br>++++NbOfNtries</td>
      <td>Max15NumericText</td>
      <td>Kredit-tapahtumien lukumäärä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++TxsSummry<br>+++TtlDbtNtries<br>++++NbOfNtries</td>
      <td>Max15NumericText</td>
      <td>Debit-tapahtumien lukumäärä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++Tp<br>++++CdOrPrtry<br>+++++Cd</td>
      <td>ExternalBalanceType1Code</td>
      <td>Saldotyypin koodi (esim. alku-, loppusaldo).</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++Amt</td>
      <td>ActiveOrHistoricCurrencyAndAmount</td>
      <td>Saldon määrä</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++CdtDbtInd</td>
      <td>CreditDebitCode</td>
      <td>Ilmaisee, onko saldo kredit vai debit.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++Dt<br>++++Dt</td>
      <td>DateAndDateTime2Choice</td>
      <td>Saldon päivämäärä.</td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++CdtLine<br>++++Incl</td>
      <td>TrueFalseIndicator</td>
      <td>
        
Ilmaisin, sisältääkö saldo luottorajan. Erikseen pyydettävä lisätieto, joka palautetaan ainoastaan jos sitä on pyydetty kyselyssä, ks. [TransactionFieldCode](#6-3)
      </td>
    </tr>
    <tr>
      <td>BkToCstmrAcctRpt<br>+Rpt<br>++Bal<br>+++CdtLine<br>++++Amt</td>
      <td>ActiveOrHistoricCurrencyAndAmount</td>
      <td>
      
Käytettävissä oleva luottoraja. Erikseen pyydettävä lisätieto, joka palautetaan ainoastaan jos sitä on pyydetty kyselyssä, ks. [TransactionFieldCode](#6-3)
      </td>
    </tr>
  </tbody>
</table>


## 8. Virhetilanteet <a name="luku8"></a>


<table>
  <colgroup><col /><col /><col /><col /></colgroup>
  <tbody>
    <tr>
      <th>Virhetilanne</th>
      <th >faultcode</th>
      <th  colspan="1">faultstring</th>
      <th  colspan="1">detail</th>
      <th  colspan="1">Virhekoodi</th>
    </tr>
    <tr>
      <td >Asynkronisesti aloitettu kysely on kadonnut</td>
      <td >SOAP-ENV:Server</td>
      <td  colspan="1">The query has been lost. Please re-send initial query.</td>
      <td  colspan="1"><code>&lt;errorcode&gt;1&lt;/errorcode&gt;</code></td>
      <td>1</td>
    </tr>
    <tr>
      <td >XML-allekirjoitus on virheellinen</td>
      <td >SOAP-ENV:Client</td>
      <td  colspan="1">The provided signature is invalid.</td>
      <td  colspan="1"><code>&lt;errorcode&gt;2&lt;/errorcode&gt;</code></td>
      <td>2</td>
    </tr>
    <tr>
      <td >Transaktio hylätty liian tiheän pollausvälin johdosta</td>
      <td >SOAP-ENV:Client</td>
      <td  colspan="1">Too many requests</td>
      <td  colspan="1"><code>&lt;errorcode&gt;3&lt;/errorcode&gt;</code></td>
      <td>3</td>
    </tr>
    <tr>
      <td >Sanomassa on validointivirheit&auml;, esimerkiksi virheellinen investigation period</td>
      <td >SOAP-ENV:Client</td><td  colspan="1">Bad Request</td>
      <td  colspan="1">
        <p>1 kpl ValidationError-elementti&auml; per validointivirhe esim.</p>
        <p><code>&lt;errorcode&gt;4&lt;/errorcode&gt;</code><br /><code>&lt;ValidationError&gt;</code><code>Validaatiovirheen kuvaus&lt;/ValidationError&gt;</code></p>
      </td>
      <td>4</td>
    </tr>
    <tr>
      <td >Sanoman indikoimalla käyttäjällä ei ole käyttöoikeutta</td>
      <td >SOAP-ENV:Client</td><td  colspan="1">Unauthorized</td>
      <td  colspan="1">
        <p><code>&lt;errorcode&gt;5&lt;/errorcode&gt;</code><br /></p>
      </td>
      <td>5</td>
    </tr>
    <tr>
      <td >Vastaussanoman koko on liian suuri (yli 5 Mb)</td>
      <td >SOAP-ENV:Client</td><td  colspan="1">Query response size is too large. Please refine the query.</td>
      <td  colspan="1">
        <p><code>&lt;errorcode&gt;6&lt;/errorcode&gt;</code><br /></p>
      </td>
      <td>6</td>
    </tr>
    <tr>
      <td >Vastaussanoma sisältää useita osumia</td>
      <td >SOAP-ENV:Client</td><td  colspan="1">Query response has multiple hits. Please refine the query.</td>
      <td  colspan="1">
        <p><code>&lt;errorcode&gt;7&lt;/errorcode&gt;</code><br /></p>
      </td>
      <td>7</td>
    </tr>
        <tr>
      <td >Vastausta ei ole toimitettu kyselyn käsittelyaikarajan sisällä. Kysely on suljettu.</td>
      <td >SOAP-ENV:Server</td><td  colspan="1">Query has expired and is closed</td>
      <td  colspan="1">
        <p><code>&lt;errorcode&gt;8&lt;/errorcode&gt;</code><br /></p>
      </td>
      <td>8</td>
    </tr>
    <tr>
      <td  colspan="1">Palvelimen virhe</td>
      <td  colspan="1">SOAP-ENV:Server</td>
      <td  colspan="1">Internal Server Error</td>
      <td  colspan="1"><code>&lt;errorcode&gt;0&lt;/errorcode&gt;</code></td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Jos tiedonhakujärjestelmä ei vastaa aikarajan kuluessa, palauttaa koostava sovellus viranomaiselle virhekoodin 1.


