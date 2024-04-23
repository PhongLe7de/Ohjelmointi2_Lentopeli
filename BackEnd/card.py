import sqlqueries
import random
from colorama import Fore, Style
import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def co_card(player_n):
    co_card = sqlqueries.co_card_sql()
    points = co_card['score']
    print_slow(Fore.YELLOW + f"Hiilidioksidikortti: {co_card['flavour_text']}" + Style.RESET_ALL)

    print(Fore.RED + f"Saat {points} Ökyrikas-pistettä!" + Style.RESET_ALL)
    if co_card['effect'] > 0:
        sqlqueries.effect_skip_turn_update(1, player_n)
    return points


def card_on_airport(player_n, other_player):
    steps_after_card=0
    probability=random.randint(1,7)
    if probability<4:
        card = sqlqueries.card_sql()
        print(f"Sait yllätyskortin: {card['type']}")
        print_slow(Fore.GREEN + card['flavour_text'] + Style.RESET_ALL)
        if card['effect'] == 1:
            sqlqueries.effect_skip_turn_update(1, other_player)
            steps_after_card=0

        elif card['effect'] == 2:
            sqlqueries.effect_skip_turn_update(1, player_n)
            steps_after_card=0

        elif card['effect'] == 3:
            steps_after_card=-3

        elif card['effect'] == 4:
            steps_after_card=3

    else:
        steps_after_card=0
        print("Et saanut kentältä yllätyskorttia.")
    return steps_after_card

