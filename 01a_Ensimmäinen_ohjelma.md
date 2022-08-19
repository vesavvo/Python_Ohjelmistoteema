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

## Python-tulkin asennus

Tällä opintojaksolla käytetään Python-ohjelmointikieltä ja JetBrains PyCharm -kehitintä.

Python-tulkki on ohjelma, joka lause
kerrallaan tulkkaa Python-kieliset lauseet tietokoneen suorittimen ymmärtämään muotoon eli konekielelle. Sen asentaminen
on välttämätöntä, jotta voit ohjelmoida Pythonilla.

Lataa Python-tulkki käyttöösi seuraavasti:

1. Siirry selaimella sivulle https://www.python.org/downloads/.
2. Valitse **Downloads / All releases**
3. Selaa sivua alemmaksi kohtaan **Looking for a specific release?**. Napsauta **Download** jonkin versionumeron
3.7.X - 3.9.X kohdalla, missä X voi olla mikä tahansa numero.
4. Lataa Python napsauttamalla sivun alaosassa linkkiä **Windows installer (64-bit)**.
5. Etene ohjatun toiminnon
esittämällä tavalla, ja asenna Python asennusohjelman ehdottamaan oletussijaintiin.

Tällä kurssilla käytetään MariaDB-tietokantaa. Sen vaatima MySQL Connector/Python -ajuri ei tätä kirjoitettaessa (elokuu 2022)
vielä tue uusimpia Python 3.10 -versioita. Tästä syystä kannattaa valita hieman vanhempi versio (esimerkiksi 3.9), jolle
tuki on jo olemassa. Jos lataat nyt uusimman Python-version, voit myöhemmin joutua asentamaan aiemman version rinnalle.

## Kehittimen asennus

Seuraavaksi asennetaan PyCharm-kehitin eli IDE. IDE on lyhenne englannin kielen sanoista
*Integrated Development Environment*. Se tarkoittaa ammattikäyttöön
soveltuvaa ohjelmistoa, jonka avulla voit kirjoittaa, ajaa ja testata ohjelmia.

PyCharm-kehittimen voit ladata seuraavasti:
1. Siirry osoitteeseen https://www.jetbrains.com/
2. Valitse **Developer tools / PyCharm** ja paina **Download**.
3. Valitse ladattavaksi Professional-versio.
4. Saat käyttöön oikeuttavan lisenssin, kun rekisteröit ohjelmiston Metropolian opiskelijana. Asennusohjelma opastaa sinua tässä. Käyttöönotto edellyttää JetBrains-tilin luomista ja opiskelijalisenssin hankkimista. Voit opiskelijana hankkia maksutta vuoden kerrallaan voimassa olevan lisenssin napsauttamalla JetBrains-sivuston yläreunassa olevaa ostoskärrykuvaketta ja valitsemalla **Special offers / For students and teachers**. Syötä lomakkeen tiedot käyttämällä Metropolian sähköpostiosoitetta ja viimeistele aktivointi sähköpostiin saamasi ohjeen mukaan. Kun lisenssi on vuoden päästä vanhenemassa, saat sähköpostiin automaattisesti ohjeen sen uusimisesta.  

Asennuksen jälkeen voit käynnistää PyCharm-ohjelman napsauttamalla sen kuvaketta.

Kun käynnistät kehittimen ensimmäistä kertaa, PyCharm saattaa tarjota esittelykierrosta tai tervetuloprojektia.
Voit kieltäytyä niistä.

## Projektin ja Python-tiedoston luonti

Nyt olet valmis kirjoittamaan ensimmäisen ohjelman. Ensimmäiseksi on perustettava projekti. Projektia voi ajatella eräänlaisena
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
`heimaailma`.
Projektipuuhun ilmestyy kuvassa näkyvä tiedosto nimeltä `heimaailma.py`. Python-ohjelma kirjoitetaan tiedostoihin, joiden päättenä on ´.py´. 


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

