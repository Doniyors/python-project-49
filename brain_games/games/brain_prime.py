#!/usr/bin/env python3
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):  # Проверяет является ли число простым или нет
    if n < 2:
        return 'no'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def right_answer_and_question():
    num = random.randint(2, 10)
    answer1 = f'Question: {num}'
    question1 = is_prime(num)
    return question1, answer1
