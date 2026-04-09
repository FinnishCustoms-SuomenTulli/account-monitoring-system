# Koostavan sovelluksen v2 rajapinta

## Tiedonhyödyntäjille

Koostavaan sovellukseen tehtävät kyselyt tehdään uuden rajapinnan kautta uudella skeemalla
   - Vanha: wsdl_root.002
   - Uusi: aggregator.002

Uudessa rajapinnassa erona on, että kaikki query-, result- ja status-kyselyt tehdään yhden osoitteen kautta.
Eri sanomatyypit on eroteltu skeemassa omiksi operaatioikseen.
```
<wsdl:operation name="Query"> 
<wsdl:operation name="Status">
<wsdl:operation name="Result">
```

Lisäksi uudessa rajapinnassa tulee käyttää alisanoman fin012 uudempaa versiota fin012.001.04

## Tiedonluovuttajille

Pmj kautta saapuville kyselyille ja luovutettaville vastauksille on julkaistu uusi skeema
   - Vanha: wsdl_root.002
   - Uusi: register.003

Lisäksi PMJ kautta saapuville kyselyille aletaan hyödyntämään alisanoman fin012 uutta versiota fin012.001.04


# Aggregating application interface v2

## For data users

Queries to aggregating application are done via the new interface using the new schema
   - Old: wsdl_root.002
   - New: aggregator.002

The difference in the new interface is that all query, result and status queries use the same address Uudessa rajapinnassa erona on, että kaikki query-, result- ja status-kyselyt tehdään yhden osoitteen kautta.
Eri sanomatyypit on eroteltu skeemassa omiksi operaatioikseen.
```
<wsdl:operation name="Query"> 
<wsdl:operation name="Status">
<wsdl:operation name="Result">
```

Lisäksi uudessa rajapinnassa tulee käyttää alisanoman fin012 uudempaa versiota fin012.001.04

## For data suppliers

Pmj kautta saapuville kyselyille ja luovutettaville vastauksille on julkaistu uusi skeema
   - Vanha: wsdl_root.002
   - Uusi: register.003

Lisäksi PMJ kautta saapuville kyselyille aletaan hyödyntämään alisanoman fin012 uutta versiota fin012.001.04
