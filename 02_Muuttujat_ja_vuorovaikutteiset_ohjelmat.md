# Muuttujat ja vuorovaikutteiset ohjelmat

Tässä moduulissa opit kirjoittamaan vuorovaikutteisia Python-ohjelmia.

Vuorovaikutteinen ohjelma kommunikoi käyttäjänsä kanssa: se lukee syötteitä, käsittelee niitä ja tuottaa sen pohjalta
tulosteita.

Esimerkki vuorovaikutteisesta ohjelmasta on ohjelma, joka kysyy käyttäjältä kaksi lukua, laskee niiden summan
ja näyttää sen käyttäjälle. Tässä tapauksessa käyttäjältä luetaan syöte (esimerkiksi luvut 2 ja 3), syötettä käsitellään
laskemalla summa, ja käyttäjälle näytetään tuloste (lukujen summa 5).

## Tulostaminen

Aloitetaan Python-kielen tulostusfunktiosta, joka on print. Seuraava ohjelma tulostaa tekstin "Hei, maailma":
```python
print('Hei, maailma!')
```
Tulostus hoidetaan print-nimisellä funktiolla, joka on Python-kielen sisäänrakennettu funktio. Funktion argumentti kirjoitetaan
kaarisulkeiden sisään. Tässä tapauksessa tulostettavana on merkkijonoliteraali "Hei, maailma".
Merkkijonoliteraaliksi kutsutaan sellaista merkkijonoa, joka kirjoitetaan suoraan ohjelmakoodiin. Merkkijonoliteraali
kirjoitetaan joko heitto- tai lainausmerkkien sisään. Niinpä ohjelma voitaisiin kirjoittaa myös seuraavasti:
```python
print("Hei, maailma!")
```
Entäpä tilanne, jossa heitto- tai lainausmerkki halutaan ottaa mukaan osaksi tulostettavaa merkkijonoa? Ratkaisuna on
kirjoittaa tulostettava merkki merkkijonoliteraalin sisään siten, että merkkijonoliteraalin alku- ja loppumerkkinä
käytetään toista merkkiä kuin sitä, joka on merkkijonoliteraalin sisällä:
```python
print('"Hei", sanoi Ville')
```

Kun ohjelmassa on useita tulostuslauseita, tulostuu jokaisen perään automaattisesti rivinvaihto:
```python
print("Hyvää")
print("huomenta")
```

Tuloste on:
```monospace
Hyvää
huomenta
```

Edellä olevasta ohjelmasta ilmenee yksi ohjelmointikielen perusrakenteista: peräkkäisyys. Lauseet suoritetaan lähtökohtaisesti
siinä järjestyksessä kuin ne on ohjelmakoodiin kirjoitettu. Muut perusrakenteet ovat valinnaisuus ja toisto;
niitä käsitellään myöhemmin.

Rivinvaihdon sisältävä tulostuslause voidaan kuitenkin toteuttaa myös yhdellä lauseella:
merkkijonoliteraalin sisälle on mahdollista kirjoittaa rivinvaihtomerkki \n.
Sama tuloste kuin edellä saadaan kirjoittamalla:
```python
print("Hyvää\nhuomenta")
```

## Syötteen luku, muuttuja ja sijoituslause

Edellä kuvatulla tavalla voidaa tehdä yksinkertaisia ohjelmia, jotka tulostavat jokaisella suorituskerralla
saman merkkijonon. Yleensä halutaan, että ohjelma saa syötteitä käyttäjältä ja käyttää niitä hyödykseen.

Kirjoitetaan nyt ohjelma, joka kysyy käyttäjältä tämän nimen ja tervehtiin sen jälkeen käyttäjää nimeltä.
Tämä onnistuu seuraavasti:

```python
käyttäjä = input('Anna nimesi: ')
print("Hauska tavata, " + käyttäjä + "!")
```

Käyttäjän syöte luetaan sisäänrakennetulla input-funktiolla. Funktio saa argumenttinaan tekstin, joka tulostetaan ruudulle.
Tekstin on syytä olla sellainen, että käyttäjä tietää, mitä hänen oletetaan syöttävän.

Sisäänrakennettu input-funktio odottaa käyttäjän syötettä näppäimistöltä. Käyttäjä päättää syötteen Enter-näppäimellä.
Kun syöte on annettu, input-funktion arvona on syötettä vastaava merkkijono.

Merkkijono on laitettava talteen, jotta sitä voidaan käyttää myöhemmin ohjelmassa. Tätä varten se tallennetaan muuttujaan (*variable*).
Tässä tapauksessa muuttuja on nimeltään käyttäjä. Käyttäjän antama syöte tallentuu tietokoneen muistiin, ja se saadaan haettua sieltä
muuttujan nimen avulla. Muuttujan nimi on siis ikäänkuin kahva tai nimilappu, jonka avulla arvo voidaan muistista hakea.

Muuttujalle annetaan arvo sijoituslauseessa. Sijoituslauseen tunnistaa yhtäsuuruusmerkistä (=). Sen vasemmalla
puolella on sen muuttujan nimi, jolle arvo annetaan. Oikealle puolelle kirjoitetaan lauseke, jonka
arvo tulee muuttujan arvoksi.

Katsotaan nyt tulostuslausetta tarkemmin.

Jos haluaisimme vain tulostaa käyttäjän syöttämän nimen, voisimme korvata alemman rivin seuraavalla:
```python
print(käyttäjä)
```
Huomaa, että nyt `käyttäjä` on muuttujan nimi. Se ei ole merkkijonoliteraali, eikä sitä kirjoiteta lainausmerkkeihin.

Haluamme kuitenkin, että ohjelma tulostaa pelkän nimen sijasta kokonaisen tervehdystekstin.
Tulostettava merkkijono voidaan koostaa osamerkkijonoista siten, että osat liitetään toisiinsa plusmerkin (+) avulla.
Alkuperäisen ohjelman alempi rivi koostaa tulosteen kolmesta osasta:
1. merkkijonoliteraalista "Hauska tavata, ",
2. muuttujan `käyttäjä` arvosta, sekä
3. merkkijonoliteraalista "!".

Ohjelma toimii siis seuraavasti:
```monospace
Anna nimesi: Viivi
Hauska tavata, Viivi!
```

## Muuttujan tyyppi

Edellä muuttujalle annettiin arvoksi käyttäjän antama merkkijono.

Python-kielessä muuttujia ei tarvitse etukäteen esitellä, eikä niiden tyyppiä tarvitse määrittää, vaan
muuttujan tyyppi määrittyy automaattisesti sijoituslauseen seurauksena. Tyyppi tarkoittaa sitä, minkälaiseen tietoon
muuttuja viittaa: onko muuttujan arvona esimerkiksi merkkijono vai luku?

Python-kielessä on kuusi muuttujan perustyyppiä:
- merkkijono (*string*)
- luku (*number*), joka voi olla kokonaisluku, pitkä kokonaisluku, liukuluku tai kompleksiluku
- totuusarvo (*boolean*), joka voi olla True tai False
- lista (*list*)
- monikko (*tuple*)
- sanakirja (*dictionary*)

Lisäksi muuttuja voi olla tyypiltään viittaus olioon. Merkkijonotyyppistä muuttujaa käsittelimme edellä. 
Listoihin, monikkoon, sanakirjaan ja olioviittaukseen palataan myöhemmin kurssilla. Tarkastellaan seuraavaksi
luku-tietotyyppiä.

Pythonin luku-tietotyypillä on neljä alatyyppiä: kokonaisluku (esimerkiksi 4), pitkä kokonaisluku (esimerkiksi 12756413000),
liukuluku (esimerkiksi 7.28 tai 4.0) ja
kompleksiluku (esimerkiksi 3-2i). Seuraavaksi luomme neljä muuttujaa, joista ensimmäiseen sijoitetaan kokonaisluku,
toiseen pitkä kokonaisluku, kolmanteen
liukuluku ja neljänteen kompleksiluku. Sen jälkeen tulostamme kaikkien neljän muuttujan arvot sekä kompleksiluvusta
erikseen reaali- ja imaginaariosan arvot:

```python
eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)
```

Kokonaislukua ja pitkää kokonaislukua syötettäessä voidaan numeromerkit ryhmitellä alaviivasymbolin avulla,
kuten muuttujalle toka edellä tehtiin. Tämä ei kuitenkaan ole pakollista.

Kokonaisluku ja pitkä kokonaisluku eroavat toisistaan siten, että pitkän kokonaisluvun arvoalue on laajempi. Siihen
voidaan tallentaa kokonaislukuja, jotka ovat todella suuria tai todella pieniä. Tavallinen kokonaisluku
voi sisältää arvon lukujen -2147483648 ja 2147483647 väliltä päätepisteet mukaan lukien. Pitkälle kokonaisluvulle
varataan muistista enemmän tilaa kuin tavalliselle kokonaisluvulle.

Huomaa, että kompleksiluvussa imaginaariosan symbolina käytetään Pythonissa j-kirjainta eikä i-kirjainta niin kuin
matematiikassa tavanomaisesti.

Esimerkkiohjelma tuottaa seuraavan tulosteen:
```monospace
-9
12456123180
4.973
(-4+2j)
-4.0
2.0
```

## Laskutoimitukset ja tyypinmuunnosfunktiot

Muuttujilla ja vakioilla voidaan tehdä laskutoimituksia. Laskutoimitusten laskujärjestys voidaan
tarvittaessa osoittaa sulkeilla.

Laskutoimituksia ovat yhteenlasku (`+`), vähennyslasku (`+`), kertolasku (`*`) ja jakolasku (`+`). Lisäksi on olemassa jakojäännösoperaatio (`%`), pelkän kokonaisosan palauttava jakolasku (`//`) sekä potenssiinkorotus (`**`).

Alla oleva ohjelma kysyy lämpötilan Fahrenheit-asteina ja muuntaa sen Celsius-asteiksi. Muunnos tehdään
siten, että Fahrenheit-asteista vähennetään 32, ja erotus kerrotaan vakiolla 5/9.

```python
fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("Lämpötila Celsius-asteina: " + str(celsius))
```

Ohjelma toimii seuraavasti:
```monospace
Anna lämpötila Fahrenheit-asteina: 102
Lämpötila Celsius-asteina: 38.888888888888886
```

Huomaa, että edellä input-funktion palauttama arvo tulkitaan aina merkkijonoksi, vaikka käyttäjän
antama syöte koostuisi pelkistä numeromerkeistä. Merkkijono voidaan muuntaa liukuluvuksi float-funktiolla tai
kokonaisluvuksi int-funktiolla.

Vastaavasti luku voidaan muuntaa merkkijonoksi str-funktiolla. Esimerkin tulostuslauseessa muunnos on tehtävä, jotta Celsius-asteet
sisältävä liukuluku voidaan liittää merkkijonoon. Liitoksen molempien osapuolten on oltava merkkijonoja.


## Tulosteen muotoilu

Toisinaan halutaan säädellä sitä, kuinka tulostus muotoillaan: monenko desimaalin tarkkuudella liukuluvut esitetään,
tai monenko merkin suuruinen tila vaikkapa merkkijonolle varataan.

Tämä voidaan toteuttaa käyttämällä ns. muotoilumerkkijonoliteraalia, jossa tulostettava 
merkkijono sisältää muotoilukoodeja.

Tarkastellaan asiaa esimerkin kautta. Vaihdamme edellisen esimerkin tulostuslauseen sellaiseksi, että Celsius-lämpötila
näytetään aina kahden desimaalin tarkkuudellla:

```python
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")
```
Huomaa, että print-funktiokutsun argumentti alkaa nyt `f`-kirjaimella, joka kertoo, että tulostettava merkkijono
sisältää muotoiltavia lausekkeita.
Ilman f-kirjainta merkkijonoliteraali tulostettaisiin sellaisena kuin se ohjelmakoodissa näkyy, aaltosulkeineen päivineen.

Muotoiltava lauseke muotoilukoodeineen kirjoitetaan aaltosulkeiden sisään. Esimerkissä muotoiltava lauseke on muuttujan `celsius`
arvo, joka on liukuluku.

Muotoilukoodi on tässä tapauksessa `6.2f`.
Kirjain `f` kertoo, että lauseke tulostetaan liukulukuna.
Liukuluvun merkkiä `f` edeltävä merkintä `6.2` täsmentää, että tulos esitetään kuusi merkkiä leveässä kentässä,
ja liukuluvun esitystarkkuus on kaksi desimaalia.

Seuraavassa on esimerkkejä muotoilukoodeista:

- .5f : liukuluku viiden desimaalin tarkkuudella
- 10.2f : liukuluku kahden desimaalin tarkkuudella kymmenen merkkiä leveään kenttään
- <20s : merkkijono 20 merkkiä leveään kenttään vasemman reunan mukaan tasattuna
- 8d : kokonaisluku kahdeksan merkkiä leveään kenttään

Muotoilukoodien kirjoittaminen on valinnaista. Muotoilumerkkijonoliteraalien käyttö helpottaa
silti numeeristen ja merkkijonomuotoisten tulosteiden yhdistelemistä, kun `str`-funktioita ja muita
muunnosfunktioita ei tarvitse välttämättä käyttää. Edellä voisimme yksinkertaisesti tulostaa Celsius-asteet
ilman muotoilukoodia:

```python
print(f"Lämpötila Celsius-asteina: {celsius}")
```

Saman muotoiltavan merkkijonoliteraalin sisällä voi olla useita muotoiltavia lausekkeita mahdollisine koodeineen.
Seuraava ohjelma tulostaa kahden luonnonvakion, piin ja Neperin luvun, arvot siten, että kummankin vakion nimi
tulostetaan 12 merkkiä leveään kenttään, ja vastaava arvo tulostetaan viidellä desimaalilla kymmenen merkkiä leveään kenttään:

```python
import math

print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")
```

Edellä luonnonvakiot pii ja Neperin luku tulostettiin Pythonin matematiikkakirjaston avulla. Niihin viitattiin
ilmauksilla `math.pi` ja `math.e`. Matematiikkakirjastoa voidaan käyttää, kun ohjelman alkuun on lisätty kirjaston
tuontilause `import math`.

Lopuksi mainittakoon, että Python tarjoaa useita tapoja tulostuksen muotoiluun. Tässä kuvatut muotoilumerkkijonoliteraalit
ovat uudehko tapa, joka on ollut tarjolla Python-versiosta 3.6. alkaen. Yhden hyvän tavan opettelu riittää,
mutta vaihtoehtoisiin tapoihin voit törmätä netin opetusmateriaaleja ja muiden tekemiä
ohjelmakoodeja tarkasteltaessa. Nämä vaihtoehtoiset tavat ovat:
1.`str.format()`-metodin käyttö
2. muotoilumerkkijonon ja lausekeluettelon käyttö print-funktiossa (ns. prosenttinotaatio)
3. mallimerkkijonon (*template string*) käyttö

Edellä lueteltuja vaihtoehtoisia tapoja ei käsitellä tässä. Aiheesta löytyy lisätietoa Python 3 -kielen dokumentaatiosta:
[https://docs.python.org/3/tutorial/inputoutput.html]

