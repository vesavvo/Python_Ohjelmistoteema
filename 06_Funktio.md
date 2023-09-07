# Funktio

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

Funktio määritetään varatun sanan `def` avulla. Sitä seuraa funktion nimi, joka on itse keksitty tunnus. Python-kielessä
on käytäntönä nimetä funktiot kuvaavilla, pienillä kirjaimilla kirjoitetuilla nimillä. Jos nimi koostuu useasta sanasta,
lisätään erotinmerkiksi alaviiva. Tämän mallin mukaan funktiolle voitaisiin antaa nimeksi vaikkapa `tervehdi_käyttäjää`.

Nimen perässä olevien kaarisulkeiden sisällä määritetään funktion parametrit. Näihin palataan hieman myöhemmin.
Jos parametreja ei anneta, kirjoitetaan kuitenkin tyhjät kaarisulkeet kuten yllä olevassa esimerkissä.

Kaarisulkeiden jälkeen lisätään kaksoispiste. Kaksoispisteen jälkeen kirjoitetaan funktion runkoon kuuluvat lauseet,
jotka suoritetaan silloin, kun funktiota kutsutaan.

Funktion runkoon kuuluvat lauseet on kirjoitettava yhden askeleen verran sisennettyinä.

Funktio päättyy `return`-lauseeseen.
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

Yllä oleva ohjelma koostuu funktiosta nyt `tervehdi`-funktiosta ja sitä seuraavasta pääohjelmasta.
Pääohjelma koostuu tässä tapauksessa kolmesta lauseesta: tulostuslauseesta, funktion kutsusta ja toisesta
tulostuslauseesta.

Funktion määrityksen on oltava ohjelmakoodissa ennen kohtaa, jossa sitä kutsutaan (eli ylempänä).
Tästä seuraa, että pääohjelma on kirjoitettava ohjelmakoodissa viimeiseksi.


Ohjelman suoritus alkaa aina pääohjelman alusta.

Kun `tervehdi`-funktiota kutsutaan, suoritus siirtyy funktion runkoon, ja pääohjelma jää odottamaan, että funktion suoritus päättyy.
Funktion suorituksen päätyttyä return-lauseeseen kutsuva ohjelmanosa jatkaa siitä mihin se jäi.

Ohjelma tuottaa seuraavan tulosteen:

```monospace
Päivä alkaa tervehdyksellä.
Moi!
Sitten siirrytään muihin asioihin.
```

## Funktion parametrit

Edellisen esimerkin `tervehdi`-funktio toimii aina samalla tavalla.
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


Edellä funktion `kerrat`-parametrimuuttujalle välitetään arvo pääohjelmalta.
Kutsuja on kaksi: ensimmäisessä kutsussa välitetään arvo 5, ja toisessa kutsussa välitetään arvo 2.

Välitettävä arvo on tässä "kovakoodattu" ohjelmakoodiin, mutta se voisi olla tallennettuna muuttujaan ja
määräytyä vasta suoritusaikana. Se voitaisiin esimerkiksi kysyä käyttäjältä.

Funktiolle välitettäviä parametrien arvoja kutsutaan argumenteiksi. Tässä kumpaankin funktion kutsuun liittyy yksi argumentti.


## Muuttujien näkyvyys

Aiemmassa esimerkissä funktion sisällä määriteltiin `i`-kierrosmuuttuja, jonka avulla tervehdys tulostettiin.
Tällaisia funktion sisällä olevia muuttujia kutsutaan paikallisiksi muuttujiksi. Ne eivät näy funktion ulkopuolelle.

Funktioiden ulkopuolella määriteltyjä muuttujia kutsutaan globaaleiksi muuttujiksi.
Niiden arvot näkyvät kaikkialle, myös funktioiden sisälle.

Jos muuttujan arvoa muutetaan funktion sisällä, muuttuja tulkitaan automaattisesti paikalliseksi muuttujaksi.

Tarkastellaan asian havainnollistamiseksi esimerkkiohjelmaa:

```python
def vaihda():
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)
```

Ohjelma tulostaa seuraaavan tulosteen:

```monospace
Pääohjelmassa aluksi: Helsinki
Funktiossa lopuksi: Vantaa
Pääohjelmassa lopuksi: Helsinki
```

Mitä tapahtui? Edellä luodaan kaksi eri ilmentymää muuttujasta kaupunki:
1. Globaali muuttuja, joka luodaan pääohjelmassa
2. Funktion sisäinen muuttuja, joka on saman niminen kuin globaali muuttuja. Sen arvon muuttaminen ei muuta globaalin muuttujan arvoa.

Muuttujien näkyvyyssäännöt on tärkeää ymmärtää, jotta osaat ohjelmoijana käyttää globaaleja ja paikallisia
muuttujia tarkoituksenmukaisesti sekä osaat välittää parametreja funktioille oikein.

## Useita parametreja

Funktiolle voidaan välittää useita argumentteja. Tällöin argumentit erotetaan toisistaan pilkulla.
Funktion kutsussa olevat argumenttien arvot sijoitetaan parametrimuuttujiin siinä järjestyksessä kuin ne esiintyvät.

Tarkastellaan esimerkkiohjelmaa:

```python
def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print (tervehdys + " " + str(i+1) + ". kerran")
    return

tervehdi("Moi", 3)
tervehdi("Hyvää päivää", 2)
```

Ohjelma tuottaa seuraavan tulosteen:

```monospace
Moi 1. kerran
Moi 2. kerran
Moi 3. kerran
Hyvää päivää 1. kerran
Hyvää päivää 2. kerran
```

Huomaamme, että tervehtimisfunktio on muuttunut aiempaa yleiskäyttöisemmäksi: sitä voidaan käyttää monenmoiseen
tervehtimiseen. Tällä tavoin funktiota parametrisoimalla (eli korvaamalla kiinteitä oletuksia parametreina
annettavilla lähtötiedoilla) funktioista saadaan vahvoja, monikäyttöisiä työkaluja suurtenkin ohjelmien tarpeisiin.

## Paluuarvo

Joskus funktio tuottaa arvon, joka on palautettava kutsuvalle ohjelmanosalle. Tämä arvon palauttaminen onnistuu
paluuarvomekanismin avulla.

Funktion tuottama arvo palautetaan `return`-lauseella. Tähänastisissa esimerkeissä `return`-lause ei ole sisältänyt
paluuarvoa. Tarkastellaan nyt paluuarvon lisäämistä.

Seuraava ohjelma laskee kahden luvun neliösumman, joka saadaan kertomalla kumpikin luvuista itsellään ja
palauttamalla näin saatujen tulojen summa. Nyt on tärkeää, että tuo neliösumma - eli funktion laskema tulos - 
saadaan välitettyä pääohjelmalle.

```python
def neliösumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = neliösumma(luku1, luku2)
print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")
```

Tuloste on seuraavanlainen:

```monospace
Anna ensimmäinen luku: 2
Anna toinen luku: 3.2
Lukujen 2.000 ja 3.200 neliösumma on 14.240.
```

Paluuarvo on luonnollisesti otettava talteen, jotta sitä voidaan käyttää.
Funktion kutsussa arvo sijoitetaan yleensä välittömästi muuttujaan tai hyödynnetään muulla tavoin.

## Lista parametrina

Funktiolle voidaan antaa parametrina lista. Seuraavassa esimerkissä inventaario-funktio saa parametrinaan listan
ja luettelee listan alkiot:

```python
def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print ("- " + t)
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)
```


Funktiota kutsutaan kahteen kertaan. Kummallakin kerralla tulostetaan repussa olevat tavarat:
```monospace
Sinulla on seuraavat tavarat:
- Vesipullo
- Kartta
- Kompassi
Sinulla on seuraavat tavarat:
- Vesipullo
- Kartta
- Kompassi
- Linkkuveitsi
```

Muutetaan nyt ohjelmaa hieman. Muokataan aliohjelmaa siten, että se tyhjentää listan sen tulostettuaan:

```python
def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print ("- " + t)
    # Tavarat katoavat inventaariossa!
    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)
```

Tulosteesta nähdään, että inventaario-funktion kutsu tyhjentää repun:
```monospace
Sinulla on seuraavat tavarat:
- Vesipullo
- Kartta
- Kompassi
Sinulla on seuraavat tavarat:
- Linkkuveitsi
```

Mitä tapahtui? Kun parametrina annetaan lista, sen välitys toimii toisin kuin alkeistyyppisten muuttujien.

Alkeistyypin arvo kopioidaan kutsussa olevasta argumentista parametrimuuttujan arvoksi. Listan tapauksessa
listan sisältöä ei kopioida, vaan listasta välitetään funktiolle vain muistiosoite, eli tieto siitä,
mistä lista keskusmuistista löytyy.

Tällöin globaalin reppu-muuttujan muistiosoite kopioituu tavarat-muuttujan arvoksi.
Nyt sekä reppu- että tavarat-muuttujat viittaavat samaan tietokoneen keskusmuistissa olevaan listaan.
Funktio muuttaa tavarat-muuttujan kautta saatavan listan sisältöä clear-listametodilla, joka tyhjentää listan.
Koska kyseessä on yksi ja sama lista, muutos näkyy myös globaalin reppu-muuttujan arvon muutoksena.
Parametrina saatuun listaan tehdyt muutokset heijastuvat siis myös kutsussa annettuun listaan.

## Muita funktioiden piirteitä

Pythonin funktioilla on lisäksi seuraavat ominaisuudet:
1. Vaihtuvan mittaiset argumenttijonot.
Argumentteja voidaan antaa kutsukerrastasta toiseen vaihteleva määrä. Funktio voi käsitellä saadut arvot listana.
2. Parametrien välittäminen avainsanojen avulla.
Ohjelmoija voi antaa parametrien arvot (nimi = arvo)-pareina. Parametreille voi antaa funktion määrityksessä myös oletusarvot.

Lisäksi Python-tukee anonyymejä funktioita eli lambda-funktioita. Tällöin määritetään vain kaava tai sääntö, jolla paluuarvo tuotetaan ilman,
että kirjoitetaan varsinaista funktiota. Lambda-funktioita käsitellään myöhemmin.

