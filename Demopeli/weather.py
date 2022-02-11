import requests
import config

class Weather:

    def kelvin_to_celsius(self, kelvin):
        return int (kelvin - 273.15)

    def check_weather_goals(self):
        sql = "SELECT id, name, description, target, target_minvalue, target_maxvalue, target_text FROM Goal"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        for a in res:
            if a[3]=="TEMP":
                # temperature rule
                if (self.temperature>=a[4] and self.temperature<=a[5]):
                    print ("Rule " + a[1] + " satisfied.")
            elif a[3]=="WEATHER":
                # weather type rule
                pass
        return


    def __init__(self, sijainti):
        apikey = "bda75ef0309aec2639f2d2b9f73d35ab"

        request = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                 str(sijainti.latitude) + "&lon=" + str(sijainti.longitude) + "&appid=" + apikey
        vastaus = requests.get(request).json()
        self.type = vastaus["weather"][0]["main"]
        self.temperature = self.kelvin_to_celsius(vastaus["main"]["temp"])
        self.humidity = vastaus["main"]["humidity"]
        self.wind_speed = vastaus["wind"]["speed"]

        self.check_weather_goals()
