import sys
from brain_games.games.brain_calc import main as brain_calc_main
from brain_games.games.brain_prime import main as brain_prime_main
from brain_games.games.brain_progression import main as brain_progression_main
from brain_games.games.brain_even import main as brain_even_main
from brain_games.games.brain_gcd import main as brain_gcd_main


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
    # Проверяем переданное имя игры и запускаем соответствующую игру
    if len(sys.argv) < 2:
        print("Не указана игра. Укажите одну из доступных игр: brain-calc, brain-prime, brain-progression, brain-even, brain-gcd")
    else:
        game_name = sys.argv[1]
        if game_name == 'brain-calc':
            main_calc()
        elif game_name == 'brain-prime':
            main_prime()
        elif game_name == 'brain-progression':
            main_progression()
        elif game_name == 'brain-even':
            main_even()
        elif game_name == 'brain-gcd':
            main_gcd()
        else:
            print("Неверное имя игры. Укажите одну из доступных игр: brain-calc, brain-prime, brain-progression, brain-even, brain-gcd")