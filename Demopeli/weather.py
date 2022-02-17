import requests
import config

class Weather:

    def kelvin_to_celsius(self, kelvin):
        return int (kelvin - 273.15)

    def check_weather_goals(self, game):
        sql = "SELECT id, name, description, target, target_minvalue, target_maxvalue, target_text FROM Goal"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        for a in res:
            if a[3]=="TEMP":
                # temperature rule
                if self.temperature>=a[4] and self.temperature<=a[5]:
                    self.meets_goals.append(a[0])
            elif a[3]=="WEATHER":
                # weather type rule
                if self.type==a[6]:
                    self.meets_goals.append(a[0])
            elif a[3]=="WIND":
                # wind rule
                if self.wind_speed>=a[4] and self.wind_speed<=a[5]:
                    self.meets_goals.append(a[0])


        # here inserts to GoalReached table
        sql = "SELECT goalid FROM GoalReached WHERE gameid='" + game.id + "'"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        old_goals = []
        for a in res:
            old_goals.append(a[0])

        for a in self.meets_goals:
            if a in old_goals:
                # old goal
                pass
            else:
                # new goal
                sql = "INSERT INTO GoalReached VALUES ('" + game.id + "', '" + str(a)  + "')"
                print(sql)
                cur = config.conn.cursor()
                cur.execute(sql)
                #config.conn.commit()

        return


    def __init__(self, sijainti, game):
        apikey = "bda75ef0309aec2639f2d2b9f73d35ab"

        request = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                 str(sijainti.latitude) + "&lon=" + str(sijainti.longitude) + "&appid=" + apikey
        vastaus = requests.get(request).json()
        self.type = vastaus["weather"][0]["main"]
        self.temperature = self.kelvin_to_celsius(vastaus["main"]["temp"])
        self.humidity = vastaus["main"]["humidity"]
        self.wind_speed = vastaus["wind"]["speed"]

        self.meets_goals = []
        self.check_weather_goals(game)
