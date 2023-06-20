#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

RANDOM_NUMBER = (2, 10)


def is_prime(n):  # Функция проверяет является ли число простым или нет
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_answer_and_question():
    num = random.randint(*RANDOM_NUMBER)
    question = f'{num}'
    answer = is_prime(num)
    return question, 'yes' if answer else 'no'
