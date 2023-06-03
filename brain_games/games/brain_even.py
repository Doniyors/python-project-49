#!/usr/bin/env python3
import prompt

from brain_games.cli import welcome_user


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    list_of_num = [15, 6, 7]

    for i in list_of_num:
        print(f'Question: {i}')
        user_input = input("Your answer: ")
        result = check_answer(user_input, i, name)
        print(result)
        if result != 'Correct!':
            return
    print('Congratulations, ' + name + '!')


def check_answer(answer, i, name):
    if answer.lower() == "no" and i % 2 != 0:
        return 'Correct!'
    elif answer.lower() == "yes" and i % 2 == 0:
        return 'Correct!'
    elif answer.lower() == "no" and i % 2 == 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""
    elif answer.lower() == "yes" and i % 2 != 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""


if __name__ == '__main__':
    main()
