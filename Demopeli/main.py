from game import Game
from airport import Airport
from weather import Weather
import json, random, string

initial_money = 1500

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

    kohteet = sijainti.find_nearby_airports()

    json_data = make_json(game, sijainti, säätila, kohteet)

    return json_data

def new_game(nick, loc):
    game = Game(0, nick, loc)
    json_data = fly(game.id, loc)

    return json_data
