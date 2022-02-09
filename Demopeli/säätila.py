import requests

class Säätila:

    def __init__(self, sijainti):
        apikey = "bda75ef0309aec2639f2d2b9f73d35ab"

        pyyntö = "https://api.openweathermap.org/data/2.5/weather?lat=" +\
                  str(sijainti.xkoord) + "&lon=" + str(sijainti.ykoord) + "&appid=" + apikey
        vastaus = requests.get(pyyntö).json()
        self.tyyppi = vastaus["weather"][0]["main"]
        self.lämpötila = vastaus["main"]["temp"]
        self.kosteus = vastaus["main"]["humidity"]
        self.tuuli = vastaus["wind"]["speed"]
