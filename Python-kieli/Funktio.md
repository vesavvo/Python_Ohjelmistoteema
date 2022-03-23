# Funktiot

Tässä moduulissa opit kirjoittamaan Python-kielen funktioita. Funktiot ovat yleiskäyttöisiä ohjelmanosia,
joita voit käyttää toistuvasti.

Funktioita käyttämällä vältyt tilanteelta, jossa joutuisit kirjoittamaan tai kopioimaan
saman tai samankaltaisen ohjelmakoodin ohjelman eri kohtiin. Saman ohjelmakoodin
toistamista tulee ohjelmoinnissa aina välttää. Ohjelmakoodin toisteisuus tekee ohjelmasta monimutkaisemman ja vaikeammin
muokattavan: jos koodi muuttuu, on muutos tehtävä useampaan kuin yhteen paikkaan. Toistuvien ohjelmanosien koodaminen
funktioiksi ratkaisee tämän ongelman.

Funktiot ovat aliohjelmia, joita kutsutaan tarpeen vaatiessa toisista ohjelmanosista. Python-kielessä
on kahdenlaisia aliohjelmia: funktioita ja metodeita. Metodeihin palataan opintojaksolla myöhemmin Python-kielen
oliopiirteiden yhteydessä.

## Funktion rakenne

Funktioita käyttävä ohjelma jakautuu
- pääohjelmaan eli siihen ohjelman osaan, joka sijaitsee funktioiden ulkopuolella
- funktioihin.

Pääohjelma voi kutsua funktioita.  Myös funktiot voivat kutsua toisia funktioita. Kutsuminen tarkoittaa sitä, että ohjelman
suoritus siirtyy kutsuttavaan funktioon. Kun kutsuttava funktio on kokonaan suoritettu, palaa suoritus
alkuperäiseen sijaintiin, funktion kutsua seuraavaan lauseeseen.

Kirjoitetaan ensimmäinen funktio:
```python
def tervehdi():
    print("Moi!")
    return
```

Funktio määritetään varatun sanan def avulla. Sitä seuraa funktion nimi, joka on itse keksitty tunnus. Python-kielessä
on käytäntönä nimetä funktiot kuvaavilla, pienillä kirjaimilla kirjoitetuilla nimillä. Jos nimi koostuu useasta sanasta,
lisätään erotinmerkiksi alaviiva. Tämän mallin mukaan funktiolle voitaisiin antaa nimeksi vaikkapa `tervehdi_käyttäjää`.

Nimen perässä olevien kaarisulkeiden sisällä määritetään funktion parametrit. Näihin palataan hieman myöhemmin.
Jos parametreja ei anneta, kirjoitetaan kuitenkin tyhjät kaarisulkeet kuten yllä olevassa esimerkissä.

Kaarisulkeiden jälkeen lisätään kaksoispiste. Kaksoispisteen jälkeen kirjoitetaan funktion runkoon kuuluvat lauseet,
jotka suoritetaan silloin, kun funktiota kutsutaan.

Funktion runkoon kuuluvat lauseet on kirjoitettava yhden askeleen verran sisennettyinä. Python-kielessä yhden askeleen
sisennys saadaan ilmaistaan tuottamalla rivin alkuun neljä välilyöntiä. Käytännössä neljää välilyöntiä ei kannata
tehdä välilyöntinäppäintä napsuttelemalla vaan painamalla yhden kerran sarkainnäppäintä eli Tab-näppäintä.
Koodin sisentäminen on tärkeä työväline Python-kielessä: sillä ilmaistaan ohjelman sisäinen hierarkia. Tässä tapauksessa
yhden askeleen sisennys ilmaisee, mitkä lauseet kuuluvat funktion runkoon. Python-kielessä koodin oikea sisentäminen
on pakollista, ja sivutuotteena se tekee koodista myös havainnollisemman ja helpommin luettavan. Tässä Python poikkeaa
monista tunnetuista ohjelmointikielistä, joissa koodin sisentäminen on kielen syntaksin näkökulmasta vapaaehtoista.

Funktio päättyy return-lauseeseen.
Return-lauseella voidaan palauttaa paluuarvo, jos sellainen on. Tässä sellaista ei ole, joten palataan
paluuarvoon myöhemmin.

Samaan ohjelmaan voidaan kirjoittaa useita funktioita. Yllä olevassa esimerkissä funktioita on vain yksi.


## Funktion kutsuminen

Kun funktio on kirjoitettu, ohjelma ei vielä tee mitään. Jotta funktion rungossa oleva ohjelmakoodi suoritettaisiin,
on funktiota kutsuttava.

Laajennetaan ohjelmaa siten, että mukana on funktion lisäksi pääohjelma, jossa funktiota kutsutaan:

```python
def tervehdi():
    print("Moi!")
    return

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")

```

Yllä oleva ohjelma koostuu funktiosta nyt tervehdi-funktiosta ja sitä seuraavasta pääohjelmasta.
Pääohjelma koostuu tässä tapauksessa kolmesta lauseesta: tulostuslauseesta, funktion kutsusta ja toisesta
tulostuslauseesta.

Funktion määrityksen on oltava ohjelmakoodissa ennen kohtaa, jossa sitä kutsutaan (eli ylempänä).
Tästä seuraa, että pääohjelma on kirjoitettava ohjelmakoodissa viimeiseksi.


Ohjelman suoritus alkaa aina pääohjelman alusta.

Kun tervehdi-funktiota kutsutaan, suoritus siirtyy funktion runkoon, ja pääohjelma jää odottamaan, että funktion suoritus päättyy.
Funktion suorituksen päätyttyä return-lauseeseen kutsuva ohjelmanosa jatkaa siitä mihin se jäi.

Ohjelma tuottaa seuraavan tulosteen:

```monospace
Päivä alkaa tervehdyksellä.
Moi!
Sitten siirrytään muihin asioihin.
```

## Funktion parametrit

Edellisen esimerkin tervehdi-funktio toimii aina samalla tavalla.
Se ei kaipaa pääohjelmalta mitään lähtötietoja.
Joskus funktiolle on välitettävä tietoja, jotta se osaa suorittaa itsensä oikein.
Näitä funktiolle välitettäviä tietoja kutsutaan parametreiksi.
Parametrien arvot ilmoitetaan funktion kutsussa.
Nämä arvot kopioidaan funktion määrittelyn yhteydessä oleviin parametrimuuttujiin.

Tarkastellaan esimerkkiohjelmaa:

```python
def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print ("Tervehditään lisää.")
tervehdi(2)
```

Ohjelma tuottaa seuraavan tulosteen:
```monospace
Päivä alkaa tervehdyksillä.
Hyvää päivää 1. kerran
Hyvää päivää 2. kerran
Hyvää päivää 3. kerran
Hyvää päivää 4. kerran
Hyvää päivää 5. kerran
Tervehditään lisää.
Hyvää päivää 1. kerran
Hyvää päivää 2. kerran
```


Edellä funktion kerrat-parametrimuuttujalle välitetään arvo pääohjelmalta.
Kutsuja on kaksi: ensimmäisessä kutsussa välitetään arvo 5, ja toisessa kutsussa välitetään arvo 2.

Välitettävä arvo on tässä "kovakoodattu" ohjelmakoodiin, mutta se voisi olla tallennettuna muuttujaan ja
määräytyä vasta suoritusaikana. Se voitaisiin esimerkiksi kysyä käyttäjältä.

Funktiolle välitettäviä parametrien arvoja kutsutaan argumenteiksi. Tässä kumpaankin funktion kutsuun liittyy yksi argumentti.


## Muuttujien näkyvyys

Aiemmassa esimerkissä funktion sisällä määriteltiin `i`-kierrosmuuttuja, jonka avulla tervehdys tulostettiin.
Tällaisia funktion sisällä olevia muuttujia kutsutaan paikallisiksi muuttujiksi. Ne eivät näy funktion ulkopuolelle.

Funktioiden ulkopuolella määriteltyjä muuttujia kutsutaan globaaleiksi muuttujiksi.
Niiden arvot näkyvät kaikkialle, myös funktioiden sisälle.

Tällöin funktion sisällä voitaisiin periaatteessa muuttaa globaalin muuttujan arvoa.
Tätä kutsutaan funktion sivuvaikutukseksi. Niitä pidetään ei-toivottavina.

Parametrien käyttö estää funktion sivuvaikutukset.
Kun alkeistyypin (kokonaisluku, liukuluku, merkkijono) arvo annetaan argumenttina, kopioidaan sen arvo parametrimuuttujaan funktiota kutsuttaessa.
Tällöin parametrimuuttujaan funktion sisällä tehdyt muutokset eivät vaikuta funktion ulkopuolelle.

Tarkastellaan asian havainnollistamiseksi esimerkkiohjelmaa:

```python
def vaihda(kaupunki):
    print("Funktiossa aluksi: " + kaupunki)
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda(kaupunki)
print("Pääohjelmassa lopuksi: " + kaupunki)
```

Ohjelma tulostaa seuraaavan tulosteen:

```monospace
Pääohjelmassa aluksi: Helsinki
Funktiossa aluksi: Helsinki
Funktiossa lopuksi: Vantaa
Pääohjelmassa lopuksi: Helsinki
```

Mitä tapahtui? Edellä luodaan kaksi eri ilmentymää muuttujasta kaupunki:
1. Globaali muuttuja, joka luodaan pääohjelmassa
2. Funktion sisäinen parametrimuuttuja, joka luodaan kun funktiota kutsutaan
Kun funktiota vaihda() kutsutaan, argumenttina annettu globaalin muuttujan arvo kopioidaan saman nimisen parametrimuuttujan arvoksi (pass-by-value).
Funktion rungossa vaihdetaan tuon funktion sisäisen parametrimuuttujan arvo. Globaalin muuttujan arvo ei kuitenkaan muutu.

Muuttujien näkyvyyssäännöt on tärkeää ymmärtää, jotta osaat ohjelmoijana käyttää globaaleja ja paikallisia
muuttujia tarkoituksenmukaisesti sekä osaat välittää parametreja funktioille oikein.

## Useita parametreja



## Lista parametrina

## Muita funktioiden piirteitä

