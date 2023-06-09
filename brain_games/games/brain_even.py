#!/usr/bin/env python3
from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

DIGIT_INTERVAL = (1, 100)


def is_even(num):  # Функция проверяет на чётность
    return num % 2 == 0


def get_answer_and_question():
    number_for_question = randint(*DIGIT_INTERVAL)
    question = f'{number_for_question}'
    answer = is_even(number_for_question)
    return question, 'yes' if answer else 'no'
