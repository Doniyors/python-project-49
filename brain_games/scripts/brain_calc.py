#!/usr/bin/env python3
import random
import prompt


def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    while num1 >= num2:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    return num1, num2


def calculate_result(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    operations = ['+', '-', '*']
    for _ in range(3):
        num1, num2 = generate_numbers()
        operation = random.choice(operations)
        question = f"Question: {num1} {operation} {num2}"
        user_answer = prompt.string(question + "\nYour answer: ")
        expected_result = calculate_result(num1, num2, operation)

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
