#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

DIGIT_INTERVAL = (2, 10)


def is_prime(n):  # Функция проверяет является ли число простым или нет
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_answer_and_question():
    num = random.randint(*DIGIT_INTERVAL)
    question = f'{num}'
    answer = is_prime(num)
    return question, 'yes' if answer else 'no'
