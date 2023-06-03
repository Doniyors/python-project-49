#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def generate_numbers():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    while random_num1 >= random_num2:
        random_num1 = random.randint(1, 100)
        random_num2 = random.randint(1, 100)
    return random_num1, random_num2


def calculate_result(random_num1, random_num2, operation):
    if operation == '+':
        return random_num1 + random_num2
    elif operation == '-':
        return random_num1 - random_num2
    elif operation == '*':
        return random_num1 * random_num2


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    operations = ['+', '-', '*']
    for _ in range(3):
        random_num1, random_num2 = generate_numbers()
        operation = random.choice(operations)
        question = f"Question: {random_num1} {operation} {random_num2}"
        user_answer = prompt.string(question + "\nYour answer: ")
        expected_result = calculate_result(random_num1, random_num2, operation)

        if int(user_answer) == expected_result:
            print("Correct!")
        else:
            print(f"Sorry, '{user_answer}' is the wrong answer. "
                  f"The correct answer is '{expected_result}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
