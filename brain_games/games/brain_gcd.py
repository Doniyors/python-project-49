#!/usr/bin/env python3
import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):  # Находит самое большую цифру на которую делятся оба числа
    while b != 0:
        a, b = b, a % b
    return a


def right_answer_and_question():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    answer1 = find_gcd(random_number1, random_number2)
    question1 = f'Question: {random_number1} {random_number2}'
    return question1, str(answer1)
