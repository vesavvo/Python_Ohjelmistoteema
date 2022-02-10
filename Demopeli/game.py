import string, random
from airport import Airport
import config

class Game:

    def __init__(self, id, player=None, loc=None):

        initial_money = 1500

        if id==0:
            # new game
            # Create new game id
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            self.id = ''.join(random.choice(letters) for i in range(20))
            self.money = initial_money
            self.location = Airport(loc)
            self.player = player

            # Insert new game into DB
            sql = "INSERT INTO Game VALUES ('" + self.id + "', " + str(initial_money) + ", '" + self.location.ident + "', '" + player + "')"
            print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)
            config.conn.commit()

        else:
            # find game from DB
            sql = "SELECT id, money, location, player FROM Game WHERE id='" + id + "'"
            print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            if len(res) == 1:
                # game found
                self.id = res[0][0]
                self.money = res[0][1]
                self.location = Airport(res[0][2])
                self.player = res[0][3]


    def set_location(self, sijainti):
        self.location = sijainti
        sql = "UPDATE Game SET location='" + sijainti.ident + "' WHERE id='" + self.id + "'"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        config.conn.commit()
        #self.loc = sijainti.ident
