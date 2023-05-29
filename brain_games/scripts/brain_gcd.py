#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        gcd = find_gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        user_input1 = input("Your answer: ")
        if int(user_input1) == gcd:
            print('Correct!')
        else:
            print(f"'{user_input1}' is wrong answer ;(. Correct answer was '{str(gcd)}'. Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')



if __name__ == '__main__':
    main()
