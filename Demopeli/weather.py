import requests

class Weather:

    def kelvin_to_celsius(self, kelvin):
        return int (kelvin - 273.15)

    def __init__(self, sijainti):
        apikey = "bda75ef0309aec2639f2d2b9f73d35ab"

        request = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                 str(sijainti.latitude) + "&lon=" + str(sijainti.longitude) + "&appid=" + apikey
        vastaus = requests.get(request).json()
        self.type = vastaus["weather"][0]["main"]
        self.temperature = self.kelvin_to_celsius(vastaus["main"]["temp"])
        self.humidity = vastaus["main"]["humidity"]
        self.wind_speed = vastaus["wind"]["speed"]
