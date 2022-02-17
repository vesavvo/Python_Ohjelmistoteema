from flask import Flask, request
import mysql.connector
import config
from game import Game
from airport import Airport
import json

app = Flask(__name__)

# Tietokantayhteys
config.conn = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lento',
         user='lentopassi',
         password='piLo_t5AD',
         autocommit=True
         )

def fly(id, dest, player=None):
    if id==0:
        game = Game(0, dest, player)
    else:
        game = Game(id)
    game.set_location(Airport(dest))
    game.location.fetchWeather(game)
    game.location.find_nearby_airports()
#    game.fetch_goal_info()
    json_data = json.dumps(game, default=lambda o: o.__dict__, indent=4)
    return json_data


# http://127.0.0.1:5000/flyto?game=123&dest=EFHK
@app.route('/flyto')
def flyto():
    args = request.args
    id = args.get("game")
    dest = args.get("dest")
    json_data = fly(id, dest)
    print("*** Called flyto endpoint ***")
    return json_data


# http://127.0.0.1:5000/newgame?player=Vesa&loc=EFHK
@app.route('/newgame')
def newgame():
    args = request.args
    player = args.get("player")
    dest = args.get("loc")
    #game = Game(0, player, loc)
    json_data = fly(0, dest, player=player)
    return json_data

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
