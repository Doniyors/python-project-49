#!/usr/bin/env python3
from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

LEN_OF_LIST1 = (1, 100)


def check_answer(num):  # Функция проверяет на чётность
    if num % 2 == 0:
        return True
    else:
        return False


def right_answer_and_question():
    list_of_nums = randint(*LEN_OF_LIST1)
    question1 = f'{list_of_nums}'
    answer1 = check_answer(list_of_nums)
    return question1, 'yes' if answer1 else 'no'
