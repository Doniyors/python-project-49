#!/usr/bin/env python3
import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):  # Находит самое большую цифру на которую делятся оба числа
    while b != 0:
        a, b = b, a % b
    return str(a)


def right_answer_and_question():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question1 = find_gcd(random_number1, random_number2)
    answer1 = f'Question: {random_number1} {random_number2}'
    return question1, answer1
