from game import Game
from airport import Airport
from weather import Weather
import json, random, string

initial_money = 1500

def fly(id, dest):
    pass


def new_game(nick, loc):
    game = Game(0, nick, loc)
    json_data = fly(game.id, loc)

    return json_data
