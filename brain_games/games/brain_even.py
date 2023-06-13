#!/usr/bin/env python3
from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer_and_question(num):
    if num % 2 == 0:
        answer1 = 'yes'
        return answer1
    else:
        answer2 = 'no'
        return answer2


def right_answer_and_question():
    list_of_nums = randint(1, 100)
    answer1 = f'Question: {list_of_nums}'
    question1 = check_answer_and_question(list_of_nums)
    return question1, answer1
