class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self):
        self.koirat = []

    def koiraSisään(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + " kirjattu sisään")
        return

    def koiraUlos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + " kirjattu ulos")
        return

    def tervehdiKoiria(self):
        for koira in self.koirat:
            koira.hauku(1)

# Pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koiraSisään(koira1)
hoitola.koiraSisään(koira2)
hoitola.tervehdiKoiria()

hoitola.koiraUlos(koira1)
hoitola.tervehdiKoiria()