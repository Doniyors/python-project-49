#!/usr/bin/env python
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def game(name):
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
    i = numbers[index_to_replace]
    numbers[index_to_replace] = '..'
    text = 'Question:'
    for num in numbers:
        text += f' {str(num) }'
    print(text)
    user_input1 = input("Your answer: ")
    if int(user_input1) == i:
        print('Correct!')
        return True
    else:
        print(f"{user_input1} is wrong answer ;(.")
        print(f"Correct answer was {str(i)}. Let's try again, {name}!")
        return False


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    correct_answers = 0
    total_questions = 3

    while correct_answers < total_questions:
        if game(name):
            correct_answers += 1
        else:
            break

    if correct_answers == total_questions:
        print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
