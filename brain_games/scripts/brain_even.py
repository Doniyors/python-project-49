#!/usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def main():
    welcome_user()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


    print('Answer "yes" if the number is even, otherwise answer "no".')
    question1 = 15
    question2 = 6
    question3 = 7
    print(f'Question: {question1}')


    user_input1 = input("Введите ваш ответ: ")
    result = check_answer1(user_input1, name)
    print(result)


    if 'wrong answer' in result:
        return
                                                                        

    print(f'Question: {question2}')
    user_input2 = input("Введите ваш ответ: ")
    result = check_answer2(user_input2, name)
    print(result)


    if 'wrong answer' in result:
        return
                                                                                                    

    print(f'Question: {question3}')
    user_input3 = input("Введите ваш ответ: ")
    result = check_answer3(user_input3, name)
    print(result)


    # функции для проверки ответов:

def check_answer1(answer, name):
    if answer.lower() == "no":
        return f'Congratulations, {name}'
    elif answer.lower() == "yes":
        return f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again,"


def check_answer2(answer, name):
    if answer.lower() == "yes":
        return f'Congratulations, {name}'
    elif answer.lower() == "no":
        return f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}"


def check_answer3(answer, name):
    if answer.lower() == "no":
        return f'Congratulations, {name}'
    elif answer.lower() == "yes":
        return f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}"


if __name__ == '__main__':
    main()