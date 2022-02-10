from game import Game
from airport import Airport
from weather import Weather
import json, random, string

initial_money = 1500

def fly(id, dest):

    game = Game(id)
    game.set_location(Airport(dest))
    game.location.getWeather()
    game.location.find_nearby_airports()
    json_data = json.dumps(game, default=lambda o: o.__dict__, indent=4)

    return json_data

def new_game(nick, loc):
    game = Game(0, nick, loc)
    json_data = fly(game.id, loc)

    return json_data
