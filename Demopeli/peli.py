import random

class Peli:
    def __init__(self, nick, raha):
        self.id = str(random.randint(1,100000000))+str(random.randint(1,100000000))
        self.raha = raha
        self.nick = nick
