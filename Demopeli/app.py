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

# http://127.0.0.1:5000/fly?game=123&dest=HEL
@app.route('/fly')
def fly():
    args = request.args
    id = args.get("game")
    dest = args.get("dest")

    reply = main.fly(conn, id, dest)

    return reply

# http://127.0.0.1:5000/new?dest=RVN
@app.route('/new')
def new():
    args = request.args
    dest = args.get("dest")
    reply = main.new_game(conn, dest)

    return reply

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
