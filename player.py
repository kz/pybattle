class Player(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.previous_attack_name = ""

    def deplete(self, points):
        self.health = self.health - points

    def set_previous_attack_name(self, attack):
        self.previous_attack_name = attack
