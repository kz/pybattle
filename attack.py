import random


class Attack(object):
    def __init__(self, name, strength, accuracy):
        self.name = name
        self.strength = strength
        self.accuracy = accuracy

    def attempt(self, previous_attack_name):
        result = {}

        # Define dodge accuracy stat
        dodge_num = 30

        # Check if the target previously used dodge
        accuracy = self.accuracy
        if previous_attack_name == "Dodge":
            accuracy -= dodge_num

        if random.randint(0, 101) <= self.accuracy:
            result['strength'] = self.strength
            if previous_attack_name == "Dodge" and self.name != "Dodge":
                result['message'] = "{target}'s python failed to dodge the attack!" \
                                    "\n{current}'s python attacked with {strength} strength!" \
                                    "\n{target}'s python now has {health} HP."
            elif self.name == "Dodge":
                result['message'] = "{current}'s python will attempt to dodge the next attack!"
            else:
                result['message'] = "{current}'s python attacked with {strength} strength!" \
                                    "\n{target}'s python now has {health} HP."
        else:
            result['strength'] = 0
            if self.accuracy != accuracy:
                result['message'] = "{target}'s python dodged the attack!\n{target}'s python is unaffected."
            else:
                result['message'] = "{current}'s python missed!\n{target}'s python is unaffected."
        return result
