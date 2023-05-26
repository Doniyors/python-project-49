#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    for _ in range(3):
        i = (random.randint(1, 100))
        i1 = (random.randint(1, 100))
        i2 = i + i1
        print(str(i) + '+' + str(i1))
        user_input1 = input("Введите ваш ответ: ")
        if i + i1 == int(user_input1):
            print('correct')
        else:
            print(user_input1 + ' is wrong answer ;(. Correct answer was ' + str(i2) + ".Let's try again, Sam!")
            return
        print('Congratulations,' + name)


if __name__ == '__main__':
    main()
