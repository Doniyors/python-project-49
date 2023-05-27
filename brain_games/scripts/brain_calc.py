#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    text1 = 'What is the result of the expression?'
    text2 = 'what is the result of the subtraction?'
    text3 = 'What is result of multiplication?'
    operations = ['+', '-', '*']
    for _ in range(3):  # цикл повторяется 3 раза
        i = (random.randint(1, 100))
        i1 = (random.randint(1, 100))
        i2 = i + i1
        while i <= i1:  # Повторяем генерацию чисел, пока первое число не станет больше второго
            i = random.randint(1, 100)
            i1 = random.randint(1, 100)
        operation = random.choice(operations)
        if operation == '+':
            print(f'{text1}')
        elif operation == '-':
            print(f'{text2}')
        elif operation == '*':
            print(f'{text3}')
        print(f'{i} {operation} {i1}')
        user_input1 = input("Введите ваш ответ: ")
        if operation == '+':
            expected_result = i + i1
        elif operation == '-':
            expected_result = i - i1
        elif operation == '*':
            expected_result = i * i1
        if int(user_input1) == expected_result:
            print('Correct!')
        else:
            print(user_input1 + ' is wrong answer ;(. Correct answer was ' + str(i2) + ".Let's try again," + name)
            return
    print('Congratulation, ' + name)


if __name__ == '__main__':
    main()
