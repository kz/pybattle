class Player(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.previous_attack_name = ""
        self.has_healed = False

    def deplete(self, points):
        self.health = self.health - points

    def heal(self, points):
        self.health = self.health + points
        if self.health > 100:
            self.health = 100

    def set_previous_attack_name(self, attack):
        self.previous_attack_name = attack
