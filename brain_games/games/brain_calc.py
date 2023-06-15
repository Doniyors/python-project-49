#!/usr/bin/env python3
import random

operations = ['+', '-', '*']

QUESTION = "What is the result of the expression?"


def generate_numbers():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    while random_num1 >= random_num2:
        random_num1 = random.randint(1, 100)
        random_num2 = random.randint(1, 100)
    return random_num1, random_num2


def calculate_result(random_num1, random_num2, operation):
    if operation == '+':
        return str(random_num1 + random_num2)
    elif operation == '-':
        return str(random_num1 - random_num2)
    elif operation == '*':
        return str(random_num1 * random_num2)


def right_answer_and_question():
    random_num1, random_num2 = generate_numbers()
    operation = random.choice(operations)
    question1 = f"Question: {random_num1} {operation} {random_num2}"
    answer1 = calculate_result(random_num1, random_num2, operation)
    return answer1, question1
