# Valintarakenne

Tässä moduulissa opit kirjoittamaan ohjelmia, jotka voivat haarautua vaihtoehtoisiin suorituspolkuihin. Näin
saat ohjelman reagoimaan eri tavoin erilaisiin syötteisiin. Haarautuminen voi perustua myös laskutoimituksen
tulokseen tai mihin tahansa seikkaan ohjelman sisäisessä tilassa.

Haarautuminen toteutetaan valintarakenteen avulla. Valintarakenne on ohjelmointikielten välttämätön ohjausrakenne,
ja sen hallinta kasvattaa huomattavasti ohjelmoijan ilmaisuvoimaa.

## Valintarakenne

Oletetaan, että tulet kahvilaan tilataksesi latten. Latte maksaa viisi euroa, ja haluat maksaa käteisellä.
Tässä vaiheessa joudut tekemään päätöksen siitä,
riittävätkö rahasi latten ostoon. Tämä valintatilanne voidaan kuvata pseudokoodina:

```monospace
jos rahaa_taskussa >=5
	osta latte
```

Pseudokoodista nähdään, että päätös tehdään ehdon toteutumisen perusteella. Ehtona on tässä tapauksessa se, että
rahaaa on vähintään viisi euroa. Ehto voi olla tosi tai epätosi: jos rahaa on esimerkiksi seitsemän euroa, on lauseke muotoa 
7>=5, joka on tosi. Toisaalta jos taskusta löytyy vain 4,85 euroa, on ehto muotoa 4,85>=5, joka on epätosi.

Ehdollisesti suoritettava ohjelmanosa (eli latten osto) suoritetaan täsmälleen silloin, kun ehto on tosi.

Python-kielessä ehdollisesti suoritettava ohjelmanosa toteutetaan if-lauseen avulla. Lauseen rakenne on seuraava:

```monospace
if (ehto):
	ehdollisesti suoritettava lohko
```

Edellä ehto on looginen lauseke, jonka totuusarvo voidaan laskea. Totuusarvo on joko tosi tai epätosi. Sen perusteella
suoritus etenee:
1. Jos ehto on tosi, suoritetaan ehdollisesti suoritettava lohko.
2. Jos ehto on epätosi, hypätään valintarakenteen jälkeiseen lauseeseen.

Ehdollisesti suoritettavaan lohkoon kuuluvat lauseitä on sisennettävä yhden askeleen verran. Python-kielessä yhden askeleen
sisennys saadaan kirjoittamalla rivin alkuun neljä välilyöntiä. Käytännössä neljää välilyöntiä ei kannata
tehdä välilyöntinäppäintä napsuttelemalla vaan painamalla yhden kerran sarkainnäppäintä eli Tab-näppäintä.
Koodin sisentäminen on tärkeä työväline Python-kielessä: sillä ilmaistaan ohjelman sisäinen hierarkia. Tässä tapauksessa
yhden askeleen sisennys ilmaisee, mitkä lauseet kuuluvat funktion runkoon. Python-kielessä koodin oikea sisentäminen
on pakollista, ja sivutuotteena se tekee koodista myös havainnollisemman ja helpommin luettavan. Tässä Python poikkeaa
monista tunnetuista ohjelmointikielistä, joissa koodin sisentäminen on kielen syntaksin näkökulmasta vapaaehtoista. 

## Ehdollisesti suoritettava ohjelmanosa

Kirjoitetaan ensimmäinen esimerkki valintarakennetta käyttävästä ohjelmasta. Ohjelma kysyy käyttäjältä 
taskussa olevan rahamäärän ja ilmoittaa tälle, jos rahat riittävät viiden euron hintaisen latten ostoon.
Jos rahat eivät riitä, ohjelma ei ilmoita mitään:

```python
rahat = float(input("Anna rahamäärä: "))
if rahat>=5:
    print("Voit ostaa latten.")
```

Kokeillaan ohjelman toimintaa erilaisilla syötteillä. Ehdollisesti suoritettava lohko suoritetaan, kun rahat riittävät:
```monospace
Anna rahamäärä: 5.45
Voit ostaa latten.
```

Sitten kokeillaan tilannetta, jossa rahaa on juuri ja juuri riittävästi:
```monospace
Anna rahamäärä: 5
Voit ostaa latten.
```
Tämä oli tärkeä kokeilu, sillä rajatapausten käsittelyssä tulee helposti ohjelmointivirheitä. Jos olisimme kirjoittaneet ehdon
vahingossa muotoon `rahat>5` olisi latte jäänyt virheellisesti toimivan ohjelman mukaan ostamatta.

Lopuksi tarkistetaan, että ehdollista lohkoa ei suoriteta, kun rahat eivät riitä:
```monospace
Anna rahamäärä: 4.95

```



## Vertailuoperaattorit

Edellä olevassa latte-esimerkissä ehto ilmaistiin suurempi kuin -vertailuoperaattorin (`>=`) avulla. Ehtojen
ilmaisemiseksi Python-kielessä voidaan käyttää seuraavia vertailuoperaattoreita:


| Merkintä | Vertailuoperaattori        | 
|----------|----------------------------|
| \>       | suurempi kuin              |
| \<       | pienempi kuin              |
| >=       | suurempi tai yhtäsuuri kuin | 
| <=       | pienempi tai yhtäsuuri kuin | 
| ==       | yhtä suuri kuin            | 
| !=       | eri suuri kuin             | 

Vertailuoperaattoreiden käyttö lukujen tapauksessa on suoraviivaista.

Operaattoreita on mahdollista käyttää myös merkkijonotyyppisille lausekkeille.
Esimerkiksi merkkijonoille `m1` ja `m2` lauseke `m1 < m2` on tosi silloin, jos merkkijono `m1` on
aakkosjärjestyksessä ennen merkkijonoa `m2`.

Seuraavassa esimerkissä verrataan merkkijonojen yhtäsuuruutta:

```python
suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")

Huomaa, että yhtäsuuruusvertailussa on kaksi yhtäsuuruusmerkkiä (`==`). Yhdellä yhtäsuuruusmerkillä ilmaistaisiin
sijoituslause.
```

Ohjelma ilmoittaa, jos suutarilla ja räätälillä on sama nimi:
``` monospace
Anna suutarin nimi: Tiina
Anna räätälin nimi: Tiina
Hyvänen aika! Suutari ja räätäli ovat kaimoja!
```

## Loogiset operaattorit

## Kaksi toisensa poissulkevaa ohjelmanosaa

## Monen vaihtoehdon valintarakenne


