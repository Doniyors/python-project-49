#!/usr/bin/env python3
import prompt

from brain_games.cli import welcome_user


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


if __name__ == '__main__':
    main()
