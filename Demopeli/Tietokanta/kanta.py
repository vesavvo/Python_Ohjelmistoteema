import mysql.connector

class Työntekijä:
    def __init__(self, numero, sukunimi, etunimi, palkka):
        self.numero = numero
        self.sukunimi = sukunimi
        self.etunimi = etunimi
        self.palkka = palkka

    def esittäydy(self):
        print(f"Päivää! Olen {self.etunimi} {self.sukunimi}. Palkkani on {self.palkka} euroa kuussa.")



# Tietokantametodit
def haeTyöntekijätSukunimellä(sukunimi):
    sql = "SELECT Numero, Sukunimi, Etunimi, Palkka FROM Työntekijä"
    sql += " WHERE Sukunimi='" + sukunimi + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    työntekijät = []
    if kursori.rowcount >0 :
        for rivi in tulos:
            työntekijät.append(Työntekijä(rivi[0], rivi[1], rivi[2], rivi[3]))
    return työntekijät

def päivitäPalkkaa(numero, uusiPalkka):
    sql = "UPDATE Työntekijä SET Palkka=" + str(uusiPalkka) + " WHERE Numero=" + str(numero)
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    if kursori.rowcount==1:
        print("Palkka päivitetty")

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='root',
         password='pelle',
         autocommit=True
         )

# sukunimi = input("Anna sukunimi: ")
# työntekijät = haeTyöntekijätSukunimellä(sukunimi)
# for t in työntekijät:
#     t.esittäydy()

numero = int(input("Anna numero: "))
uusiPalkka = float(input("Anna uusi palkka: "))
päivitäPalkkaa(numero, uusiPalkka)


