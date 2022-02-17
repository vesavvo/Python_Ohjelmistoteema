import string, random
from airport import Airport
from goal import Goal
import config

class Game:

    def __init__(self, id, loc=None, player=None):

        if id==0:
            print("Id, loc, player:")
            print (id)
            print(loc)
            print(player)

            # new game
            # Create new game id
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            self.id = ''.join(random.choice(letters) for i in range(20))
            self.footprint = config.initial_footprint
            self.location = Airport(loc)
            self.player = player
            # Insert new game into DB
            sql = "INSERT INTO Game VALUES ('" + self.id + "', " + str(config.initial_footprint) + ", '" + loc + "', '" + player + "')"
            print(sql)
            cur = config.conn.cursor()
            cur.execute(sql)
            #config.conn.commit()

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

        # read game's goals
        self.fetch_goal_info()




    def set_location(self, sijainti):
        self.location = sijainti
        sql = "UPDATE Game SET location='" + sijainti.ident + "' WHERE id='" + self.id + "'"
        print(sql)
        cur = config.conn.cursor()
        cur.execute(sql)
        #config.conn.commit()
        #self.loc = sijainti.ident


    def fetch_goal_info(self):
        self.goals = []

        sql = "SELECT * FROM (SELECT Goal.id, Goal.name, Goal.description, GoalReached.gameid, "
        sql += "Goal.target, Goal.target_minvalue, Goal.target_maxvalue, Goal.target_text "
        sql += "FROM Goal INNER JOIN GoalReached ON Goal.id = GoalReached.goalid "
        sql += "WHERE GoalReached.gameid = '" + self.id + "' "
        sql += "UNION SELECT Goal.id, Goal.name, Goal.description, NULL, "
        sql += "Goal.target, Goal.target_minvalue, Goal.target_maxvalue, Goal.target_text "
        sql += "FROM Goal WHERE Goal.id NOT IN ("
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
            goal = Goal(a[0], a[1], a[2], is_reached, a[4], a[5], a[6], a[7])
            self.goals.append(goal)
        return
