from peli import Peli
from kenttä import Kenttä
from säätila import Säätila
import json, random, string

max_xdist = 1
max_ydist = 1
initial_money = 1500

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

def siirry(conn, id, kohde):
    # DUMMY

    # find game from DB
    sql = "SELECT id, money, location FROM Peli WHERE id='" + id + "'"
    print (sql)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) == 1:
        id = res[0][0]
        raha = res[0][1]
        old_loc = res[0][2]

        peli = Peli(id, raha)
        sijainti = Kenttä(kohde)
        säätila = Säätila(sijainti)

        kohteet = etsi_lähikentät(sijainti, max_xdist, max_ydist)

        json_data = tee_datapaketti(peli, sijainti, säätila, kohteet)
    else:
        data = {"Success:" : "false"}
        json_data = json.dumps(data)
    return json_data

def uusipeli(conn, starting_point):

    # Create new game id
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    game_id = ''.join(random.choice(letters) for i in range(20))

    # Insert new game into DB
    sql = "INSERT INTO Peli VALUES ('" + game_id + "', " + str(initial_money) + ", '" + starting_point + "')"
    print (sql)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

    # Move plane to starting point

    return "DUMMY"
