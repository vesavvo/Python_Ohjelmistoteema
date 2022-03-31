# Monikko, joukko ja sanakirja

Aiemmin käsiteltiin Python-kielen listarakennetta, joka on kielen tarjoamista tietorakenteista yleisimmin käytetty.
Python-kieli tarjoaa myös kolme muuta sisäänrakennettua tietorakennetta, joista kullakin on oma käyttöalueensa.

Tässä moduulissa opit käyttämään näitä kolmea Pythonin tietorakennetta: monikkoa, joukkoa ja sanakirjaa.

## Monikko

Monikko (*tuple*) muistuttaa Pythonin listarakennetta siinä mielessä, että siinä voidaan esittää järjestetty
jono alkioita. Toisin kuin lista, monikko on kuitenkin muuttumaton: siihen ei voi lisätä alkioita eikä siitä
voi poistaa alkioita monikon luonnin jälkeen.

Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen: tiedetään,
että muutoksille ei ole tarvetta ohjelman suorituksen aikana. Monikon käytön edut liittyvät muistinhallintaan:
monikolle voidaan varata sitä luotaessa kiinteä muistialue, ja yksittäisen alkion osoite keskusmuistissa voidaan
laskea suoraan tietorakenteen alkuosoitteen ja indeksin avulla. Listan tapauksessa tämä ei ole mahdollista, vaan
haettaessa alkiota indeksin perusteella ajoympäristö joutuu yleensä iteroimaan alkiot lävitse. Ero näkyy siten,
että alkion haku indeksin perusteella on monikon tapauksessa nopeampaa. Käytännössä ero on huomaamaton silloin,
kun tietorakenne on pieni.

Katsotaan esimerkkiä monikon käytöstä. Seuraava ohjelma luo monikon viikonpäivien nimistä. Ohjelma kysyy käyttäjältä
viikonpäivän järjestysnumeron ja tulostaa sitä vastaavan viikonpäivän nimen. Huomaa, että monikon indeksointi
alkaa nollasta samoin kuin listan:

```python
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
```

Ohjelma toimii ajettaessa näin:

```monospace
Anna viikonpäivän järjestysnumero (1-7): 3
3. viikonpäivä on keskiviikko.
```

## Joukko

Joukko (*set*) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä. Koska joukon alkioille
ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä. Toisin kuin listassa tai monikossa, sama
alkio voi esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.

Tarkastellaan seuraavaa esimerkkiä:
```python
pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p)
```

Ohjelman tuottaa seuraavan tulosteen:
```monospace
{'Shakki', 'Cluedo', 'Monopoli'}
{'Shakki', 'Dominion', 'Cluedo', 'Monopoli'}
{'Dominion', 'Cluedo', 'Monopoli'}
{'Dominion', 'Cluedo', 'Monopoli'}
Dominion
Cluedo
Monopoli
```

Aluksi luodaan joukko, jossa on kolme peliä: Monopoli, Shakki ja Cluedo. Tämän jälkeen pelit sisältävä joukko tulostetaan.
Havaitaan, että pelit ovat tulosteessa eri järjestyksessä kuin missä ne joukkoa luotaessa kirjoitettiin.
Tulostuslause konkretisoi sen, että joukon alkioiden järjestys ei ole määritelty: ohjelmoijan on varauduttava
siihen, että joukkoa tulostettaessa alkiot voivat näkyä missä järjestyksessä tahansa. Esitysjärjestys
määräytyy ajoympäristön sisäisen tallennusratkaisun mukaisesti, ja sen on
sallittua vaihdella jopa saman ohjelman eri suorituskerroilla.

Seuraavaksi kolmealkioiseen pelien joukkoon liitetään neljäs jäsen, Dominion. Joukkoon liittäminen tehdään `add`-operaation
avulla. Tulostuslause paljastaa jälleen, että alkioiden
näkyvä järjestys voi olla mikä tahansa. 

Tämän jälkeen joukosta poistetaan yksi alkio, Shakki. Tähän käytetään `remove`-operaatiota.

Jäljellä on Dominion, Cluedo ja Monopoli. Seuraavaksi yritetään lisätä joukkoon uusi alkio, joka on sama
kuin joukossa ennestään oleva alkio: Cluedo. Lisäämiseen käytetty `add`-metodi ei tuota virheilmoitusta,
mutta tulosteesta nähdään, että samaa peliä ei lisätty toista kertaa. Tämä on joukon keskeinen ominaisuus:
sama alkio voi esiintyä vain kertaalleen.

Lopuksi joukon alkiot iteroidaan eli käydään läpi yksi kerrallaan. Tämä tapahtuu samanlaisella `for/in`-rakenteella
kuin listojen tapauksessa. Tuloksena oleva järjestys voi jälleen olla ohjelmoijan näkökulmasta mikä tahansa.

Edellisessä esimerkissä kaikki joukon alkiot olivat merkkijonoja, joten ne olivat keskenään saman tyyppisiä.
Mainittakoon, että samantyyppisyyden vaatimusta ei ole. On siis sallittua luoda joukko, jonka yksi alkio on 
kokonaisluku, toinen alkio on merkkijono ja kolmas vaikkapa lista.

## Sanakirja

Sanakirja (*dictionary*) on Pythonin käytetyimpiä tietorakenteita.

Sanakirjaan voidaan tallentaa avain-arvopareja. Avain on ikään kuin kahva, josta vetämällä
oikea sanakirjan tietue löytyy, jotta sen arvon päästään käsiksi.

Sanakirja-tietorakenteesta käytetään toisinaan nimityksiä assosiatiivinen taulukko ja hajautusrakenne.

Seuraava kuva havainnollistaa sanakirjarakennetta:

![Sanakirjarakenne](img/sanakirja.png)

Sanakirja nimeltä `numerot` sisältää viiden henkilön puhelinnumerot. Henkilön nimi toimii avaimena: kun tiedät nimen,
saat arvon - eli puhelinnumeron - selville.

Laaditaan vastaava rakenne Python-kielellä. Luodaan aluksi kolmen henkilön tiedot sisältävä sanakirja.
Sitten lisätään kaksi henkilöä erikseen sanakirjan luonnin jälkeen ja tulostetaan sanakirja,
jossa on tässä vaiheessa viiden henkilön nimet ja puhelinnumerot.
Lopuksi kysytään käyttäjältä henkilön nimi ja tulostetaan saatua nimeä vastaava puhelinnumero, jos annettu
nimi löytyy sanakirjan avainten joukosta:

```python
numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")
```

Ohjelma tuottaa seuraavan tulosteen:
```monospace
{'Viivi': '050-1234567', 'Ahmed': '040-1112223', 'Pekka': '050-7654321', 'Olga': '050-1011012', 'Mary': '0401-2132139'}
Anna nimi: Olga
Henkilön Olga puhelinnumero on 050-1011012.
```

Kun sanakirja alustetaan arvot luettelemalla, annetaan kukin avain-arvopari seuraavasti: `avain : arvo`. Peräkkäiset
avain-arvoparit erotellaan toisistaan pilkulla.

Kun olemassa olevaan sanakirjaan lisätään arvo, käytetään notaatiota `sanakirja[avain] = arvo`, missä `sanakirja` on
sanakirjaan viittaavan muuttujan nimi. Vastaavasti sanakirjassa olevan alkion arvo saadaan haettua
kirjoittamalla `sanakirja[avain]`.

Kun sanakirja läpikäydään `for/in`-rakennetta käyttäen, saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa
esiintyvän avaimen.

Entä ovatko sanakirjan alkiot - eli avain-arvoparit - järjestettyjä? Tämän osalta tilanne riippuu Pythonin versiosta:
versiosta 3.7 lukien alkiot ovat järjestettyjä, eli ajoympäristö takaa, että sanakirjan iterointijärjestys on
sama kuin järjestys, jossa alkiot sanakirjaan syötetiin. Vanhemmissa Python-versioissa tätä ei taata.

