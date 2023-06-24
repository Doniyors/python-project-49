#!/usr/bin/env python3
import random

GAME_RULES = 'What number is missing in the progression?'

FIRST_DIGIT_INTERVAL = (5, 10)
SECOND_DIGIT_INTERVAL = (2, 5)
DIGIT_INTERVAL = (1, 10)


def get_answer_and_question():
    first_term = random.randint(*FIRST_DIGIT_INTERVAL)
    index_replace = random.randint(0, first_term - 1)
    differences = random.randint(*SECOND_DIGIT_INTERVAL)
    random_num = random.randint(*DIGIT_INTERVAL)
    numbers = give_question(first_term, index_replace, differences, random_num)
    answer = numbers[index_replace]
    question = formulate_question(numbers, index_replace)
    return question, str(answer)


def formulate_question(numbers, index_to_replace):
    numbers_with_placeholder = numbers.copy()
    numbers_with_placeholder[index_to_replace] = '..'
    question = " ".join(str(num) for num in numbers_with_placeholder)
    return question


def give_question(first_term, index_replace, differences, random_num):
    numbers = []
    numbers.append(random_num)
    for _ in range(first_term):
        previous_number = numbers[-1]
        new_number = previous_number + differences
        numbers.append(new_number)
    return numbers
