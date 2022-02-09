from peli import Peli
from kenttä import Kenttä
from säätila import Säätila
import json

def etsi_lähikentät(sijainti, max_xdist, max_ydist):
    lista = []
    # DUMMY - korvataan tietokantahaulla
    lista.append(Kenttä("TKU"))
    lista.append(Kenttä("TMP"))
    lista.append(Kenttä("MIK"))
    return lista

def tee_datapaketti(peli, sijainti, säätila, kohteet):
    kohdelista = []
    for k in kohteet:
        kohdelista.append((k.__dict__))
    data = {
        "peli" : peli.__dict__,
        "sijainti" : sijainti.__dict__,
        "säätila": säätila.__dict__,
        "tarjolla" : kohdelista
    }

    json_data = json.dumps(data)
    return json_data

def uusi_siirto(id, kohde):
    # Alusta peli
    nick = "Vesa"
    raha = 1500
    max_xdist = 1
    max_ydist = 1

    peli = Peli(nick, raha)
    sijainti = Kenttä(kohde)
    säätila = Säätila(sijainti)

    kohteet = etsi_lähikentät(sijainti, max_xdist, max_ydist)

    json_data = tee_datapaketti(peli, sijainti, säätila, kohteet)
    return json_data


    #return "Tämähän toimii!"


