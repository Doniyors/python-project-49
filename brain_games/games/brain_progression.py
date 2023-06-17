#!/usr/bin/env python3
import random

QUESTION = 'What number is missing in the progression?'


LEN_OF_LIST = (5, 10)
NUMBER_TO_JOIN = (2, 5)
RANDOM_NUMBER = (1, 10)


def random_function():
    len_of_list1 = random.randint(*LEN_OF_LIST)
    index_to_replace1 = random.randint(0, len_of_list1 - 1)
    number_to_join1 = random.randint(*NUMBER_TO_JOIN)
    random_number1 = random.randint(*RANDOM_NUMBER)
    return len_of_list1, index_to_replace1, number_to_join1, random_number1


def right_answer_and_question():
    numbers = give_question1()
    index_to_replace1 = random.randint(0, len(numbers) - 1)
    answer1 = numbers[index_to_replace1]
    numbers[index_to_replace1] = '..'
    question1 = " ".join(str(num) for num in numbers)
    return question1, str(answer1)


def give_question1():
    numbers = []
    len_of_list1, _, number_to_join1, random_number1 = random_function()
    numbers.append(random_number1)
    for _ in range(len_of_list1):
        previous_number = numbers[-1]
        new_number = previous_number + number_to_join1
        numbers.append(new_number)
    return numbers
