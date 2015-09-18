import random


class Attack(object):
    def __init__(self, name, strength, accuracy):
        self.name = name
        self.strength = strength
        self.accuracy = accuracy

    def attempt(self):
        result = {}

        if random.randint(0, 101) <= self.accuracy:
            result['strength'] = self.strength
            result['message'] = "{current}'s python attacked with {strength} strength!" \
                                "\n{target}'s python now has {health} HP."
        else:
            result['strength'] = 0
            result['message'] = "{current}'s python missed!\n{target}'s python is unaffected."

        return result
