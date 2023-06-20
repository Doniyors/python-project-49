#!/usr/bin/env python3
import random

GAME_RULES = 'What number is missing in the progression?'


RANDOM_NUMBER_INTERVAL_FOR_LIST = (5, 10)
RANDOM_NUMBER_INTERVA_TO_JOIN = (2, 5)
RANDOM_NUMBER = (1, 10)


def random_function():
    len_of_list1 = random.randint(*RANDOM_NUMBER_INTERVAL_FOR_LIST)
    index_to_replace1 = random.randint(0, len_of_list1 - 1)
    number_to_join1 = random.randint(*RANDOM_NUMBER_INTERVA_TO_JOIN)
    random_number1 = random.randint(*RANDOM_NUMBER)
    return len_of_list1, index_to_replace1, number_to_join1, random_number1


def get_answer_and_question():
    numbers = give_question1()
    _, index_to_replace1, _, _ = random_function()
    answer = numbers[index_to_replace1]
    question = formulate_question(numbers, index_to_replace1)
    return question, str(answer)


def formulate_question(numbers, index_to_replace):
    numbers_with_placeholder = numbers.copy()
    numbers_with_placeholder[index_to_replace] = '..'
    question = " ".join(str(num) for num in numbers_with_placeholder)
    return question


def give_question1():
    numbers = []
    len_of_list1, _, number_to_join1, random_number1 = random_function()
    numbers.append(random_number1)
    for _ in range(len_of_list1):
        previous_number = numbers[-1]
        new_number = previous_number + number_to_join1
        numbers.append(new_number)
    return numbers
