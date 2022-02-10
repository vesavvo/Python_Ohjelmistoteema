from flask import Flask, request
import mysql.connector
import main

app = Flask(__name__)

# Tietokantayhteys
conn = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lento',
         user='lentopassi',
         password='piLo_t5AD'
         )

# http://127.0.0.1:5000/flyto?game=123&dest=HEL
@app.route('/flyto')
def fly():
    args = request.args
    id = args.get("game")
    dest = args.get("dest")

    reply = main.fly(conn, id, dest)

    return reply

# http://127.0.0.1:5000/newgame?nick=Vesa&loc=RVN
@app.route('/newgame')
def newgame():
    args = request.args
    nick = args.get("nick")
    loc = args.get("loc")
    reply = main.new_game(conn, nick, loc)

    return reply


# http://127.0.0.1:5000/newplayer?nick=Vesa
@app.route('/newplayer')
def newplayer():
    # DUMMY
    return "TBD"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
