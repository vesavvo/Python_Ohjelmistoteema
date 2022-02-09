from flask import Flask, request
import main

app = Flask(__name__)

# http://127.0.0.1:5000/pelaa?id=123&kohde=HEL
@app.route('/pelaa')
def etene():
    args = request.args
    id = args.get("id")
    kohde = args.get("kohde")

    tulos = main.uusi_siirto(id, kohde)

    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
