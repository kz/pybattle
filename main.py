#!/usr/bin/env python
from player import Player
from attack import Attack

def main():
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

    print("{!s} challenges {!s} to a python battle!".format(player_one.name, player_two.name))


if __name__ == '__main__':
    main()
