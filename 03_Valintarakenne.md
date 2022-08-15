# Valintarakenne (if)

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

Python-kielessä ehdollisesti suoritettava ohjelmanosa toteutetaan `if`-lauseen avulla. Lauseen rakenne on seuraava:

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
yhden askeleen sisennys ilmaisee, mitkä lauseet kuuluvat ehdollisesti suoritettavaan osaan. Python-kielessä koodin oikea sisentäminen
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

Loogisia operaattoreita on sallittua ketjuttaa. Seuraava lauseke on tosi silloin, jos henkilön pituus on
vähintään 170 mutta alle 180 cm: `170 <= pituus < 180`.

Operaattoreita on mahdollista käyttää myös merkkijonotyyppisille lausekkeille.
Esimerkiksi merkkijonoille `m1` ja `m2` lauseke `m1 < m2` on tosi silloin, jos merkkijono `m1` on
aakkosjärjestyksessä ennen merkkijonoa `m2`.

Seuraavassa esimerkissä verrataan merkkijonojen yhtäsuuruutta:

```python
suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")
```

Huomaa, että yhtäsuuruusvertailussa on kaksi yhtäsuuruusmerkkiä (`==`). Yhdellä yhtäsuuruusmerkillä ilmaistaisiin
sijoituslause.


Ohjelma ilmoittaa, jos suutarilla ja räätälillä on sama nimi:
``` monospace
Anna suutarin nimi: Tiina
Anna räätälin nimi: Tiina
Hyvänen aika! Suutari ja räätäli ovat kaimoja!
```

## Loogiset operaattorit

Aiemmissa esimerkeissä valintarakenteen ehto voitiin ilmaista yksinkertaisella tavalla vertailuoperaattorien
avulla. Toisinaan ehto on monimutkaisempi: se saattaa esimerkiksi koostua useasta yksittäisestä ehdosta,
joista jokaisen on oltava tosi, jotta valintaehto kokonaisuudessaan olisi tosi. Tällaisia rakenteisia ehtoja voidaan koostaa
loogisten operaattorien avulla.

Python kielessä on seuraavat loogiset operaattorit:

| Merkintä | Looginen operaattori            | 
|----------|---------------------------------|
| and      | ja ("molemmat")                 |
| or       | tai ("jompikumpi tai molemmat") |
| not      | negaatio ("ei")                 | 

Oletetaan, että  `a` ja `b` ovat loogisia lausekkeita, joiden arvot siis ovat joko tosi tai epätosi. Tällöin:
- lauseke `a and b` on tosi täsmälleen silloin, kun sekä lauseke `a` että lauseke `b` ovat tosia.
- lauseke `a or b` on tosi täsmälleen silloin, kun vähintään jompikumpi lausekkeista `a` ja `b` on tosi.
- lauseke `not a` on tosi täsmälleen silloin, kun lauseke `a` on epätosi.

Edellä mainituista operaatioista not-operaattoria sovelletaan ensin, sen jälkeen and-operaattoria ja viimeiseksi
or-operaattoria. Laskujärjestystä voidaan muuttaa sulkeilla.

Esimerkkejä:
- Lauseke `a or b and c` on tosi silloin, kun joko `a` on tosi tai sekä `b` että `c` ovat tosia.
- Lauseke `(a or b)` and `c` on tosi silloin, kun vähintään jompikumpi lausekkeista `a` tai `b` on tosi ja sen lisäksi lauseke `c` on tosi.
- Lauseke `a and not b` on tosi silloin, kun `a` on tosi ja `b` on epätosi.

Tarkastellaan esimerkkiohjelmaa, joka ilmoittaa, jos lääkettä saa antaa potilaalle. Lääkkeen käyttö on sallittua,
kun potilas on aikuinen. Käyttö on sallittua myös, jos potilas on vähintään 15-vuotias ja hänen painonsa on vähintään 55 kiloa.
Seuraava ohjelma kysyy aluksi potilaan iän. Jos ikä on vähintään 15 mutta alle 18 vuotta, ohjelma kysyy myös painon.
Lopuksi ohjelma ilmoittaa käyttäjälle, jos lääkkeen käyttö on sallittua.

```python
ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if (ikä >=18 or ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua.")
```

Kokeillaan ohjelman toimintaa 17-vuotiaalle, 55 kiloa painavalle henkilölle:
```monospace
Anna ikä: 17
Anna paino (kg): 55
Lääkkeen käyttö on sallittua.
```

Alempaa `if`-lausetta tarkasteltaessa saattaa huomio kiinnittyä siihen, että paino on määritelty
vain niille henkilöille, joiden ikä on 15, 16 tai 17 vuotta. Muilta painoa ei ole kysytty, eikä
tuota muuttujaa ole määritelty. Pythonissa on kuitenkin piirre, jota tässä voidaan hyödyntää: loogisen lausekkeen arvon laskeminen
lopetetaan heti, kun arvo on saatu selville. Siinä tapauksessa, että ikä on vähintään 18 vuotta, on `or`-lausekkeen
vasen puoli tosi, ja koko lausekkeen arvo tosi. Painotietoa ei tällöin tarvita loogisen lausekkeen arvon laskemiseksi.
Silloin jos ikä oli alle 18 vuotta, siirrytään laskemaan `or`-sanan oikealla puolella olevan lausekkeen arvoa. Jos ikä on alle
15 vuotta, on sekä `or`-sanan vasemmalla että oikealla puolella olevien lausekkeiden arvo on epätosi ja
koko `or`-lausekkeen arvo sen vuoksi epätosi. Painotieto
luetaan vain silloin, jos tiedetään, että ikä on vähintään 15 ja alle 18 vuotta - ja juuri näissä tapauksissa kyseinen muuttuja on
määritelty. Tätä Python-kielen piirrettä kutsutaan oikosulkemiseksi (*short-circuiting*).


## Kaksi toisensa poissulkevaa vaihtoehtoa

Edellä olevassa lääkkeen käyttöä koskevassa esimerkkiohjelmassa on se heikkous, että ohjelma ei anna mitään tulostetta
niissä tapauksissa, kun lääkkeen käyttö on kiellettyä. Ohjelma toimisi käyttäjän näkökulmasta paremmin, jos se
tuottaisi aina vastauksen.

Ohjelmaan halutaan siis lisätä toinen ehdollisesti suoritettava lohko, johon mennään silloin, jos alkuperäinen
ehto oli epätosi. Tämä voidaan tehdä lisäämällä `if`-lauseeseen `else`-haara.

`Else`-haaran sisältävän ehtolauseen toimintaidea on tämä:
```monospace
if (ehto):
    lohko, joka suoritetaan, jos ehto on tosi
else:
    lohko, joka suoritetaan jos ehto on epätosi
```

Lisätään `else`-haara lääke-esimerkkiin:

```python
ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if (ikä >=18 or ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkettä ei saa käyttää.")
```

Esimerkissä oleva `else`-haara liittyy jälkimmäiseen `if`-lauseeseen. Yleisesti `else`-haara tulkitaan liittyväksi viimeiseen `if`-lauseeseen,
joka on ohjelmassa sisennetty samalle tasolle kuin `else`-haara.

Tarkastellaan ohjelman tuottamia tulosteita eri syötteillä:

```monospace
Anna ikä: 18
Lääkkeen käyttö on sallittua.
```

```monospace
Anna ikä: 16
Anna paino (kg): 61
Lääkkeen käyttö on sallittua.
```

```monospace
Anna ikä: 13
Lääkettä ei saa käyttää.
```

```monospace
Anna ikä: 17
Anna paino (kg): 52
Lääkettä ei saa käyttää.
```


## Monta vaihtoehtoa

Tarkastellaan lopuksi tilannetta, jossa valittavia vaihtoehtoja on useita, ja jokaiselle määritetään oma ehtonsa.
Tämä toteutetaan `elif`- haarojen avulla. Sana on lyhenne sanoista "else if".

Seuraava ohjelma kysyy käyttäjän iän ja ilmoittaa hänelle, onko tämä eläkeikäinen, työikäinen, koululainen vai pikkulapsi.
(Ikärajojen osalta tässä vedetään mutkat suoriksi ja oletetaan, että kukin elämänvaihe alkaa täsmälleen tietyssä iässä; oikeastihan
näin ei ole.)

```python
ikä = int(input("Anna ikäsi: "))
if ikä>=65:
    print("Olet eläkeiässä.")
elif ikä>=18:
    print("Olet työiässä.")
elif ikä>=7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")
```

Kokeillaan toimintaa antamalla iäksi 23 vuotta:
```monospace
Anna ikäsi: 23
Olet työiässä.
```

Miten `elif`-haaroja sisältävä rakenne toimii? Suoritus etenee seuraavasti:

1. Aluksi testataan, onko ikä vähintään 65 vuotta. Jos näin on, suoritetaan ehdollinen lohko, jonka jälkeen suoritus päättyy.
2. Jos ensimmäinen ehto oli epätosi (eli ikä ei ole vähintään 65 vuotta), testataan onko ikä vähintään 18 vuotta. Tätä ehtoa testattaessa
tiedetään jo, että ikä on alle 65 vuotta, joten tähän ehtoon ei tarvitse lisätä ylärajaa iälle. Jos ehto on tosi, suoritetaan haaraan
liittyvä ehdollinen lohko, ja suoritus päättyy.
3. Jos kumpikaan testatuista ehdoista ei ollut tosi, on ikä alle 18 vuotta. Kolmannessa haarassa testataan, onko ikä vähintään seitsemän vuotta
   (eli käytännössä 7-17 vuotta). Jos näin on, suoritetaan kolmas ehdollinen lohko ja suoritus päättyy.
4. Jos ikä ei ollut edes 7 vuotta, suoritetaan `else`-haarassa oleva ehdollinen lohko.

Ohjelma siis kirjoitettiin siten, että ensimmäisen haaran kireää ehtoa löysätään vaihe vaiheelta, jolloin iän ylärajoja ei tarvitse
haarojen ehtoihin kirjoittaa. Ne voitaisiin toki kirjoittaa, mutta se olisi tarpeetonta ja lisäisi uuden mahdollisuuden
tehdä ohjelmointivirhe.
