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
    lista.append(Airport("EFEJ"))
    lista.append(Airport("EFSE"))
    lista.append(Airport("EFKG"))
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

def fly(id, dest):

    game = Game(id)
    sijainti = Airport(dest)
    säätila = Weather(sijainti)
    game.updateLocation(sijainti)

    kohteet = find_close_airports(sijainti, max_xdist, max_ydist)

    json_data = make_json(game, sijainti, säätila, kohteet)

    return json_data

def new_game(nick, loc):
    peli = Game(0, nick, loc)

    return "DUMMY"
