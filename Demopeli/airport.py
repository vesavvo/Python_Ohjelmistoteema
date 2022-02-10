import random
import config

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



