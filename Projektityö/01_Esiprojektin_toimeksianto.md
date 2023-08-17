# Esiprojektin toimeksianto

Tavoitteenanne on rakentaa **toiminnallinen prototyyppi pelistä**.

![Sähkölentokone](img/Pipistrel_WATTsUP_airplane.jpg)

<sub><sup>Pipistrel WATTsUP -sähkölentokoneen kuva: Ymmo, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</sup></sub>


Pelin prototyyppi on peli, jonka
avulla käyttäjä voi matkustaa joko koko maailmassa tai sallimallanne alueella. Peli hyödyntää
todellisten lentokenttien sijanteja.



Projekti etenee neljässä vaiheessa:

1. Pelin määrittely esiprojektia varten (Ohjelmisto 1)
2. Esiprojektin toteutus ja testaus (Ohjelmisto 1)
3. Määrittelyn tarkennus projektityötä varten (Ohjelmisto 2)
4. Projektityön toteutus ja testaus (Ohjelmisto 2)

Ensimmäiset kaksi vaihetta tehdään Ohjelmisto 1 -opintojakson aikana. Tällöin toteutettavassa esiprojektissa on tarkoitus rakentaa pelistä toiminnallinen prototyyppi, joka toteutetaan Python-kielellä ja joka hyödyntää relaatiotietokantaa.

Jälkimmäiset kaksi vaihetta tehdään Ohjelmisto 2 -opintojakson kuluessa. Projektityössä esiprojektin tuloksena syntynyttä toiminnallista prototyyppiä laajennetaan ja muokataan siten, että pelillä on selaimessa toimiva karttapalvelua hyödyntävä käyttöliittymä. Lisäksi peli ohjelmoidaan käyttämään ulkoista tietolähdettä, esimerkiksi sääpalvelua.

Esiprojektin määrittelyvaiheen tarkoituksena on saavuttaa yhteinen näkemys siitä, minkälaista ohjelmistoa esiprojektissa lähdetään rakentamaan. Vaiheen tuloksena syntyy kirjallisessa muodossa oleva määrittelydokumentti, joka kuvaa ohjelmiston toiminnallisuuden eli sen,
mitä tulevalla ohjelmistolla voidaan tehdä. Vaatimusmäärittelyssä otetaan lisäksi kantaa ohjelmiston sellaisiin
vaatimuksiin, joita ei voida pelkistää toiminnoiksi. Näitä kutsutaan laadullisiksi vaatimuksiksi, ja ne voivat liittyä esimerkiksi
suorituskykyyn, vasteaikoihin tai käytettävyyteen.


## Määrittelydokumentti

Määrittelydokumentin tärkein hyve on konkreettisuus. Ohjelman toiminta kuvataan sellaisella tarkkudella, että tulkinnalle
jää mahdollisimman vähän sijaa. Asioita ei lähtökohtaisesti jätetä toteutusvaiheessa päätettäviksi.

Määrittelydokumentissa kuvataan siis toiminta ja laadulliset vaatimukset. Näkökulma on ohjelmiston käyttäjässä: dokumentti
vastaa kysymykseen "Mitä käyttäjä voi ohjelmistolla tehdä?". Toteutustekniikoihin ei oteta kantaa.

Lentopelin määrittelydokumentin on sisällettävä ainakin seuraavat luvut:
1. Johdanto
2. Visio
3. Toiminnalliset vaatimukset
4. Laadulliset vaatimukset

Luku 1 (Johdanto) kuvaa, mikä dokumentin tarkoitus on ja kenelle se on suunnattu. Johdannossa voidaan myös esitellä dokumentin rakenne.

Luku 2 (Visio) kuvaa lentopelin yleisidean. Mikä on pelin tarkoitus, ja mitä pelissä tehdään? Visio voidaan esittää
myös kuvana, jonka tueksi laaditaan tekstiselostus. Selostakaa tässä vapaamuotoisesti pelin "punainen lanka": miten peli
etenee, ja millaisia vaiheita pelaaja käy läpi?

Luku 3 (Toiminnalliset vaatimukset) kuvaa periaatteessa kaiken, mitä käyttäjä voi pelillä tehdä. Toiminnalliset vaatimukset esitetään tyypillisesti käyttäjätarinoina, joissa on tekijä, toimenpide ja tavoite. Esimerkki käyttäjätarinasta on "Pelaajana
voin valita karttapohjalla näkyvistä kohteista seuraavan lentokentän, jotta sähkölentokoneeni siirtyy sinne". Käyttäjätarinassa kuvataan siis tekijä (pelaaja), toimenpide (kentän valinta) sekä käyttäjää hyödyttävä tavoite,
joka toimenpiteestä seuraa (kohteeseen siirtyminen). Käyttäjätarinoita laaditaan niin monta, että ne yhdessä kuvaavat pelin toiminnallisuuden. Lentopelille käyttäjätarinoita tarvittaneen useita kymmeniä. Jokaisen käyttäjätarinan on oltava yksiselitteinen ja konkreettinen. Käyttäjätarinan pohjalta on voitava aikanaan todentaa, onko vastaava toiminnallisuus toteutettu ohjelmistossa.
 
Luku 4 (Laadulliset vaatimukset) tarkentaa, millaisia muita kuin toiminnallisia vaatimuksia lentopelillä on. Näitä voivat olla esimerkiksi suorituskykyvaatimukset ("Lentokentän tietojen haku tietokannasta saa kestää korkeintaan kaksi sekuntia") tai
käytettävyysvaatimukset ("Käyttäjän on saatava välitön palaute jokaisesta tekemästään toimenpiteestä").

## Pelin reunaehdot

Määrittelyn pohjaksi asetetaan joukko reunaehtoja. Reunaehtojen tarkoitus on varmistaa, että saavutatte peliprojektin aikana ne oppimistavoitteet, joita opintojaksoille on määritetty.

Voitte siis määritellä ja toteuttaa minkälaisen pelin tahansa, kunhan se toteuttaa alla kuvatut reunaehdot:

1. Käyttäjä pelaa peliä vuorovaikutteisesti näppäimistön avulla.
2. Peli käyttää relaatiotietokantaa, jonka pohjana on opintojaksolla käytetty lentokenttätaulu. Tietokannan skeemaa saa vapaasti muuttaa ja laajentaa.
3. Pelissä on konkreettinen tavoite, ja se tuottaa hyvän pelikokemuksen.
4. Peli huomioi kestävän kehityksen näkökulman.
5. Peli on hyvien tapojen mukainen ja soveltuu myös nuorille käyttäjille (K12).

## Määrittelydokumentin arviointi

Määrittelydokumentin arviointi perustuu dokumentin kattavuuteen ja laatuun. Erityisesti arvioidaan seuraavia seikkoja:
- Saako vision perusteella yleiskuvan pelistä ja sen ideasta?
- Onko pelin toiminnallisuus kuvattu kattavasti, yksiselitteisesti, konkreettisesti ja toteuttamiskelpoisesti? Saako dokumentista tarkan käsityksen siitä, miten peli toimii?
- Sisältääkö peli uudenlaisia ideoita?
- Onko tarpeelliset laadulliset vaatimukset kuvattu konkreettisesti?
- Huomioiko vaatimusmäärittely pelille asetetut reunaehdot?
- Onko määrittelydokumentti kielensä ja ulkoasunsa puolesta laadukas tekninen asiakirja?
