import random


class Attack(object):
    def __init__(self, name, strength, accuracy):
        self.name = name
        self.strength = strength
        self.accuracy = accuracy

    def attempt(self):
        payload = {}

        if random.randint(0, 101) <= self.accuracy:
            payload['strength'] = self.strength
            payload['message'] = "{!s}'s python attacked with {!s} strength!\n{!s}'s python now has {!s} HP."
        else:
            payload['strength'] = 0
            payload['message'] = "{!s}'s python missed!\n{!s}'s python is unaffected."
