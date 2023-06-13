<<<<<<< HEAD
from math import sqrt
from random import randint
from brain_games.engine import NO, YES


QUESTION = (f'Answer "{YES}" if given number is prime. '
            f'Otherwise answer "{NO}".')

NUMBER_SPREAD = (1, 100)


def is_prime(num: int) -> str:
    if num in [1, 2]:
        return YES
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return NO
    return YES


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    right_answer = is_prime(number)
    task = (f"Question: {number}")
    return right_answer, task
=======
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
>>>>>>> my-branch
