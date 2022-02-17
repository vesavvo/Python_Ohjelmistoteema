import random
import config
from weather import Weather
from geopy import distance

class Airport:
    def __init__(self, ident, active=False):
        self.ident = ident
        self.active = active

        # find airport from DB
        sql = "SELECT ident, name, latitude_deg, longitude_deg FROM Airport WHERE ident='" + ident + "'"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) == 1:
            # game found
            self.ident = res[0][0]
            self.name = res[0][1]
            self.latitude = float(res[0][2])
            self.longitude = float(res[0][3])

    def find_nearby_airports(self):
        #print("Testing geopy...")
        #self.distanceTo(1, 2)
        lista = []
        sql = "SELECT ident FROM Airport WHERE latitude_deg BETWEEN "
        sql += str(self.latitude-config.max_lat_dist) + " AND " + str(self.latitude+config.max_lat_dist)
        sql += " AND longitude_deg BETWEEN "
        sql += str(self.longitude-config.max_lon_dist) + " AND " + str(self.longitude+config.max_lon_dist)
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        for r in res:
            if r[0]!=self.ident:
                nearby_apt = Airport(r[0])
                nearby_apt.distance = self.distanceTo(nearby_apt)
                if nearby_apt.distance<=config.max_distance:
                    lista.append(nearby_apt)
                    nearby_apt.co2_consumption = self.co2_consumption(nearby_apt.distance)
        return lista


    def fetchWeather(self, game):
        self.weather=Weather(self, game)
        return

    def distanceTo(self, target):

        coords_1 = (self.latitude, self.longitude)
        coords_2 = (target.latitude, target.longitude)
        dist = distance.distance(coords_1, coords_2).km
        return int(dist)

    def co2_consumption(self, km):
        consumption = config.co2_per_flight + km*config.co2_per_km
        return consumption




