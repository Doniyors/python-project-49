<<<<<<< HEAD
from random import randint, choice

QUESTION = "What is the result of the expression?"

NUMBER_SPREAD = (1, 30)

OPERATORS = ['+', '-', '*']
=======
#!/usr/bin/env python3
import random

operations = ['+', '-', '*']

QUESTION = "What is the result of the expression?"
>>>>>>> my-branch


def get_right_answer(num1: int, num2: int, operator: str) -> str | None:
    if operator == "*":
        return str(num1 * num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "+":
        return str(num1 + num2)


<<<<<<< HEAD
def get_answer_and_question() -> tuple:
    operand1 = (randint(*NUMBER_SPREAD))
    operand2 = (randint(*NUMBER_SPREAD))
    operator = choice(OPERATORS)
    right_answer = get_right_answer(operand1, operand2, operator)
    task = f'Question: {operand1} {operator} {operand2}'

    return right_answer, task
=======
def calculate_result(random_num1, random_num2, operation):
    if operation == '+':
        return str(random_num1 + random_num2)
    elif operation == '-':
        return str(random_num1 - random_num2)
    elif operation == '*':
        return str(random_num1 * random_num2)


def right_answer_and_question():
    for _ in range(3):
        random_num1, random_num2 = generate_numbers()
        operation = random.choice(operations)
        question1 = f"Question: {random_num1} {operation} {random_num2}"
        answer1 = calculate_result(random_num1, random_num2, operation)

        return answer1, question1
>>>>>>> my-branch
