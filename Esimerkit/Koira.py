class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)
