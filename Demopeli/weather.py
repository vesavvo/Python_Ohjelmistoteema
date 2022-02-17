import requests
import config

class Weather:

    def kelvin_to_celsius(self, kelvin):
        return int (kelvin - 273.15)

    def check_weather_goals(self, game):

        for goal in game.goals:
            if goal.target=="TEMP":
                # temperature rule
                if self.temp>=goal.target_minvalue and self.temp<=goal.target_maxvalue:
                    self.meets_goals.append(goal.goalid)
            elif goal.target=="WEATHER":
                # weather type rule
                if self.main==goal.target_text:
                    self.meets_goals.append(goal.goalid)
            elif goal.target=="WIND":
                # wind rule
                if self.wind["speed"]>=goal.target_minvalue and self.wind["speed"]<=goal.target_maxvalue:
                    self.meets_goals.append(goal.goalid)

        for goal in game.goals:
            if goal.reached==False and goal.goalid in self.meets_goals:
                # new goal
                sql = "INSERT INTO GoalReached VALUES ('" + game.id + "', '" + str(goal.goalid)  + "')"
                print(sql)
                cur = config.conn.cursor()
                cur.execute(sql)
                goal.reached = True
        return


    def __init__(self, sijainti, game):
        apikey = "bda75ef0309aec2639f2d2b9f73d35ab"

        request = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                 str(sijainti.latitude) + "&lon=" + str(sijainti.longitude) + "&appid=" + apikey
        vastaus = requests.get(request).json()
        self.main = vastaus["weather"][0]["main"]
        self.description = vastaus["weather"][0]["description"]
        self.icon = "https://openweathermap.org/img/wn/" + vastaus["weather"][0]["icon"] + ".png"
        self.temp = self.kelvin_to_celsius(vastaus["main"]["temp"])
        self.humidity = vastaus["main"]["humidity"]
        self.wind = {
            "speed": vastaus["wind"]["speed"],
            "deg": vastaus["wind"]["deg"]
        }

        self.meets_goals = []
        self.check_weather_goals(game)
