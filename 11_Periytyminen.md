# Periytyminen

Periytyminen on olio-ohjelmoinnin mekanismi, jossa luokkien välille muodostetaan hierarkia: yksittäisestä
luokasta, jotka kutsutaan yliluokaksi, johdetaan sitä tarkentavia ja täsmentäviä aliluokkia.

Tässä moduulissa opit käyttämään periytymissuhdetta kirjoittaessasi oliopohjaisia Python-olioita.

## Yliluokka ja aliluokka

Tarkastellaan seuraavaa tilannetta, jossa ohjelma käsittelee Työntekijä-olioita:

```python
class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))

for t in työntekijät:
    t.tulosta_tiedot()
```

Ohjelma luo kaksi työntekijä: Viivin ja Ahmedin, lisää heidät työntekijälistaan ja tulostaa listan sisällön:

``` monospace
1: Viivi Virta
2: Ahmed Habib
```

Jokaisella työntekijällä on kolme ominaisuutta: työntekijänumero, etunimi ja sukunimi. Työntekijänumero annetaan
jokaiselle työntekijälle automaattisesti työntekijöiden lukumäärän perusteella. Työntekijöiden lukumäärä on
tässä luokkamuuttuja: sen arvoa ei ole määritelty erikseen jokaiselle Työntekijä-luokan oliolle, vaan
arvo on määritelty kertaalleen Työntekijä-luokalle. Huomaa, että luokkamuuttuja määritellään alustajan ulkopuolella,
ja siihen viitattaessa käytetään `self`-sana korvataan luokan nimellä.


Oletetaan, että kohtaamme uuden kehitystarpeen: osa työntekijöistä on tuntipalkkaisia työntekijöitä
ja osa kuukausipalkkaisia. Miten palkkatieto tulisi lisätä Työntekijä-luokan ominaisuuksien luetteloon?

Yksi ratkaisu olisi lisätä kaksi eri ominaisuutta: tuntipalkka ja kuukausipalkka. Ratkaisu olisi
kuitenkin epätarkka, ja sovellusta käytettäessä joutuisimme aina tarkastamaan kenttien arvojen perusteella,
kumpi työntekijän alatyyppi on kyseessä. Lisäksi mikään ei teknisesti estäisi meitä määrittämästä
samalle työntekijälle sekä tunti- että kuukausipalkkaa.

Otetaan ratkaisuksi Python-kielen periytymismekanismi.
Kirjoitetaan Työntekijä-luokalle kaksi tarkentavaa aliluokkaa:
Tuntipalkkainen ja Kuukausipalkkainen. Kun luomme uuden olion, voimme tehdä siitä esimerkiksi Tuntipalkkainen-aliluokan
ilmentymän. Tällöin sillä on kaikki Työntekijä-yliluokasta perityt ominaisuudet ja metodit (kuten etunimi-ominaisuus
ja työskentele-metodi), mutta niiden lisäksi käytössä on vain tuntipalkkaisille työntekijöille aliluokassa määritetty
tuntipalkka-ominaisuus.

Laajennettu ohjelma näyttää tältä:

```python
class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in työntekijät:
    t.tulosta_tiedot()

```

Esimerkissä luodaan kaksi tuntipalkkaista työntekijää, yksi kuukausipalkkainen työntekijä sekä yksi työntekijä (Pekka), jonka
osalta ei oteta kantaa, minkälainen hänen työsuhteensa on.

Toistorakenne tuottaa seuraavan tulosteen:
```monospace
1: Viivi Virta
 Tuntipalkka: 12.35
2: Ahmed Habib
 Kuukausipalkka: 2750
3: Pekka Puro
4: Olga Glebova
 Tuntipalkka: 14.92
```


Yliluokka-aliluokkasuhde ilmaistaan Pythonissa siten, että aliluokan määrittävään `class`-lauseeseen
lisätään sulkeisiin yliluokan nimi. Siis lauseen alku `class Tuntipalkkainen(Työntekijä)` määrää,
että Tuntipalkkainen-luokasta tulee Työntekijä-luokan aliluokka.

Aliluokalle kirjoitetaan tarvittaessa oma alustaja. Kun aliluokan ilmentymä luodaan, vain aliluokkaan
kirjoitettu alustaja suoritetaan. Käytännössä usein halutaan toimia kuten esimerkissämme: ohjelmassa kutsutaan
aliluokan alustajaa, joka puolestaan kutsuu yliluokan alustajaa. Tässä tapauksessa aliluokan alustaja
antaa arvon tuntipalkalle, kun taas etunimi ja sukunimi on määritetty yliluokassa. Niiden arvot välitetään
yliluokalle kutsumalla yliluokan alustajaa eli `__init__`-metodia. Olion yliluokkaan päästään käsiksi
super()-funktion avulla: lause `super().__init__(etunimi, sukunimi)` kutsuu siis yliluokan alustajaa,
joka saa parametreinaan etu- ja sukunimen.

Yliluokassa määritetyt ominaisuudet näkyvät automaattisesti aliluokkaan. Voimme siis luoda `Tuntipalkkainen`-luokan ilmentymän
`t` ja milloin tahansa hakea hänen etunimensä ilmaisulla `t.etunimi`.

## Metodien ylikirjoittaminen

Kun tarkastelemme edellä olevaa esimerkkiä, havaitsemme, että `Työntekijä`-yliluokkaan kirjoitettu `tulosta_tiedot`-metodi 
tulostaa henkilön etu- ja sukunimen. Metodi toimii hyvin silloin, kun henkilö on luotu `Työntekijä`-luokan
ilmentymäksi ottamatta kantaa siihen, onko hän tunti- vai kuukausipalkkainen. Toisaalta esimerkiksi tuntipalkkaisten
työntekijöiden tietojen tulostamiseen metodi on liian suppea: se tulostaa nimitiedot mutta ei pääse käsiksi
aliluokassa määritettyyn tuntipalkkaan.

Ongelma ratkeaa ylikirjoittamalla `tulosta_tiedot`-metodi. Ylikirjoittaminen tarkoittaa sitä, että aliluokkaan
luodaan toinen toteutus yliluokassa olevasta metodista. Aliluokassa oleva, ylikirjoitettu metodi menee edelle
yliluokassa määritellystä metodista. Kun siis kirjoitamme `t.tulosta_tiedot()` oliolle, joka on
`Tuntipalkkainen`-luokan ilmentymä, kutsutaan automaattisesti `Tuntipalkkainen`-luokassa olevaa versiota metodista.
Jos sama metodikutsu kirjoitetaan `Työntekijä`-luokan ilmentymäksi luodulle oliolle, kutsutaan yliluokassa
olevaa versiota.

Ylikirjoittamisen ansiosta saamme ohjelmaan joustavuutta: työntekijät voivat olla keskenään erilaisia, ja niiden
tietorakenteet voivat poiketa toisistaan. Tästä huolimatta kaikkien työntekijöiden tiedot saadaan pääohjelmassa
tulostettua yksinkertaisella toistorakenteella:

```
for t in työntekijät:
    t.tulosta_tiedot()
```

Kutsuttavan metodin muunnelmat ja toteutustekniset yksityiskohdat on piilotettu sinne minne ne kuuluvat: toteuttaviin luokkiin.
Pääohjelmaan ne eivät säteile.

## Moniperintä

Toisinaan on tilanteita, joissa sama luokka halutaan määrittää kahden tai jopa useamman luokan aliluokaksi.
Tätä piirrettä kutsutaan moniperinnäksi. Python-kielessä moniperintä on sallittua toisin kuin joissain
muissa olio-ohjelmointikielissä.

Seuraava esimerkki kuvaa moniperintää. Määritetään kaksi luokkaa: `Kulkuneuvo` ja `Urheiluväline`. Kolmas luokka `Polkupyörä` voidaan
asettaa molempien mainittujen luokkien aliluokaksi.

```python
class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino

class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)
        
        self.vaihteet = vaihteet

pp = Polkupyörä(45, 18.7, 3)
print (pp.vaihteet)
print (pp.nopeus)
print (pp.paino)
```

Luomme Polkupyörä-olion, josta tulostamme vaihteiden lukumäärän, nopeuden ja painon. Vaihteiden lukumäärä on määritetty 
`Polkupyörä`-luokassa. Nopeus periytyy `Kulkuneuvo`-luokasta, ja paino periytyy `Urheiluväline`-luokasta. Ohjelma tuottaa seuraavan tulosteen:
```monospace
3
45
18.7
```


Tässä tapauksessa emme voi `Polkupyörä`-luokan alustajasta viitata molempien yliluokkien alustajin
`super`-funktiolla tähän tapaan:

```python
# Toimimattomat alustajien kutsut
super().__init__(nopeus)
super().__init__(paino)
```
Yliluokka, johon `super`-funktio viittaa, määräytyy Pythonin metodien etsintäjärjestyksen perusteella. Tässä tapauksessa
kumpikin lause kutsuisi `Kulkuneuvo`-luokassa olevaa alustajaa, ja ohjelma toimisi väärin.

Voimme kutsua yliluokkien alustajia vaihtoehtoisella notaatiolla, jossa yliluokka mainitaan nimeltä:

```python
Kulkuneuvo.__init__(self, nopeus)
Urheiluväline.__init__(self, paino)
```
