from game import Game
from airport import Airport
from weather import Weather
import json, random, string

max_xdist = 1
max_ydist = 1
initial_money = 1500

def find_close_airports(sijainti, max_xdist, max_ydist):
    lista = []
    # DUMMY - korvataan tietokantahaulla
    lista.append(Airport("TKU"))
    lista.append(Airport("TMP"))
    lista.append(Airport("MIK"))
    return lista

def make_json(peli, sijainti, säätila, kohteet):
    kohdelista = []
    for k in kohteet:
        kohdelista.append((k.__dict__))
    data = {
        "game" : peli.__dict__,
        "location" : sijainti.__dict__,
        "weather": säätila.__dict__,
        "possible_destinations" : kohdelista
    }

    json_data = json.dumps(data)
    return json_data

def fly(conn, id, kohde):

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

        peli = Game(id, raha)
        sijainti = Airport(kohde)
        säätila = Weather(sijainti)

        kohteet = find_close_airports(sijainti, max_xdist, max_ydist)

        json_data = make_json(peli, sijainti, säätila, kohteet)
    else:
        data = {"Success:" : "false"}
        json_data = json.dumps(data)
    return json_data

def new_game(conn, starting_point):

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
