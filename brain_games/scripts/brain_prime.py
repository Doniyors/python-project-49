#!/usr/bin/env python3
import random
import prompt


def is_prime(n):  # Проверяет является ли число простым или нет
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(name):
        num = random.randint(2, 10)  # Генерируйте числа в нужном диапазоне
        print(f'Question: {num}')
        user_input1 = input("Your answer: ")
        if is_prime(num) is True and user_input1.lower() == 'yes':
            print('Correct!')
        if is_prime(num) is False and user_input1.lower() == 'no':
            print('Correct!')
        if is_prime(num) is False and user_input1.lower() == 'yes':
            print(user_input1 + " is wrong answer ;(. Correct answer was 'yes'.Let s try again, " + name + '!')
            return False
        if is_prime(num) is True and user_input1.lower() == 'no':
            print(user_input1 + " is wrong answer ;(. Correct answer was 'yes'.Let s try again, " + name + '!')
            return False


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for_congratulations = 0
    for_congratulations_num_2 = 3
    for _ in range(3):
        for_congratulations += 1
        if generate_prime(name) is False:
            break
        else:
            continue

    if for_congratulations == for_congratulations_num_2:
        print("Congratulations, " + name + '!')

if __name__ == '__main__':
    main()
