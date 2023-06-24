#!/usr/bin/env python3
import random

operations = ['+', '-', '*']

GAME_RULES = "What is the result of the expression?"

FIRST_DIGIT_INTERVAL = (1, 100)
SECOND_DIGIT_INTERVAL = (1, 100)


def generate_numbers():
    first_number = random.randint(*FIRST_DIGIT_INTERVAL)
    second_number = random.randint(*SECOND_DIGIT_INTERVAL)
    while first_number <= second_number:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
    return first_number, second_number


def calculate_result(first_number, second_number, operation):
    if operation == '+':
        return str(first_number + second_number)
    elif operation == '-':
        return str(first_number - second_number)
    elif operation == '*':
        return str(first_number * second_number)


def get_answer_and_question():
    first_number, second_number = generate_numbers()
    operation = random.choice(operations)
    question = f"{first_number} {operation} {second_number}"
    answer = calculate_result(first_number, second_number, operation)
    return question, answer
