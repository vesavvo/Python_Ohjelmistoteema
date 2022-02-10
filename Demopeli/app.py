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

# http://127.0.0.1:5000/siirto?id=123&kohde=HEL
@app.route('/siirto')
def etene():
    args = request.args
    id = args.get("id")
    kohde = args.get("kohde")

    tulos = main.siirry(id, kohde)

    return tulos

# http://127.0.0.1:5000/uusi?nick=Vesa&kohde=RVN
@app.route('/uusi')
def uusi():
    args = request.args
    nick = args.get("nick")
    kohde = args.get("kohde")
    tulos = main.uusipeli(conn, nick, kohde)

    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
