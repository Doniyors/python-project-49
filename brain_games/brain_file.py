import sys
from brain_games.games.brain_games import main as brain_games_main
from brain_games.games.brain_calc import main as brain_calc_main
from brain_games.games.brain_prime import main as brain_prime_main
from brain_games.games.brain_progression import main as brain_progression_main
from brain_games.games.brain_even import main as brain_even_main
from brain_games.games.brain_gcd import main as brain_gcd_main

games = {
    'brain-calc': brain_calc_main,
    'brain-prime': brain_prime_main,
    'brain-progression': brain_progression_main,
    'brain-games': brain_games_main,
    'brain-even': brain_even_main,
    'brain-gcd': brain_gcd_main
}


def main():
    if len(sys.argv) < 2:
        print("Не указана игра.")
        return

    game_name = sys.argv[1]

    if game_name in games:
        games[game_name].run()
    else:
        print(f"Неверное имя игры: {game_name}")


if __name__ == '__main__':
    main()
