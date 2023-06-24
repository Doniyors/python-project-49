#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.engine import start_game_end_game


def main():
    start_game_end_game(brain_gcd)


if __name__ == "__main__":
    main()
