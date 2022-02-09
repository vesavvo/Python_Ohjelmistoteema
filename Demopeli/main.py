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

def tee_datapaketti():
    kohteet = []
    for k in kentät_tarjolla:
        kohteet.append((k.__dict__))
    data = {
        "peli" : peli.__dict__,
        "sijainti" : sijainti.__dict__,
        "säätila": säätila.__dict__,
        "tarjolla" : kohteet
    }

    json_data = json.dumps(data)
    return json_data

# Alusta peli
nick = "Vesa"
alkusijainti = "HEL"
raha = 1500
max_xdist = 1
max_ydist = 1

peli = Peli(nick, raha)
sijainti = Kenttä(alkusijainti)
säätila = Säätila(sijainti)

kentät_tarjolla = etsi_lähikentät(sijainti, max_xdist, max_ydist)

json_data = tee_datapaketti()
print(json_data)
