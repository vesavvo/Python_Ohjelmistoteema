from game import Game
from airport import Airport
from weather import Weather
import json, random, string

initial_money = 1500

def make_json(peli, sijainti, kohteet):
    data = {
        "game" : peli,
        "location" : sijainti,
        "possible_destinations" : kohteet
    }
    print(data)
    json_data = json.dumps(data, default=lambda o: o.__dict__, indent=4)
    print(json_data)
    return json_data

def fly(id, dest):

    game = Game(id)
    sijainti = Airport(dest)
    sijainti.getWeather()
    game.updateLocation(sijainti)

    kohteet = sijainti.find_nearby_airports()

    json_data = make_json(game, sijainti, kohteet)

    return json_data

def new_game(nick, loc):
    game = Game(0, nick, loc)
    json_data = fly(game.id, loc)

    return json_data
