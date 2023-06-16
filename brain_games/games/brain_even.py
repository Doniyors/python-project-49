#!/usr/bin/env python3
from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(num):  # Функция проверяет на чётность
    if num % 2 == 0:
        return True
    else:
        return False


def right_answer_and_question():
    list_of_nums = randint(1, 100)
    question1 = f'{list_of_nums}'
    answer1 = check_answer(list_of_nums)
    return question1, 'yes' if answer1 else 'no'
