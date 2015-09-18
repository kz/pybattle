class Player(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def deplete(self, points):
        self.health = self.health - points
