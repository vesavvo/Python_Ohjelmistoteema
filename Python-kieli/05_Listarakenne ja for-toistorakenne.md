# Listarakenne ja for-toistorakenne

Tässä moduulissa opit käyttämään listoja, jotka ovat Python-kielen tärkein tietorakenne. Lista tarkoittaa järjestettyä
joukkoa alkioita. Listarakenteen avulla voit tallentaa useita arvoja yhteen listamuuttujaan, ja voit käydä
nuo arvot läpi tarkoitukseen kehitettyä for-toistorakennetta käyttäen.

## Lista ja alkiot

Ohjelmoinnissa tietorakenteella tarkoitetaan ratkaisua, jossa yhteen muuttujaan on tallennettuna yhden arvon
sijasta kokonainen joukko arvoja. Tietorakenteita on erilaisia: lista, sanakirja, puu, pino ja verkko. Jokaisella tietorakenteella
on oma käyttöalueensa.

Lista on tietorakenne, jossa alkiot ovat ikään kuin jonossa, määrätyssä järjestyksessä. Listaan voidaan liittää
alkioita haluttuun kohtaan, ja listasta voidaan poistaa alkioita. Listan alkiot voidaan myös käydä läpi luetellen
ne. Listarakenteessa uusi alkio lisätään usein listan loppuun, ja alkio poistetaan listan alusta. Muutkin ratkaisut
ovat mahdollisia.

Tarkastellaan ohjelmaa, joka luo listan ja asettaa sen arvoksi viiden henkilön nimet, eli viisi merkkijonoa:

```python
nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
```
Listamuuttujan luovassa sijoituslauseessa listamuuttujan nimi on yhtäsuuruusmerkin vasemmalla puolella.
Oikealle puolelle kirjoitetaan hakasulkeet. Listaan
liitettävät jäsenet luetellaan hakasulkeiden sisällä pilkulla erotettuina.

Tässä tapauksessa tuloksena on viisialkioinen lista, jonka alkiot ovat merkkijonoja. Listaan viitataan
listamuuttujalla, joka on nimeltään `nimet`. Seuraava kuva havainnollistaa listan rakennetta:

![Listamuuttuja ja listan alkiot](img/lista.png)

Tarkastellaan sitten tapoja viitata listan alkioihin. Seuraavassa ohjelmassa tulostaa luodun listan alkioita ja osia:

```python
nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)
```

Tuloste on seuraava:

```monospace
Olga
Ahmed
Olga
['Ahmed', 'Pekka']
['Pekka', 'Olga', 'Mary']
['Viivi', 'Ahmed', 'Pekka', 'Olga', 'Mary']
```

Ensimmäinen tulostuslause tulostaa listan alkion, jonka indeksi on kolme. Python-listan alkioihin voidaan aina viitata
indeksin avulla. Indeksi on listan alkion järjestysnumero. Numerointi alkaa aina nollasta, joten indeksillä 3 viitataan listan
neljänteen alkioon, joka on merkkijono "Olga".

Toisessa tulostuslauseessa tulostetaan indeksiä 1 vastaava alkio. Se on listan toinen merkkijono, eli "Ahmed".

Kolmannessa tulostuslauseessa on annettu negatiivinen indeksi. Tällöin listan alkioiden laskenta aloitetaan listan lopusta
lukien: merkintä -1 vastaa listan viimeistä alkiota, -2 toiseksi viimeistä ja niin edelleen. Tässä tapauksessa tulostuu
toiseksi viimeinen alkio eli merkkijono "Olga".

Neljäs tulostuslause tulostaa listan osan. Hakasulkeissa annettu indeksiväli `1:3` tarkoittaa, että tuloksena
olevaan uuteen listaan otetaan alkiot indeksistä 1 alkaen (alkupiste mukaan lukien) ja indeksiin 3 päättyen (päätepiste pois lukien).
Välin alkupiste otetaan siis aina mukaan tuloksena olevaan uuteen listaan, mutta loppupiste ei. Näin uuteen listaan
päätyvät alkiot 1 ja 2 eli "Ahmed" ja "Pekka".

Viidennessä tulostuslauseessa indeksivälin loppupiste on jätetty antamatta. Tällöin tulostetaan alkiot alkupisteestä
alkaen (ja se mukaan lukien) aina listan loppuun asti. Tuloksena on indeksejä 2, 3 ja 4 vastaavien alkioiden
"Pekka", "Olga" ja "Mary" muodostama lista.

Viimeinen esimerkki tulostaa listan kokonaisuudessaan.

Listan pituus saadaan tarvittaessa Python-kielen sisäänrakennetulla `len`-funktiolla:

```python
print (len(nimet))
```

Tuloksena on listan pituus, joka on siis yhtä suurempi kuin viimeisen alkion indeksi:
```monospace
5
```

## Viittaus listan ulkopuolelle

Kun listan alkioon viitataan indeksin avulla, on mahdollista ohjelmoida kielletty viittaus, joka osoittaa
sellaiseen alkioon, jota ei listassa ole. Tällainen virhe on ohjelmoitaessa varsin yleinen, ja se on hyvä
opetella heti tässä vaiheessa tunnistamaan.

Seuraavassa listassa on viisi alkiota. Tarkoitus on viitata listan viidenteen alkioon, mutta - koska indeksointi
alkaa nollasta - ohjelmaan kirjoitettu indeksi 5 viittaa kuudenteen alkioon. Tuloksena on virhetilanne:

```python
nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
# Virheellinen viittaus
print (nimet[5])
```

Syntyy ajonaikainen poikkeus, ja konsolissa nähdään selostus virheestä:
```monospace
Traceback (most recent call last):
  File "C:/Users/olliv/PycharmProjects/Python_Ohjelmistoteema/Esimerkit/listaesimerkki.py", line 4, in <module>
    print (nimet[5])
IndexError: list index out of range

Process finished with exit code 1
```

Virheilmoitus on tälläkin kertaa ohjelmoijan ystävä: se näyttää virheellisen lauseen sekä virheen syyn: listan indeksi oli
sallitun arvoalueen ulkopuolella.

## Listaoperaatiot

Edeltävissä esimerkeissä listan alkiot lueteltiin listaa luotaessa, ja lista pysyi sen jälkeen muuttumattomana
koko ohjelman suorituksen ajan. Listaa käytetään usein kuitenkin dynaamisesti: siihen lisätään ja siitä poistetaan
alkioita ohjelman suorituksen aikana.

Seuraava ohjelma luo aluksi tyhjän listan. Sen jälkeen ohjelma pyytää käyttäjältä nimiä siihen asti, että
käyttäjä syöttää tyhjän merkkijonon pelkästään painamalla Enter-näppäintä. Lopuksi ohjelma tulostaa listan kokonaisuudessaan:

```python
nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
```

Alla on esimerkki ohjelman toiminnasta:
```monospace
Anna ensimmäinen nimi tai lopeta painamalla Enter: Mikko
Anna seuraava nimi tai lopeta painamalla Enter: Kerttu
Anna seuraava nimi tai lopeta painamalla Enter: John
Anna seuraava nimi tai lopeta painamalla Enter: Miriam
Anna seuraava nimi tai lopeta painamalla Enter:
['Mikko', 'Kerttu', 'John', Miriam']
```

Esimerkissä listan loppuun saatiin lisättyä uusia alkioita yksi kerrallaan `append`-listaoperaatiolla.
Python-kielessä on joukko valmiita listaoperaatioita, joiden avulla listaan voidaan lisätä ja poistaa alkioita.
Operaatioiden avulla voidaan myös järjestellä listan alkioita erilaisin tavoin.

Tavallisimmat listaoperaatiot on koottu alla olevaan taulukkoon:

| Operaatio | Tarkoitus                                                                                   | Esimerkki                                                       | 
|--------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| append | lisää alkion listan loppuun                                                                 | nimet.append("Matti")                                           |
| remove | poistaa alkion ensimmäisen ilmentymän listasta                                              | nimet.remove("Pekka")                                           |
| insert | lisää alkion haluttuun kohtaan, ennen alkiota, jonka indeksi vastaa ensimmäistä argumenttia | nimet.insert(4, "Teppo")                                        |
| extend | liittää toisen listan ensimmäiseen listaan                                                  | toisetNimet = ["Allu","Ninni"]<br/>nimet.insert(toisetNimet)    |
| index  | palauttaa alkion ensimmäisen sijainnin indeksin                                             | monesko = nimet.index("Olga")                                   |
| in     | testaa, esiintyykö alkio listassa                                                           | if "Matti" in nimet:<br/>&nbsp;&nbsp;&nbsp;&nbsp;"Matti löytyi" |

## Listan läpikäynti for-toistorakenteen avulla

Edellä kirjoittamamme ohjelma kysyi käyttäjiltä nimiä ja tulosti sen jälkeen listamuuttujan kerralla ja kokonaisuudessaan.

Tarkastellaan seuraavaksi, miten voimme käydä listan läpi alkio alkiolta. Laajennetaan ohjelmaa siten,
että ohjelma tervehtiin jokaista listaan lisättyä henkilöä erikseen. Ohjelma kirjoitetaan seuraavasti:

```python
nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for n in nimet:
    print (f"Moi, {n}!")
```

Ohjelma toimii näin:
```monospace
Anna ensimmäinen nimi tai lopeta painamalla Enter: Stefan
Anna seuraava nimi tai lopeta painamalla Enter: Ville
Anna seuraava nimi tai lopeta painamalla Enter: Aamu
Anna seuraava nimi tai lopeta painamalla Enter:
Moi, Stefan!
Moi, Ville!
Moi, Aamu!
```

Listan läpikäynti toteutettiin for-toistorakenteen avulla:
```python
for n in nimet:
    print (f"Moi, {n}!")
```

Toistorakenne on omiaan listan läpikäyntiin. Kierrosmuuttuja `n` saa vuoron perään arvokseen kunkin listan alkion. Toistoa
jatketaan niin kauan kuin listassa riittää alkioita.

Tällaista listan läpikäyntiä alkio kerrallaan kutsutaan listan iteroimiseksi.

## Range-funktio

`For`-toistorakenteella on myös muita käyttömahdollisuuksia kuin edellä esitetty listan läpikäynti.
Rakenteen avulla voidaan helposti luoda kierrosmuuttuja, joka saa vuoron perään halutut arvot, joko yhden välein tai muutoin
askeltaen.

- range(1,4) määrittää arvot 1, 2, 3
- range(5,0,-1) määrittää arvot 5, 4, 3, 2, 1
- range(10,21,2) määrittää arvot 10, 12, 14, 16, 18, 20

`Range`-funktion ensimmäinen argumentti on välin alkupiste, toinen argumentti on välin loppupiste ja kolmas, valinnainen argumentti on 
askeleen suuruus. Jos askeleen suuruus jätetään määrittämättä, on askel yksi. Jos askeleeksi annetaan nolla, saadaan virheilmoitus.

Jos `range`-funktiolle annetaan vain yksi argumentti, tulkitaan se välin loppupisteeksi. Alkupiste on tällöin nolla
ja askel yksi.

Range-funktio tuottaa Pythonin range- eli arvoväli-tietorakenteen, joka määrittää halutut arvot. Arvoväli voidaan
käydä läpi samaan tapaan kuin listarakenne.

Esimerkiksi seuraava ohjelma tulostaa kolmella jaolliset luvut väliltä 3 ja 30. Huomaa, että `range`-funktion
kutsussa oleva alkupiste kuuluu mukaan arvoväliin, mutta loppupiste ei. Tästä syystä loppupisteeksi on asetettava jokin luku, joka 
on hieman suurempi kuin 30.

```python
for luku in range(3,31,3):
    print (luku)
```

Ohjelma tulostaa:

```monospace
3
6
9
12
15
18
21
24
27
30
```

`Range`-funktion avulla on näppärää korvata kierrosmuuttujaan perustuva toistorakenne.
Seuraava ohjelma tulostaa kuusi kertaa merkkijonon "Moi!".

```python
for luku in range(6):
    print ("Moi!")
```