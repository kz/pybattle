class Python(object):
    def __init__(self, health=100):
        self.health = health

    def deplete(self, points):
        self.health = self.health - points
