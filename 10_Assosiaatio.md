# Assosiaatio

Tässä moduulissa opit kirjoittamaan ohjelmia, joissa oliot ovat vuorovaikutuksessa keskenään.

Olio-ohjelmoinnissa ohjelma koostetaan luokista. Niistä luodaan ajon aikana ilmentymiä eli olioita.
Oliot voivat olla vuorovaikutuksessa keskenään: olio voi käsitellä toisia olioita ja kutsua niiden metodeja.

Tätä olioiden välistä tuntemissuhdetta kutsutaan assosiaatioksi. Assosiaatiosuhteet ohjelmoimalla saavutetaan
olio-ohjelmoinnin voima: ohjelma pilkkoutuu pieniksi, helposti ymmärrettäviksi palasiksi, ja ohjelmoija
voi kirjoittaa koodia vähän kerrallaan yhteen asiaan keskittyen. Kun olioiden väliset assosiaatiot
on hyvin suunniteltu, suurikin ohjelmakokonaisuus rakentuu näistä pienistä osista ikään kuin varkain.

## Rakenteen suunnittelu

Aiemmassa moduulissa kirjoitimme `Koira`-luokan, jossa määritetään koiran ominaisuudet (nimi, syntymävuosi ja yksilöllinen
haukahdus). Lisäksi luokkaan on kirjoitettu yksi metodi: `hauku`. `Koira`-luokka on seuraavanlainen:

```python
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return
```

Laajennetaan esimerkkiä siten, että perustamme koirahoitolan. Määritellään koirahoitola seuraavasti:
koira voidaan viedä hoitoon koirahoitolaan ja hakea
sieltä pois. Välillä hoitolan työntekijä tekee hoitolassa kierroksen; silloin hän tervehtii kaikkia koiria, ja jokainen koira haukahtaa.

Aloitetaan pohtimalla sitä, mitä koirahoitolan toteuttamiseksi vaaditaan.

Ensinnäkin koirahoitola kannattaa toteuttaa omana luokkanaan. Hoitolan toiminnallisuus ei liity mitenkään yksittäiseen
koiraan, eikä sitä tule kirjoittaa Koira-luokan sisään. Kirjoitamme siis ohjelmaan toisen luokan nimeltä Hoitola.

Sitten pohdimme, mitä ominaisuuksia koirahoitolalla on. Huomaamme, että hoitolan täytyy
olla tietoinen siitä, mitä koiria siellä kulloinkin on hoidossa. Sen voimme toteuttaa listan avulla: liitetään
hoitolan ominaisuudeksi lista, jonka alkiot ovat koiria.

Entä onko hoitolalla toimintoja, jotka on syytä kirjoittaa metodeiksi?
Äsken tehdystä hoitolan määrittelystä tunnistetaan, että koirahoitolalle kannattaa laatia kolme
metodia:
1. koiran kirjaaminen sisään hoitolaan
2. koiran kirjaaminen ulos hoitolasta
3. kierroksen tekeminen hoitolassa.

Nyt ohjelma on määritelty ja suunniteltu, ja pääsemme toteuttamaan sen.

## Kahdesta luokasta koostuva ohjelma

Esimerkkiohjelmassamme on kaksi luokkaa: `Koira` ja `Hoitola`. Python-kielessä samaan lähdekooditiedostoon voidaan
kirjoittaa monta luokaa, ja näin usein tehdäänkin. Luokat voisivat sijaita myös eri tiedostoissa. Jos tähän ratkaisuun päädytään,
on toiseen tiedostoon viittaaminen mahdollista vain, jos ohjelman alkuun liitetään toisen tiedoston (eli moduulin)
esittelevä `import`-lause.

Pienissä ohjelmissa on näppärää kirjoittaa luokat samaan tiedostoon, ja niin teemme nytkin. Luomme koirahoitola.py-nimisen
tiedoston, ja ohjelmoimme sinne vaadittavan toiminnallisuuden:

```python
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self):
        self.koirat = []

    def koiraSisään(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + " kirjattu sisään")
        return

    def koiraUlos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + " kirjattu ulos")
        return

    def tervehdiKoiria(self):
        for koira in self.koirat:
            koira.hauku(1)

# Pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koiraSisään(koira1)
hoitola.koiraSisään(koira2)
hoitola.tervehdiKoiria()

hoitola.koiraUlos(koira1)
hoitola.tervehdiKoiria()
```

Esimerkkiohjelma koostuu kolmesta osasta:
1. `Koira`-luokasta
2. `Hoitola`-luokasta
3. pääohjelmasta.

Ohjelman suoritus alkaa pääohjelman alusta. Aluksi luodaan kaksi koiraa, Muro ja Rekku. Sitten luodaan uusi
hoitola:
```python
hoitola = Hoitola()
```

Tässä vaiheessa suoritus siirtyy Hoitola-luokan alustajaan, jossa luotavan hoitolan ominaisuudeksi
lisätään koirat-niminen tyhjä lista. Vasta luodussa hoitolassa ei vielä ole yhtään koiraa, mutta siinä on nyt
olemassa lista, johon koirat voidaan aikanaan lisätä.

Tämän jälkeen ensimmäinen koira (Muro) kirjataan sisään hoitolaan:
```python
hoitola.koiraSisään(koira1)
```
Kyseessä on hoitolan tarjoama metodi: sisäänkirjaus on selkeästi hoitolan toiminto, ja se on sen vuoksi ohjelmoitu
`Hoitola`-luokkaan. Sisäänkirjauksen yhteydessä on tietenkin kerrottava, mitä koiraa ollaan kirjaamassa. Tätä varten
`Koira`-olio (tai oikeastaan viittaus siihen) annetaan metodikutsun argumenttina. Metodikutsun seurauksena suoritus siirtyy
`koiraSisään`-metodiin, jossa parametrina saatu koira lisätään hoitolan koiralistaan.

Samaan tapaan hoitolaan lisätään toinen koira, Rekku.

Sitten hoitajan on aika tehdä hoitolassa kierros ja tervehtiä kaikkia koiria. Tätä varten kutsutaan vastaavaa `Hoitola`-luokkaan
kirjoitettua metodia:
```python
hoitola.tervehdiKoiria()
```
Tämä metodi toteutettiin parametrittomana. Tervehtiminen kohdistuu kaikkiin hoitolassa kulloinkin oleviin koiriin, ja
hoitola itse tietää, mitä koiria siellä kulloinkin on hoidossa. Metodi käy läpi koirien listan ja käskee
kutakin koiraa haukahtamaan yhden kerran.

Lopuksi esimerkkiohjelmassa kirjataam ulos yksi koira, Muro. Tätä varten kutsutaan `Hoitola`-luokkaan kirjoitettua vastaavaa
metodia, joka poistaa annetun alkion listasta. Tämän jälkeen koiria tervehditään jälleen, mutta tervehdykseen on
vastaamassa enää Rekku.

Ohjelman toiminta ilmenee sen tuottamasta tulosteesta:
```python
Muro kirjattu sisään
Rekku kirjattu sisään
Muro haukkuu: Vuh-vuh
Rekku haukkuu: Viu viu viu
Muro kirjattu ulos
Rekku haukkuu: Viu viu viu
```

Näin kirjoitimme ohjelman, jossa on ilmentymiä (eli olioita) kahdesta eri luokasta. Sanomme, että `Hoitola`-
ja `Koira`-luokkien välillä on pysyvä assosiaatiosuhde: `Hoitola`-oliolla on instanssimuuttuja, joka sisältää viittaukset
`Koira`-olioihin.

Assosiaatiosuhde on tässä yksisuuntainen: `Hoitola`-olio tietää, mitä koiria kulloinkin on hoidossa. `Koira`-olio sen sijaan
ei tiedä mitään hoitolasta, jossa se mahdollisesti on. Assosiaatiosuhde voidaan toteuttaa yksi- tai kaksisuuntaisena.
Kaksisuuntainen assosiaatiosuhde kannattaa ottaa käyttöön vain silloin, kun sille on hyvät perusteet. Tällöin
ohjelmoijalle tulee ylimääräistä kuormaa siitä, että eri suuntiin olevien olioviittausten on oltava sisällöiltään
synkronoidut.


## Tilapäinen assosiaatiosuhde

Edellä todettiin, että esimerkin `Hoitola`- ja `Koira`-luokkien välillä oli pysyvä assosiaatiosuhde: hoitolan koirat
on tallennettu hoitolan ominaisuutena olevaan koiralistaan.

`Hoitola`- ja `Koira`-luokkien välillä on myös toisenlainen riippuvuus: `Hoitola`-luokka tarjoaa kaksi metodia, joiden
parametrina annetaan viittaus `Koira`-olioon. Assosiaatiosuhde voi olla voimassa vain metodikutsun ajan silloin,
kun toisen luokan ilmentymä kerrotaan metodin parametrina. Kun metodin kutsu päättyy, katoaisi metodin suorituksen
aikainen assosiaatiosuhdekin, ellei tietoa suhteesta ole tallennettu ominaisuudeksi, kuten esimerkissämme on tehty.

Tarkastellaan nyt esimerkkiä tilanteesta, jossa assosiaatiosuhde on puhtaasti tilapäinen: auton ja maalaamon välistä
suhdetta. Esimerkissä luodaan sininen auto ja annetaan se maalaamolle maalattavaksi punaiseksi:

```python
class Auto:
    def __init__(self, rekisteritunnus, väri):
        self.rekisteritunnus = rekisteritunnus
        self.väri = väri

class Maalaamo:
    def maalaa(self, auto, väri):
        auto.väri = väri

maalaamo = Maalaamo()
auto = Auto("ABC-123", "sininen")
print("Auto on " + auto.väri)
maalaamo.maalaa(auto, "punainen")
print("Auto on nyt " + auto.väri)
```

Ohjelma tulostaa auton värin ennen ja jälkeen maalauksen:

```monospace
Auto on sininen
Auto on nyt punainen
```

Tässä esimerkissä maalaamo tuntee maalattavan auton vain `maalaa`-metodin suorituksen ajan, sillä viittaus `Auto`-olioon
on saatu metodikutsun parametrina. Kun metodin suoritus päättyy, parametrimuuttujan arvoon ei enää pääse käsiksi.
Myöskään auto ei tiedä maalaamosta mitään. Maalaamon ja auton assosiaatiosuhde on tässä esimerkissä tilapäinen.
