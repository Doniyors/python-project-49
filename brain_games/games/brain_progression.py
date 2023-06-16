#!/usr/bin/env python3
import random

QUESTION = 'What number is missing in the progression?'


def random_function():
    len_of_list = random.randint(5, 10)
    index_to_replace = random.randint(0, len_of_list - 1)
    number_to_join = random.randint(2, 5)
    random_number = random.randint(1, 10)
    return len_of_list, index_to_replace, number_to_join, random_number


def right_answer_and_question():
    _, index_to_replace, _, _ = random_function()
    numbers = give_question1()
    answer1 = numbers[index_to_replace] # Значение которое нужно угадать
    numbers[index_to_replace] = '..'
    question1 = " ".join(str(num) for num in numbers)
    return question1, str(answer1)


def give_question1():
    numbers = []
    len_of_list, _, number_to_join, random_number = random_function()
    numbers.append(random_number)
    for _ in range(len_of_list):
        previous_number = numbers[-1]
        new_number = previous_number + number_to_join
        numbers.append(new_number)
    return numbers
