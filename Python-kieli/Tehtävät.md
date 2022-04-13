# Harjoitustehtäviä

## 1. Ensimmäinen ohjelma ja versionhallinnan käyttöönotto

1. Asenna PyCharm-kehitin. Kirjoita ohjelma, joka tervehtii sinua omalla nimelläsi.
Jos nimesi on Viivi Virta, ohjelma tulostaa: `Hei, Viivi Virta!`
2. Luo itsellesi GitHub-käyttäjätili ja tee repositorio Python-harjoitustehtäviä varten. Määritä  PyCharm käyttämään
repositoriota harjoitustehtäväprojektin tietojen tallentamiseen. Varmista, että voit hakea, sitouttaa ja työntää
tekemiäsi muutoksia (*pull*, *commit*, *push*).

## 2. Muuttujat ja vuorovaikutteiset ohjelmat

1. Tee ohjelma, joka kysyy käyttäjän nimeä. Sen jälkeen ohjelma tulostaa näytölle henkilökohtaisen tervehdyksen.
Jos käyttäjä antaa nimekseen Pekka, on tervehdys `Moi Pekka`.
2. Tee ohjelma, joka kysyy käyttäjän ja käyttäjän äidin nimen sekä iän.
Ohjelma laskee ja tulostaa heidän ikäeronsa muodossa `Pekka on 30 vuotta nuorempi kuin
hänen äitinsä Maija.`
3. Tee ohjelma, joka kysyy käyttäjältä nelikulmion molempien sivujen pituuden. Ohjelma laskee ja tulostaa nelikulmion pinta-alan.
4. Tee ohjelma, joka kysyy ympyrän säteen ja laskee sen perusteella ympyrän pinta-alan.
5. Tee ohjelma, joka kysyy käyttäjältä illallisen energiamäärän kilokaloreina.
Ohjelma tulostaa montako kilojoulea aterian energiasisältö on.
Tulosta muodossa `2000 kilokalorin illallinen vastaa 8368 kilojoulea`.

## 3. Valintarakenne (if)

1. Tee ohjelma, joka kysyy käyttäjältä kolme lukua. Lopuksi ohjelma tulostaa luvuista suurimman.
Huomaa, että ohjelman on toimittava oikein myös tilanteissa, joissa kaksi tai kolme luvuista on keskenään yhtä suuria.
2. Tee ohjelma, joka kysyy käyttäjältä kolme lukua. Lopuksi ohjelma tulostaa luvut suuruusjärjestyksessä pienimmästä
3. suurimpaan. Tämänkin ohjelman on toimittava oikein myös tilanteissa, joissa kaksi tai kolme luvuista on keskenään yhtä suuria.


## 4. Alkuehdollinen toistorakenne (while)

1. Kirjoita `while`-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
2. Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa.
3. Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja kunnes käyttäjän siihen asti syöttämien lukujen
summa on 10 tai korkeampi. Lopuksi ohjelma tulostaa syötettyjen lukujen summan.
4. Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin `Liian suuri arvaus`, `Liian pieni arvaus` tai `Oikein`.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
5. Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat
ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein
tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan `Tervetuloa`
ja jälkimmäisessä `Pääsy evätty`. (Oikea käyttäjätunnus on **python** ja salasana **rules**).
6. Toteutetaan algoritmi piin (π) likiarvon laskemiseksi. Oletetaan, että A on yksikköympyrä eli ympyrä,
jonka keskipiste on origossa ja jonka säde on yksi. Sen ympärille piirretään pienin mahdollinen neliö B siten,
että ympyrä A jää kokonaan neliön sisäpuolelle. Neliön nurkkapisteet ovat tällöin (-1,-1), (1,-1), (1,1) ja (-1,1).
Jos neliön sisälle arvotaan satunnaisesti suuri määrä pisteitä, osuu niistä myös ympyrän sisälle likimain niin suuri
osuus kuin ympyrän pinta-ala on neliön pinta-alasta eli πr^2/4, joka (koska ympyrän säde on yksi) sievenee
muotoon π/4. Tästä saadaan yksinkertainen menetelmä piin likiarvon laskemiseksi: Arvotaan neliön B sisälle
suuri määrä satunnaisissa kohdissa olevia pisteitä, esimerkiksi miljoona. Olkoon N tämä pisteiden kokonaismäärä.
Jokaisesta neliön B sisään arvotusta pisteestä testataan vuorollaan, jääkö se myös yksikköympyrän A sisälle.
Olkoon n ympyrän sisälle jäävien pisteiden kokonaismäärä. Nyt pätee n/N≈π/4, josta saadaan π≈4n/N. Kirjoita ohjelma,
joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä.
Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle. (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on helppoa testata
onko se yksikköympyrän A sisällä: riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)

## 5. Listarakenne ja läpikäyvä toistorakenne (for)

1. Tee ohjelma, joka kysyy neljän kaupungin nimet (käytä `for`-toistorakennetta nimien kysymiseen)
ja tallentaa ne listaan. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. 
2. Jatka edellistä ohjelmaa siten, että
a)	ohjelma kysyy poistettavan kaupungin nimen ja poistaa sen listasta. Ohjelma tulostaa lyhentyneen listan.
b)	ohjelma kysyy uuden kaupungin nimen ja lisää sen listan loppuun. Ohjelma tulostaa pidentyneen listan.
c)	ohjelma luo aluksi yhden sijasta kaksi neljän kaupungin listaa. Tämän jälkeen tarkoitus on yhdistää kaksi listaa yhdeksi jättilistaksi. Ohjelma yhdistää toisen nimilistan ensimmäiseen listaan ja tulosta yhdistetyn listan nimet.
3. Tee ohjelma, joka kysyy käyttäjältä kuinka monesta arvosanasta lasketaan keskiarvo.
Sen jälkeen ohjelma kysyy arvosanat. Lopuksi ohjelma tulostaa annetut arvosanat yksi kerrallaan allekkain
vastakkaisessa järjestyksessä kuin ne syötettiin ja ilmoittaa niiden keskiarvon.
4. Tee ohjelma, joka pyytää käyttäjältä kymmenen lukua. Lopuksi ohjelma tulostaa pienimmän ja suurimman annetuista
luvuista. Käytä `for`-toistorakennetta.

## 6. Funktio

1. Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
2. Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä
poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään
käyttäjältä ohjelman suorituksen alussa.
3. Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa
sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä
syöttää negatiivisen gallonamäärän.
4. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien
lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
5. Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen
sekä alkuperäisen että karsitun listan.
6. Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä
pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on
hyödynnettävä kirjoitettua funktiota.


## 7. Monikko, joukko ja sanakirja

1. Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
vuodenajan (`kevät`, `kesä`, `syksy`, `talvi`). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen
talvikuukausi.

2. Kirjoita ohjelma, joka kysyy käyttäjältä nimiä. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa,
joko tekstin `Uusi nimi` tai `Aiemmin syötetty nimi` sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee
syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.

3. Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai 
lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä
valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus
päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät
koodeja helposti selaimen avulla.)


## 8. Luokka, olio, alustaja

## 9. Assosiaatio

## 10. Periytyminen

## 11. Relaatiotietokannan käyttö

1. Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
2. Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi `FI`) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne. 
3. Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden
kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys `geopy`-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla
**View / Tool Windows / Python Packages**. Kirjoita hakukenttään `geopy` ja vie asennus loppuun.

## 12. Taustapalvelun rakentaminen