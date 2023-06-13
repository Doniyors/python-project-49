<<<<<<< HEAD
from random import randint
from brain_games.engine import NO, YES


NUMBER_SPREAD = (1, 100)

QUESTION = (f'Answer "{YES}" if the number is even, '
            f'otherwise answer "{NO}".')


def is_even(num: int) -> str:
    if num % 2 == 0:
        return YES
    return NO


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    right_answer = is_even(number)
    task = (f'Question: {number}')
    return right_answer, task
=======
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
>>>>>>> my-branch
