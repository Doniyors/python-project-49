#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def find_gcd(a, b):  # Находит самое большую цифру на которую делятся оба числа
    while b != 0:
        a, b = b, a % b
    return a


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        gcd = find_gcd(random_number1, random_number2)
        print(f'Question: {random_number1} {random_number2}')
        user_input1 = input("Your answer: ")
        if int(user_input1) == gcd:
            print('Correct!')
        else:
            print(f"'{user_input1}' is wrong answer ;(.")
            print(f"Correct answer was '{str(gcd)}'. Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
