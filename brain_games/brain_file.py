import sys
from brain_games.games.brain_games import main as brain_games_main
from brain_games.games.brain_calc import main as brain_calc_main
from brain_games.games.brain_prime import main as brain_prime_main
from brain_games.games.brain_progression import main as brain_progression_main
from brain_games.games.brain_even import main as brain_even_main
from brain_games.games.brain_gcd import main as brain_gcd_main


def main_games():
    brain_games_main()


def main_calc():
    # Код для запуска игры brain_calc
    brain_calc_main()


def main_prime():
    # Код для запуска игры brain_prime
    brain_prime_main()


def main_progression():
    # Код для запуска игры brain_progression
    brain_progression_main()


def main_even():
    # Код для запуска игры brain_even
    brain_even_main()


def main_gcd():
    # Код для запуска игры brain_gcd
    brain_gcd_main()


if __name__ == '__main__':
    available_games = {
        'brain-calc': main_calc,
        'brain-prime': main_prime,
        'brain-progression': main_progression,
        'brain-even': main_even,
        'brain-gcd': main_gcd
    }

    if len(sys.argv) < 2:
        print("""Не указана игра.
        Укажите одну из доступных игр: brain-calc, brain-prime,
        brain-progression, brain-even, brain-gcd""")
    else:
        game_name = sys.argv[1]
        if game_name in available_games:
            available_games[game_name]()
        else:
            print("""Неверное имя игры.
            Укажите одну из доступных игр: brain-calc, brain-prime,
            brain-progression, brain-even, brain-gcd""")
