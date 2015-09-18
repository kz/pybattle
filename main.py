#!/usr/bin/env python
from time import sleep
from player import Player
from attack import Attack
import yaml


def main():
    # Load YAML config
    config_path = "./attack.yml"
    f = open(config_path, 'r')
    attack_config = yaml.load(f)
    f.close()


    # Load attacks
    attacks = []
    for name, properties in attack_config.items():
        attacks.append(Attack(name, int(properties['strength']), int(properties['accuracy'])))


    # Introduce the game
    print("""
    PyBattle
    ===
    Each player is given a python with 100HP (health points).
    The first player whose python depletes the other python's health points wins.
    ===
    """)

    # Obtain player names
    player_one = Player(input("What is Player 1's name? "))
    player_two = Player(input("What is Player 2's name? "))

    # Start the game
    print()
    print("{!s} challenges {!s} to a python battle!".format(player_one.name, player_two.name))
    sleep(0.5)

    # Start a round
    while player_one.health < 0 and player_two.health < 0:





if __name__ == '__main__':
    main()
