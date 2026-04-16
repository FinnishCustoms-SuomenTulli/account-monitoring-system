# Koostavan sovelluksen v2 rajapinta

## Tiedonhyödyntäjille

Koostavaan sovellukseen tehtävät kyselyt tehdään uuden rajapinnan kautta uudella skeemalla.
   - Vanha: wsdl_root.002
   - Uusi: aggregator.002

Uudessa rajapinnassa erona vanhaan on se, että kaikki query-, result- ja status-kyselyt tehdään yhden osoitteen kautta.
Eri sanomatyypit on eroteltu skeemassa omiksi operaatioikseen.
```
<wsdl:operation name="Query"> 
<wsdl:operation name="Status">
<wsdl:operation name="Result">
```

Lisäksi uudessa rajapinnassa tulee käyttää alisanoman fin.012 uudempaa versiota fin.012.001.04

## Tiedonluovuttajille

Pankki- ja maksutilien valvontajärjestelmän kautta saapuville kyselyille ja luovutettaville vastauksille on julkaistu uusi skeema.
   - Vanha: wsdl_root.002
   - Uusi: register.003

Lisäksi saapuville kyselyille aletaan käyttää alisanoman fin.012 uutta versiota fin.012.001.04.

## Käyttöönotto tiedonluovuttajalle

Uusi rajapinta tukee sekä vanhaa että uutta tiedonluovuttajien rajapintaan lähetettävän sanoman versiota. Koostava sovellus huolehtii, että tiedonluovuttajalle lähetetään heidän rajapintansa mukainen sanomaversio.
Kun tiedonluovuttaja on valmis siirtymään käyttämään uutta skeema versiota, päivityksen aikataulu täytyy ilmoittaa Tullille postilaatikkoon tilirekisteri(at)tulli.fi. Tulli tekee tiedonluovuttajan ilmoittaman aikataulun mukaisesti tarvittavat konfiguraatiomuutokset. Tämän jälkeen tiedonluovuttajalle ohjataan uuden skeeman mukaisia sanomia vanhan sijaan.

**Ennen uuden skeeman käyttöönottoa tuotannossa on tiedonluovuttajan päivitettävä testirajapinta käyttämään uutta skeema versiota. Tämän jälkeen Tulli suorittaa tiedonluovuttajakohtaisen hyväksymistestauksen tilitietokyselyille.**

## Käyttöönotto tiedonhyödyntäjälle

Uuden rajapinnan kautta saa kaikkien tiedonluovuttajien vastaukset. Vanhasta rajapinnasta saa vain niiden tiedonluovuttajien vastaukset, jotka eivät vielä ole siirtyneet käyttämään uutta skeemaversiota. Tiedonhyödyntäjän siirtyessä käyttämään uutta rajapintaa käyttöönotto ei vaadi muutoksia Tullin puolella. Uusi rajapinta toimii samoilla luvituksilla ja varmenteilla kuin vanha rajapinta. 

**Ennen uuden rajapinnan käyttöönottoa tuotannossa on tiedonhyödyntäjän syytä käydä läpi kaikki testitapaukset testiympäristön rajapintaa vasten. Kun tiedonhyödyntäjä katsoo testauksen läpäistyksi, tulisi hänen ilmoittaa Tullille tilirekisteri(at)tulli.fi tuotantorajapinnan käytön aloituksen aikataulu, jotta käytönaloituksessa voidaan tukea tarvittaessa.**

![Rajapintasiirtymä](https://github.com/FinnishCustoms-SuomenTulli/account-monitoring-system/blob/main/diagrams/rajapintasiirtyma-fi.png)

# Aggregating application interface v2

## For data users

Queries to aggregating application use the new interface with the new schema.
   - Old: wsdl_root.002
   - New: aggregator.002

The difference in the new interface compared to the old one is that all query, result and status queries use the same address. 
The different message types are divided into their own separate operations in the schema. 
```
<wsdl:operation name="Query"> 
<wsdl:operation name="Status">
<wsdl:operation name="Result">
```

In addition, the new version of fin.012 submessage fin.012.001.04 must be used in the new interface.

## For data suppliers

A new schema has been released for  queries and responses sent through the bank and payment account monitoring system.
   - Old: wsdl_root.002
   - New: register.003

In addition, the use of new version of fin.012 submessage fin.012.001.04 is starting for arriving queries.

## Deployment for data suppliers

The new interface supports both the old and new version of the message that is sent to the data supplier's interface. The aggregating application makes sure that data users receive message versions that match their interface. When the data supplier is ready to start using the new schema version, they need to inform Customs about the update schedule to the email address tilirekisteri(at)tulli.fi. Customs makes the necessary configuration changes according to the schedule the data supplier has given. After the changes the data supplier is forwarded messages in line with the new schema instead of the old one.

**Before the new schema is deplyed to production the data supplier must update their test interface to use the new schema version. After that Customs will perform acceptance testing of account information queries for the data supplier.**

## Deployment for data users

All data suppliers' responses are available via the new interface. Via the old interface, only responses from the data suppliers who have not yet deployed the new schema version are available. When the data user is ready to start using the new interface the deployment does not require any changes by Customs. The new interface uses the same permissions and certificates as the old one. 

**Before deploying the new interface to production, the data user should run through the test cases using the test environment interface. When the data user considers the testing is passed, they should inform Customs at tilirekisteri(at)tulli.fi about the schedule for starting production interface to get support for the deployment if needed.**

![Interface transition](https://github.com/FinnishCustoms-SuomenTulli/account-monitoring-system/blob/main/diagrams/rajapintasiirtyma-en.png)
