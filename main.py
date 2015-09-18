#!/usr/bin/env python
from time import sleep

import yaml

from player import Player
from attack import Attack


def main():
    # Load YAML config
    config_path = "./attack.yml"
    f = open(config_path, 'r')
    attack_config = yaml.load(f)
    f.close()

    # Load attacks
    attacks = {}
    for name, properties in attack_config.items():
        attacks[name] = (Attack(name, int(properties['strength']), int(properties['accuracy'])))

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
    print("\n{!s} challenges {!s} to a python battle!\n".format(player_one.name, player_two.name))
    sleep(0.5)

    # Assign players to current/target players
    current_player = player_one
    target_player = player_two

    # Start a round
    while player_one.health > 0 and player_two.health > 0:
        # Output player's turn
        sleep(0.5)
        print("It's {!s}'s turn --\n".format(current_player.name))
        sleep(0.5)

        # Output player HPs
        sleep(0.5)
        print("{!s} - {!s}/100 HP".format(player_one.name, player_one.health))
        print("{!s} - {!s}/100 HP\n".format(player_two.name, player_two.health))
        sleep(0.5)

        # Output available attacks
        sleep(0.5)
        print("Available attacks:")
        print("==================")
        for name, attack in attacks.items():
            print("{!s} - Strength: {!s} - Accuracy: {!s}".format(attack.name, attack.strength, attack.accuracy))
        print("==================\n")
        sleep(0.5)

        # Player inputs attack
        while True:
            input_attack = input("{!s}, enter the name of the attack you want to use: ".format(current_player.name))
            if input_attack in attacks:
                chosen_attack = attacks[input_attack]
                break
            else:
                print("The selected attack is invalid. Try again!\n")

        # Show chosen attack
        sleep(1)
        # noinspection PyUnboundLocalVariable
        print("\n{!s} chose {!s}!\n".format(current_player.name, chosen_attack.name))
        sleep(1)

        # Process attack
        attack_result = chosen_attack.attempt()
        target_player.deplete(attack_result['strength'])

        # Display attack result to players
        print(attack_result['message']
              .replace('{current}', current_player.name)
              .replace('{target}', target_player.name)
              .replace('{strength}', str(attack_result['strength']))
              .replace('{health}', str(target_player.health)))

        # Update player objects and switch around current/target players
        if current_player.name == player_one.name:
            player_one = current_player
            player_two = target_player

            current_player = player_two
            target_player = player_one
        else:
            player_two = current_player
            player_one = target_player

            current_player = player_one
            target_player = player_two

        sleep(1.5)
        print("\n=======================================================\n")

    # Calculate winning/losing player
    if player_one.health <= 0:
        winning_player = player_one
        losing_player = player_two
    else:
        winning_player = player_two
        losing_player = player_one

    # Display results to players
    print("{!s}'s python falls to the ground in defeat.".format(losing_player.name))
    print("{!s} is the winner!".format(winning_player.name))


if __name__ == '__main__':
    main()
