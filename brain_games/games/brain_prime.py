#!/usr/bin/env python3
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):  #  Функция проверяет является ли число простым или нет
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def right_answer_and_question():
    num = random.randint(2, 10)
    question1 = f'Question: {num}'
    answer1= is_prime(num)
    return question1, 'yes' if answer1 else 'no'
