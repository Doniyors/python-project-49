import prompt


def start_game(game, games_num: int = 3):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.QUESTION)
    for _ in range(games_num):
        question1, answer1 = game.right_answer_and_question()
        print(question1)
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != answer1:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f" Correct answer was '{answer1}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")
