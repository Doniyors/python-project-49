#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    for _ in range(3):
        i = (random.randint(1, 100))
        i1 = (random.randint(1, 100))
        #   minimum = min(i, i1)
        maximum = max(i, i1)
        print('Which number is greater?')
        print(f'{i} {i1}')
        user_input1 = input("Введите ваш ответ: ")
        if int(user_input1) == maximum:
            print('Correct!')
        else:
            print(user_input1 + ' is wrong answer ;(. Correct answer was ' + str(maximum) + ".Let's try again," + name)
            return
    print('Congratulations, ' + name)


if __name__ == '__main__':
    main()
