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
