import random
import config
from weather import Weather

class Airport:
    def __init__(self, ident):
        self.ident = ident

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
        lista = []
        # DUMMY - korvataan tietokantahaulla
        #lista.append(Airport("EFEJ"))
        #lista.append(Airport("EFSE"))
        #lista.append(Airport("EFKG"))

        sql = "SELECT ident FROM Airport WHERE latitude_deg BETWEEN "
        sql += str(self.latitude-config.max_lat_dist) + " AND " + str(self.latitude+config.max_lat_dist)
        sql += " AND longitude_deg BETWEEN "
        sql += str(self.longitude-config.max_lon_dist) + " AND " + str(self.longitude+config.max_lon_dist)
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        for r in res:
            lista.append(Airport(r[0]))

        return lista

    def getWeather(self):
        self.weather=Weather(self)

