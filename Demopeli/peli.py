from pelaaja import Pelaaja
from kenttä import Kenttä


class Peli:
    def __init__(self):
        pass

# Alustus
nick = "Vesa"
alkusijainti = "HEL"

pelaaja = Pelaaja(nick)
sijainti = Kenttä(alkusijainti)
sijainti.dump()
