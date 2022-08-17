# Ensimmäinen ohjelma

Tervetuloa ohjelmoimaan Python-kieltä Metropolia Ammattikorkeakoulussa!

... ja sama Pythoniksi:
```
print("Tervetuloa opiskelemaan Python-kieltä!")
```
Python on maailman yleisimpiä ohjelmointikieliä. Kun opiskelet Pythonia, voit:
- oppia ohjelmoimaan helposti ja hauskasti
- koodata laadukkailla ja ergonomisilla kehitystyökaluilla
- luoda näyttävää grafiikkaa visualisointikirjastojen avulla
- soveltaa tekoälyä kattavien koneoppimiskirjastojen ansiosta

Ensimmäisenä opiskeluvuonna saat vankat Python-ohjelmoinnin perustaidot. Syvennät osaamistasi myöhemmissä opinnoissa,
ja opit käyttämään Python-kieltä työkaluna ohjelmointi- ja ohjelmistotuotantoprojekteissa.

Tässä ensimmäisessä moduulissa asennat Python-kehitystyökalut ja opit kirjoittamaan ja ajamaan ensimmäisen Python-ohjelmasi.

## Kehittimen asennus

Aloitetaan kehittimen eli IDE:n asentamisesta. IDE on lyhenne englannin kielen sanoista
*Integrated Development Environment*. Se tarkoittaa ammattikäyttöön
soveltuvaa ohjelmistoa, jonka avulla voit kirjoittaa, ajaa ja testata ohjelmia.

Tällä opintojaksolla käytetään JetBrains PyCharm -kehitintä, jonka voit ladata seuraavasti:
1. Siirry osoitteeseen https://www.jetbrains.com/
2. Valitse **Developer tools / PyCharm** ja paina **Download**.
3. Valitse ladattavaksi Professional-versio.
4. Saat käyttöön oikeuttavan lisenssin, kun rekisteröit ohjelmiston käyttäen Metropolian opiskelijana. Asennusohjelma opastaa sinua tässä. Käyttöönotto edellyttää JetBrains-tilin luomista ja opiskelijalisenssin hankkimista. Voit opiskelijana hankkia maksutta vuoden kerrallaan voimassa olevan lisenssin napsauttamalla JetBrains-sivuston yläreunassa olevaa ostoskärrikuvaketta ja valitsemalla **Special offers / For students and teachers**. Syötä lomakkeen tiedot käyttämällä Metropolian sähköpostiosoitetta ja viimeistele aktivointi sähköpostiin saamasi ohjeen mukaan. Kun lisenssi on vuoden päästä vanhenemassa, saat sähköpostiin automaattisesti ohjeen sen uusimisesta.  

Asennuksen jälkeen voit käynnistää PyCharm-ohjelman napsauttamalla sen kuvaketta.

## Projektin ja Python-tiedoston luonti

Ennen kuin voit kirjoittaa ohjelmia, on perustettava projekti. Projektia voi ajatella eräänlaisena
salkkuna, johon kerätään samaan aihepiiriin liittyviä ohjelmia. Esimerkiksi ensimmäisiä ohjelmointikokeiluja
varten voit perustaa uuden projektin nimeltä ´kokeilut´. Nimi kirjoitetaan projektin tiedostopolun perään:

![Uuden projektin luonti](img/uusiprojekti.png)

Uusi projekti perustetaan oletusarvoisesti virtuaaliympäristöön (venv). Tämä helpottaa ohjelmien käyttämien
pakkausten ja niiden versioiden hallintaa.

Kun painat **Create**, kehitin kysyy, avataanko projekti olemassaolevassa vai uudessa ikkunassa. Voit valita kumman vain vaihtoehdon.

Näytön vasempaan reunaan ilmestyy projektipuu, joka näyttää projektiin kuuluvat tiedostot:

![Uuden projektin luonti](img/projektipuu.png)

Jokainen ohjelma kirjoitetaan tiedostoon projektin kansiohierarkian sisälle. Voit tehdä ensimmäistä
ohjelmaa varten uuden tiedoston napsauttamalla projektin nimeä projektipuussa hiiren kakkospainikkeella.
Valitse sitten **New / Python file** ja kirjoita avautuvaan valintaikkunaan tiedoston nimi, esimerkiksi
`hello`.
Projektipuuhun ilmestyy kuvassa näkyvä tiedosto nimeltä `hello.py`. Python-ohjelma kirjoitetaan tiedostoihin, joiden päättenä on ´.py´. 


## Ohjelman kirjoitus, tallennus ja ajo

Ohjelma, eli Python-lähdekoodi, kirjoitetaan editorikenttään: 

![Ensimmäinen ohjelma](img/ekaohjelma.png)

Voit suorittaa eli ajaa ohjelman napsauttamalla hiiren kakkospainiketta editorikentässä ja valitsemalla **Run 'hello'**.

Tuloste ilmestyy alareunan konsoli-ikkunaan:

```python
Hei, maailma!
```

Jos ohjelmassa on virheitä, ei hätää! Saat virheilmoituksen, joka auttaa virheen paikantamisessa. Sen jälkeen voit
korjata ohjelmaa niin monta kertaa kuin on tarpeen ja suorittaa sen aina uudelleen.

Virheiden teko kuuluu ohjelmointiin. On arvioitu, että 80 prosenttia ammattimaisen ohjelmoijan työajasta kuuluu
virheiden jäljitykseen ja niiden korjaamiseen. Myös oppiminen tapahtuu virheitä tekemällä. Kun selvität virheen
syyn ja korjaat sen, olet oppinut hieman paremmaksi ohjelmoijaksi.

