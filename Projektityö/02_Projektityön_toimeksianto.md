# Projektityön toimeksianto

Projektityön tavoitteena on muokata ja täydentää esiprojektin aikana rakentamaanne toiminnallista prototyyppiä siten,
että tuloksena on **karttapalvelua ja ulkoista tietolähdettä käyttävä selaimen kautta pelattava lentopeli**.

![Kuumailmapallo](img/640px-Hot_Air_Balloon_Launch_(Unsplash).jpg)

<sub><sup>Kuumailmapallon kuva: Songeunyoung songeunyoung, CC0, via Wikimedia Commons</sup></sub>


## Määrittelydokumentti

Projektityön määrittelydokumentti kuvaa, mitä projektityön tuotoksena saatavalla, laajennetulla lentopelillä voidaan tehdä.
Voitte hyödyntää esiprojektin määrittelydokumentin sisältöä ja osia uudessa määrittelydokumentissanne. Määrittelyvaiheessa hyödynnetään Projektityö-kansiossa olevaa valmista määrittelydokumentin pohjaa.

Projektityön määrittelydokumentin on sisällettävä ainakin seuraavat luvut:
1. Johdanto
2. Visio
3. Läpäisykuvaus
4. Poikkeavat suorituspolut
5. Laadulliset vaatimukset
6. Muut seikat

Luku 1 (Johdanto) kuvaa, mikä dokumentin tarkoitus on ja kenelle se on suunnattu. Johdannossa voidaan myös esitellä dokumentin rakenne.

Luku 2 (Visio) kuvaa uuden, laajennetun lentopelin yleisidean. Miten käyttäjä pelaa peliä, ja mitä pelissä tapahtuu?
Visio voidaan jälleen esittää
myös kuvana, jonka tueksi laaditaan tekstiselostus.

Luku 3 (Läpäisykuvaus) kuvaa konkreettisesti, miten pelin kulku etenee tyypillisellä käyttökerralla.

Luku 4 (Poikkeavat suorituspolut) kuvaa toiminnan siltä osin, kuin se ei ilmene läpäisykuvauksesta. Tässä kuvataan muun muassa vika- ja virhetilanteiden käsittely

Luku 5 (Laadulliset vaatimukset) tarkentaa, millaisia muita kuin toiminnallisia vaatimuksia lentopelillä on. Näitä voivat olla esimerkiksi vasteaika- ja käytettävyysvaatimukset.

Luku 6 (Muut seikat) esittelee muut mahdolliset määrittelyvaiheessa esiin tulevat seikat.



## Pelin reunaehdot

Projekityön tuotoksena olevaan lentopeliin liittyvät alla kuvatut reunaehdot.
Voitte jälleen määritellä ja toteuttaa minkälaisen pelin tahansa, kunhan se toteuttaa alla kuvatut ehdot:

1. Käyttäjä pelaa peliä vuorovaikutteisesti selaimessa.
2. Käyttöliittymä on toteutettu HTML-sivunmäärityskielen ja CSS-tyylisivujen avulla. Välttämättömän selaintoiminnallisuuden toteuttamiseen käytetään JavaScript-kieltä.
3. Pelin toimintalogiikka on toteutettu Python-kielisenä taustapalveluna, joka tarjoaa selaimelle rajapinnan (API).
4. Taustapalvelun ja selaimen välinen kommunikaatio toteutetaan API-pyynnöin ja JSON-vastauksin.
5. Pelin taustapalvelu käyttää relaatiotietokantaa, jonka pohjana on opintojaksolla käytetty lentokenttätietokanta. Tietokannan skeemaa saa vapaasti muuttaa ja laajentaa.
6. Pelissä on konkreettinen tavoite, ja se tuottaa hyvän pelikokemuksen.
7. Peli huomioi kestävän kehityksen näkökulman.
8. Peli on hyvien tapojen mukainen ja soveltuu myös nuorille käyttäjille (K12).

Seuraavat seikat eivät ole välttämättömiä, mutta ne katsotaan eduksi:

1. Selaimessa näytetään satelliitti- tai karttadataa graafisesti.
2. Ohjelmoinnissa hyödynnetään Pythonin oliopiirteitä.
3. Pelin taustapalvelu kommunikoi ulkoisten tietolähteiden kanssa.

## Määrittelydokumentin arviointi

Projekityön määrittelydokumentilla on vastaavat kriteerit kuin esiprojektissa tehdyllä määrittelydokumentilla.Määrittelydokumentin arviointi perustuu dokumentin kattavuuteen ja laatuun. Erityisesti arvioidaan seuraavia seikkoja:
- Saako vision perusteella yleiskuvan pelistä ja sen ideasta?
- Onko pelin toiminnallisuus kuvattu kattavasti, yksiselitteisesti, konkreettisesti ja toteuttamiskelpoisesti? Saako dokumentista tarkan käsityksen siitä, miten peli toimii?
- Sisältääkö peli uudenlaisia ideoita?
- Onko tarpeelliset laadulliset vaatimukset kuvattu konkreettisesti?
- Huomioiko vaatimusmäärittely pelille asetetut reunaehdot?
- Onko määrittelydokumentti kielensä ja ulkoasunsa puolesta laadukas tekninen asiakirja?
