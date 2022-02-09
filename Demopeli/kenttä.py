import random

class Kenttä:
    def __init__(self, iata_koodi):
        self.iata_koodi = iata_koodi

        # Helsingin koordinaatit: 60.317222, 24.963333
        # DUMMY
        self.xkoord = 60.317222-10+random.random()*20
        self.ykoord = 24.963333-10*random.random()*20
        self.nimi = "Kaupunki_" + str(random.randint(1,10000))

    def dump(self):
        print(self.iata_koodi, self.xkoord, self.ykoord, self.nimi)
