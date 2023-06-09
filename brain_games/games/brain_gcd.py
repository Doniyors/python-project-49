#!/usr/bin/env python3
import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'

FIRST_DIGIT_INTERVAL = (1, 100)
SECOND_DIGIT_INTERVAL = (1, 100)


def find_gcd(a, b):  # Находит самое большую цифру на которую делятся оба числа
    while b != 0:
        a, b = b, a % b
    return a


def get_answer_and_question():
    random_number1 = random.randint(*FIRST_DIGIT_INTERVAL)
    random_number2 = random.randint(*SECOND_DIGIT_INTERVAL)
    answer = find_gcd(random_number1, random_number2)
    question = f'{random_number1} {random_number2}'
    return question, str(answer)
