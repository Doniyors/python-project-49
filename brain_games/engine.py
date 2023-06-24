import prompt


def start_game_end_game(game, raunds: int = 3):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.GAME_RULES)
    for _ in range(raunds):
        question, answer = game.get_answer_and_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != answer:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f" Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")
