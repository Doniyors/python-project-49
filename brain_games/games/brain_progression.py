<<<<<<< HEAD
from random import randint


QUESTION = "What number is missing in the progression?"
PROGRESSION_START_SPREAD = (1, 50)
PROGRESSION_STEP_SPREAD = (1, 10)
PROGRESSION_LENGTH_SPREAD = (5, 10)


def get_answer_and_question() -> tuple:
    progression_start = randint(*PROGRESSION_START_SPREAD)
    progression_step = randint(*PROGRESSION_STEP_SPREAD)
    progression_length = randint(*PROGRESSION_LENGTH_SPREAD)
    element_to_guess = randint(0, progression_length - 1)

    element_of_progression = progression_start
    progression = []
    for _ in range(progression_length):
        progression.append(str(element_of_progression))
        element_of_progression += progression_step

    right_answer = progression[element_to_guess]
    progression[element_to_guess] = ".."
    task = ("Question: " + " ".join(progression))
    return right_answer, task
=======
#!/usr/bin/env python3
import random

QUESTION = 'What number is missing in the progression?'


def right_answer_and_question():
    numbers = []
    len_of_list = random.randint(5, 10)
    index_to_replace = random.randint(0, len_of_list - 1)
    number_to_join = random.randint(2, 5)
    random_number = random.randint(1, 10)
    numbers.append(random_number)
    for _ in range(len_of_list):
        previous_number = numbers[-1]
        new_number = previous_number + number_to_join
        numbers.append(new_number)
    answer1 = numbers[index_to_replace]  # Значение которое нужно угадать
    numbers[index_to_replace] = '..'
    question1 = 'Question: ' + ' '.join(str(num) for num in numbers)
    return str(answer1), question1
>>>>>>> my-branch
