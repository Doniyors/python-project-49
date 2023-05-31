#!/usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions = [15, 6, 7]

    for question in questions:
        print(f'Question: {question}')
        user_input = input("Your answer: ")
        result = check_answer(user_input, question, name)
        print(result)
        if result != 'Correct!':
            return
    print('Congratulations, ' + name + '!')


def check_answer(answer, question, name):
    if answer.lower() == "no" and question % 2 != 0:
        return 'Correct!'
    elif answer.lower() == "yes" and question % 2 == 0:
        return 'Correct!'
    elif answer.lower() == "no" and question % 2 == 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""
    elif answer.lower() == "yes" and question % 2 != 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""


if __name__ == '__main__':
    main()
