# Luokka ja olio
Tässä moduulissa opit olio-ohjelmoinnin perusteet. Opit kirjoittamaan luokkia, jotka määrittävät yhteiset ominaisuudet
ja operaatiot luokan ilmentymille eli olioille. Opit olioiden luonnin, alustamisen ja käytön periaatteet.

## Luokka

Olio-ohjelmoinnissa luokalla tarkoitetaan yleiskäsitettä, joka määrittää yleiset ja yhteiset piirteet, joita
sen jäsenillä on.

Esimerkiksi **koira** on tällainen yleiskäsite. Jokaisella koiralla on joukko ominaisuuksia
kuten nimi ja syntymävuosi. Lisäksi koiralla on toimintoja (eli Python-termein metodeja) kuten haukkuminen.

Voimme nyt kirjoittaa pienimmän mahdollisen Koira-luokan seuraavasti:
```python
class Koira:
    pass
```

Edellä `pass`-lause on tyhjä lause, joka ei tee mitään. Se tarvitaan paikkamerkiksi, sillä luokan määrityksen rungossa on oltava
ainakin yksi lause.

Tämä luokan määritys vain kertoo, että on olemassa Koira-luokka. Se ei toistaiseksi ota kantaa koirien ominaisuuksiin
eikä niiden metodeihin.

Voimme käyttää Koira-luokkaa siten, että luomme tuosta luokasta olion. Olio tarkoittaa luokan ajonaikaista ilmentymää
eli realisaatiota. Luomme näin Koira-olion, joka on nimeltään Rekku ja jonka syntymävuosi on 2022: 



```python
class Koira:
    pass
   
koira = Koira()
koira.nimi = "Rekku"
koira.syntymävuosi = 2022

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." )
```

Pääohjelman ensimmäinen lause luo Koira-olion, johon viitataan muuttujalla `koira`. Luodulle koiralle annetaan
nimeksi Rekku ja syntymävuodeksi 2022. Nämä ovat luodun olion ominaisuuksia, ja ne ovat oliokohtaisia. Voisimme siis luoda
monta koiraa, joista jokaisella olisi oma yksilöllinen nimensä ja syntymävuotensa. Jollekin koirista voisimme
lisäksi määrittää rodun ja jollekin lempinimen. Olioiden ominaisuudet voivat siis poiketa toisistaan.

Kuten esimerkistä näkyy, olion ominaisuuteen viitataan kirjoittamalla ensin olion nimi, sitten piste ja lopuksi
ominaisuuden nimi. Esimerkki tällaisesta viittauksesta on `koira.nimi`.

Esimerkkiohjelman viimeinen lause tulostaa pääohjelman luoman koiraolion nimen ja syntymävuoden:
```monospace
Rekku on syntynyt vuonna 2022.
```

Huomaa Python-kielen vakiintunut kirjoitustapa luokkien nimille: ne kirjoitetaan isoin alkukirjaimin. Jos luokan nimi koostuu
useammasta sanasta, sanat kirjoitetaan yhteen ilman alaviivamerkkiä siten, että kukin sana aloitetaan isolla
alkukirjaimella. Tästä kirjoitustyylistä käytetään nimitystä *CamelCase*. Esimerkki tällaisesta luokan nimestä
on `NäytönSuorakulmio`.


## Alustaja eli konstruktori

Edellä Koira-olio luotiin siten, että ensin tehtiin olio ilman ominaisuuksia, ja sen jälkeen oliolle määritettiin
ominaisuudet yksi kerrallaan. Tämä on ohjelmoijalle melko työläs tapa luoda olioita.

Olioiden luonnin helpottamiseksi luokan sisälle kirjoitetaan usein alustaja eli konstruktori, joka automaattisesti
asettaa halutut arvot luotavan olion ominaisuuksiksi. Seuraavan esimerkin luokassa on nimen ja syntymävuoden asettava
alustaja. Pääohjelma käyttää olion luonnissa juuri laadittua alustajaa:

```python
class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira = Koira("Rekku", 2022)

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." )
```

Python-kielen alustaja määritetään luokan sisällä kirjoittamalla funktio, jonka nimenä
on `__init__`. Funktion ensimmäiseksi parametriksi määritetään aina `self`. Tämän jälkeen määritellään
muut parametrit, jotka alustajalle halutaan antaa. Tässä tapauksessa ne ovat nimi ja syntymävuosi. Näin kirjoitettu
ja nimetty funktio tulkitaan ohjelmaa ajettaessa automaattisesti alustajaksi, ja se suoritetaan aina, kun uusi
olio luodaan. Alustajan loppuun ei kirjoiteta return-lausetta.

Alustajan sisällä on kaksi sijoituslausetta, joilla annetaan arvot luotavan olion ominaisuuksille.
Uuden olion ominaisuuksiin viitataan kirjoittamalla varattu sana `self`, minkä jälkeen tulee piste ja halutun
ominaisuuden nimi. Uuden olion ominaisuuden arvoksi annetaan tyypillisesti alustajan parametrina saatu arvo. Esimerkiksi
lause `self.nimi = nimi` antaa uuden olion nimi-ominaisuuden arvoksi nimi-parametrimuuttujan arvon.

Huomaa, että oliota luotaessa alustajan ensimmäinen parametri `self` ohitetaan kokonaan. Ei siis kirjoiteta:
```python
# Virheellinen luontilause
koira = Koira(self, "Rekku", 2022)
```
vaan kirjoitetaan:
```python
koira = Koira("Rekku", 2022)
```


## Metodit

Edellä opittiin määrittämään oliolle ominaisuuksia. Tämän lisäksi olioille halutaan usein määrittää toimintoja, joita 
kutsutaan metodeiksi. Kirjoitetaan alla Koira-luokkaan hauku-metodi, jota voidaan kutsua Koira-luokan ilmentymille eli
olioille. Esimerkin ohjelma luo kaksi Koira-oliota ja käskee niitä haukkumaan kyseiselle oliolle
tyypilliseen tapaan:

```python
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)
```

Alustajan parametreja on nyt kolme. Viimeiselle parametrille (`haukahdus`) on annettu oletusarvo, joka asetetaan
silloin, kun parametria ei oliota luetaessa anneta. Esimerkissä Muro-koira saa siis oletushaukahduksen.

Luokan sisään kirjoitettiin `hauku`-niminen metodi, jota voidaan kutsua mille tahansa olemassa olevalle Koira-luokan
ilmentymälle. Metodin ensimmäiseksi parametriksi asetetaan aina `self`. Tämän jälkeen luetellaan muut parametrit, joiden
arvo annetaan metodia kutsuttaessa.

Metodin kutsu tehdään siten, että kirjoitetaan olion nimi, sen jälkeen piste ja lopuksi metodin nimi kaarisulkeineen
ja mahdollisine parametreineen. Esimerkiksi kutsu `koira1.hauku(2)` kutsuu koira1-olion hauku-metodia. Metodikutsun parametrina
välitetään haukahdusten määrä (2). Metodin sisällä voidaan viitata olion omiin ominaisuuksiin siten,
että kirjoitetaan `self`, jota seuraa piste ja ominaisuuden nimi. Esimerkiksi ilmaisu `self.haukahdus` viittaa kulloisenkin
olion `haukahdus`-ominaisuuden arvoon.
