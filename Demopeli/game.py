import string, random
from airport import Airport
import config

class Game:

    def __init__(self, id, player=None, loc=None):

        if id==0:
            # new game
            # Create new game id
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            self.id = ''.join(random.choice(letters) for i in range(20))
            self.footprint = config.initial_footprint
            self.location = Airport(loc)
            self.player = player
            # Insert new game into DB
            sql = "INSERT INTO Game VALUES ('" + self.id + "', " + str(config.initial_footprint) + ", '" + self.location.ident + "', '" + player + "')"
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
                self.footprint = res[0][1]
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


    def fetch_goal_info(self):
        self.goals = []

        #sql = "SELECT goal.id, goal.name, goal.description, game.id "
        #sql += "FROM Goal LEFT JOIN GoalReached ON Goal.id = GoalReached.goalid LEFT JOIN Game "
        #sql += "ON GoalReached.gameid = Game.id WHERE Game.id = '" + self.id + "' OR Game.id IS NULL"

        sql = "SELECT * FROM (SELECT Goal.id, Goal.name, Goal.description, GoalReached.gameid FROM "
        sql += "Goal INNER JOIN GoalReached ON Goal.id = GoalReached.goalid "
        sql += "WHERE GoalReached.gameid = '" + self.id + "' "
        sql += "UNION SELECT Goal.id, Goal.name, Goal.description, NULL FROM Goal WHERE Goal.id NOT IN ("
        sql += "SELECT Goal.id FROM Goal INNER JOIN GoalReached ON Goal.id = GoalReached.goalid "
        sql += "WHERE GoalReached.gameid = '" + self.id + "')) AS t ORDER BY t.id;"

        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        for a in res:
            if a[3]==self.id:
                is_reached = True
            else:
                is_reached = False
            goal = {
                "goalid" : a[0],
                "name" : a[1],
                "description": a[2],
                "reached": is_reached
            }
            self.goals.append(goal)
        return
