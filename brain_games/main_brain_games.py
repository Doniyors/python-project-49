#!/usr/bin/env python3
import random
import prompt


def generate_numbers():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    while random_num1 >= random_num2:
        random_num1 = random.randint(1, 100)
        random_num2 = random.randint(1, 100)
    return random_num1, random_num2


def calculate_result(random_num1, random_num2, operation):
    if operation == '+':
        return random_num1 + random_num2
    elif operation == '-':
        return random_num1 - random_num2
    elif operation == '*':
        return random_num1 * random_num2


def main1():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    operations = ['+', '-', '*']
    for _ in range(3):
        random_num1, random_num2 = generate_numbers()
        operation = random.choice(operations)
        question = f"Question: {random_num1} {operation} {random_num2}"
        user_answer = prompt.string(question + "\nYour answer: ")
        expected_result = calculate_result(random_num1, random_num2, operation)

        if int(user_answer) == expected_result:
            print("Correct!")
        else:
            print(f"Sorry, '{user_answer}' is the wrong answer. "
                  f"The correct answer is '{expected_result}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main1()


def main2():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    list_of_num = [15, 6, 7]

    for i in list_of_num:
        print(f'Question: {i}')
        user_input = input("Your answer: ")
        result = check_answer(user_input, i, name)
        print(result)
        if result != 'Correct!':
            return
    print('Congratulations, ' + name + '!')


def check_answer(answer, i, name):
    if answer.lower() == "no" and i % 2 != 0:
        return 'Correct!'
    elif answer.lower() == "yes" and i % 2 == 0:
        return 'Correct!'
    elif answer.lower() == "no" and i % 2 == 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""
    elif answer.lower() == "yes" and i % 2 != 0:
        return f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!"""


if __name__ == '__main__':
    main2()


def welcome_user():
    print("Welcome to the Brain Games!")


def find_gcd(a, b):  # Находит самое большую цифру на которую делятся оба числа
    while b != 0:
        a, b = b, a % b
    return a


def main3():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        random_number1 = random.randint(1, 100)
        random_number2 = random.randint(1, 100)
        gcd = find_gcd(random_number1, random_number2)
        print(f'Question: {random_number1} {random_number2}')
        user_input1 = input("Your answer: ")
        if int(user_input1) == gcd:
            print('Correct!')
        else:
            print(f"'{user_input1}' is wrong answer ;(.")
            print(f"Correct answer was '{str(gcd)}'. Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main3()


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
        print(f"'{user_input1}' is wrong answer ;(.")
        print(f"Correct answer was 'yes'. Let's try again, {name}!")
        return False
    if is_prime(num) is True and user_input1.lower() == 'no':
        print(f"'{user_input1}' is wrong answer ;(.")
        print(f"Correct answer was 'yes'. Let's try again, {name}!")
        return False


def main4():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for_congratulations = 0
    for_congratulations_num_2 = 3
    for _ in range(3):
        if generate_prime(name) is False:
            break
        else:
            for_congratulations += 1
            continue

    if for_congratulations == for_congratulations_num_2:
        print("Congratulations, " + name + '!')


if __name__ == '__main__':
    main4()


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
    i = numbers[index_to_replace]  # Значение которое нужно угадать
    numbers[index_to_replace] = '..'
    text = 'Question:'
    for num in numbers:
        text += f' {str(num) }'
    print(text)
    i5 = input("Your answer: ")
    if int(i5) == i:
        print('Correct!')
        return True
    else:
        print(f"""'{i5}' is wrong answer ;(. Correct answer was '{str(i)}'.
Let's try again, {name}!""")
        return False


def main5():
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
    main5()
