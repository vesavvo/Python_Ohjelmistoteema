import random

class Airport:
    def __init__(self, id):
        self.id = id

        # Helsingin koordinaatit: 60.317222, 24.963333
        # DUMMY
        self.xcoord = 60.317222 - 10 + random.random() * 20
        self.ycoord = 24.963333 - 10 + random.random() * 20
        self.name = "Kaupunki_" + self.id

    def dump(self):
        print(self.id, self.xcoord, self.ycoord, self.name)
