# Harjoitustehtäviä

Jokaiseen moduuliin liittyvistä tehtävistä saa yhteensä 6 pistettä. Yhden tehtävän pistearvo saadaan jakamalla se
tehtävien lukumäärällä.

## 1. Ensimmäinen ohjelma ja versionhallinnan käyttöönotto

1. Asenna PyCharm-kehitin. Kirjoita ohjelma, joka tervehtii sinua omalla nimelläsi.
Jos nimesi olisi Viivi Virta, ohjelma tulostaisi: `Hei, Viivi Virta!`
2. Luo itsellesi GitHub-käyttäjätili ja tee repositorio Python-harjoitustehtäviä varten. Määritä  PyCharm käyttämään
repositoriota harjoitustehtäväprojektin tietojen tallentamiseen. Varmista, että voit hakea, sitouttaa ja työntää
tekemiäsi muutoksia (*pull*, *commit*, *push*).

## 2. Muuttujat ja vuorovaikutteiset ohjelmat

1. Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi. Esimerkkejä:
   - Jos syötät nimeksesi Viivi, ohjelma tervehtii sinua sanoin `Terve, Viivi!`
   - Jos syötät nimeksesi Ahmed, ohjelma tervehtii sinua sanoin `Terve, Ahmed!`

2. Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

3. Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

4. Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

5. Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
   - Yksi leiviskä on 20 naulaa.
   - Yksi naula on 32 luotia.
   - Yksi luoti on 13,3 grammaa.

   Esimerkki ohjelman toiminnasta:
```monospace
Anna leiviskät.
3

Anna naulat.
9

Anna luodit.
13.5

Massa nykymittojen mukaan:
29 kilogrammaa ja 545.95 grammaa. 
```

6. Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
   - kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
   - nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

Vihje: tutustu random.randint()-funktion käyttöön.

## 3. Valintarakenne (if)

1. Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.

2. Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
   - LUX on parvekkeellinen hytti yläkannella.
   - A on ikkunallinen hytti autokannen yläpuolella.
   - B on ikkunaton hytti autokannen yläpuolella.
   - C on ikkunaton hytti autokannen alapuolella.

   Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa `Virheellinen hyttiluokka`.

3. Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
   - Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
   - Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

4. Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.


## 4. Alkuehdollinen toistorakenne (while)

1. Kirjoita `while`-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
2. Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa.
`1 tuuma = 2,54 cm`
3. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
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


1. Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä `for`-toistorakennetta.

2. Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje:
listan alkioiden lajittelujärjestyksen voi kääntää antamalla `sort`-metodille argumentiksi `reverse=True`.

4. Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
   - Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
   - Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

5. Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä `for`-toistorakennetta nimien kysymiseen)
ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. käytä `for`-toistorakennetta nimien kysymiseen ja `for/in` toistorakennetta niiden läpikäymiseen.




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
   - Yksi gallona on 3,785 litraa.
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

2. Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä
syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
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

## 8. Relaatiotietokannan käyttö

>Huom! Joillain käyttäjillä on ilmennyt yllättäviä haasteita uusimman MySQL-ajuriversion 8.0.30 kanssa.
>Jos törmäät virheilmoitukseen `mysql.connector.errors.ProgrammingError: Character set 'utf8' unsupported`,
>vaihda toiseksi uusimpaan ajuriversioon 8.0.29: Valitse PyCharmissa View/Tool Windows/Python Packages.
>Etsi hakutoiminnolla pakkaus mysql-connector-python. Poista version 8.0.30 asennus painamalla oikeassa laidassa olevaa kolmea pistettä ja valitsemalla Delete. Vaihda ajuriversioksi 8.0.29 Latest-valinnan tilalle ja asenna napsauttamalla Install.


1. Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
2. Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi `FI`) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne. 
3. Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden
kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys `geopy`-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla
**View / Tool Windows / Python Packages**. Kirjoita hakukenttään `geopy` ja vie asennus loppuun.




## 9. Luokka, olio, alustaja

1. Kirjoita `Auto`-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
ja kuljettu matka. Kirjoita
luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus
142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

2. Jatka ohjelmaa kirjoittamalla `Auto`-luokkaan `kiihdytä`-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion `nopeus`-ominaisuuden arvoa. 
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

3. Laajenna ohjelmaa siten, että mukana on `kulje`-metodi, joka saa
   parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: `auto`-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu
`auto.kulje(1.5)` kasvattaa kuljetun matkan lukemaan 2090 km.

5. Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
   - Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla `kiihdytä`-metodia.
   - Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla `kulje`-metodia.

   Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet
selkeäksi taulukoksi muotoiltuna.


## 10. Assosiaatio

1. Kirjoita `Hissi`-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
`siirry_kerrokseen`, `kerros_ylös` ja `kerros_alas`. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle
hissille `h` esimerkiksi metodikutsun `h.siirry_kerrokseen(5)`, metodi kutsuu joko `kerros_ylös`- tai `kerros_alas`-metodia niin monta kertaa, että 
hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
sen jälkeen takaisin alimpaan kerrokseen.

2. Jatka edellisen tehtävän ohjelmaa siten, että teet `Talo`-luokan. Talon alustajaparametreina annetaan alimman ja 
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien
lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi `aja_hissiä`, joka saa parametreinaan hissin numeron
ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

3. Jatka edellisen tehtävän ohjelmaa siten, että `Talo`-luokassa on parametriton
metodi `palohälytys`, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee
palohälytys.

5. Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita `Kilpailu`-luokka, jolla on ominaisuuksina
kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan
nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
   - `tunti_kuluu`, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
   arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle `kulje`-metodia.
   - `tulosta_tilanne`, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
   - `kilpailu_ohi`, joka palauttaa `True`, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän.

   Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
   Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi
   kilpailun etenemistä kutsumalla toistorakenteessa `tunti_kuluu`-metodia, jonka jälkeen aina tarkistetaan `kilpailu_ohi`-metodin
avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan `tulosta tilanne`-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.


## 11. Periytyminen

1. Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi `tulosta_tiedot`, joka tudostaa kyseisen julkaisun kaikki tiedot. 
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta
molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

2. Kirjoita aiemmin laatimallesi `Auto`-luokalle aliluokat `Sähköauto` ja `Polttomoottoriauto`. Sähköautolla on ominaisuutena
akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille
alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu
yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot
yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin
autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.


## 12. Ulkoisen rajapinnan käyttö

1. Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää
rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
2. Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy
käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (*API key*). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

## 13. Taustapalvelun ja rajapinnan rakentaminen

1. Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa
tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
`http://127.0.0.1:5000/alkuluku/31`. Vastauksen on oltava muodossa:
`{"Number":31, "isPrime":true}`.

2. Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
`http://127.0.0.1:5000/kenttä/EFHK`. Vastauksen on oltava muodossa:
`{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}`.
 
