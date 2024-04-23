import sqlqueries
import random
from colorama import Fore, Style


def instructions():
    print(Fore.BLUE + "NOPPA :", Fore.YELLOW + "Paina <ENTER>")
    print(Fore.BLUE + "PELIN TOIMINNOT :", Fore.YELLOW + "kirjoita 'OHJE'")
    print(Fore.BLUE + "LOPETA :", Fore.YELLOW + "kirjoita 'LOPETA'")
    print(Fore.BLUE + "Ohjeet saa aina näkyville, jos kirjoittaa 'OHJE'")
    print(Style.RESET_ALL)


def create_gameboard():
    board = []
    sql_start=sqlqueries.airport1() #Svalbard eka ruutu
    board.append(sql_start)

    continents=['EU','AS','OC','AF', 'NA', 'SA'] #Yksi kenttä/maa
    continents_airports=[]
    for item in continents:
        sql_continents = sqlqueries.airport2(item)
        continents_airports.append(sql_continents)
    #Jotta maanosat ei ole omissa listoissaan, purku:
    for continent in continents_airports:
        for airport in continent:
            board.append(airport)

    sql_end = sqlqueries.airport3() #Maali Antarcticassa
    board.append(sql_end)

    return board


def game_progress(player_n):
    roll_dice=None
    print(f"Pelaaja {player_n}")
    want_to_play = input("Haluatko heittää noppaa? ").upper()
    if want_to_play == "":
        roll_dice = random.randint(1, 6)
        print(Fore.BLUE + f"Nopan arvo: {roll_dice}" + Style.RESET_ALL)
    elif want_to_play == "LOPETA":
        roll_dice = -1
    elif want_to_play == "OHJE":
        print(Fore.BLUE + "NOPPA :", Fore.YELLOW + "Paina <ENTER>")
        print(Fore.BLUE + "PELIN TOIMINNOT :", Fore.YELLOW + "kirjoita 'OHJE'")
        print(Fore.BLUE + "LOPETA :", Fore.YELLOW + "kirjoita 'LOPETA'")
        print(Fore.BLUE + "Ohjeet saa aina näkyville, jos hakukenttään kirjoittaa 'OHJE'")
        print(Style.RESET_ALL)

        want_to_play = input("Haluatko heittää noppaa? ").upper()
        if want_to_play =="":
            roll_dice = random.randint(1, 6)
            print(f"Nopan arvo: {roll_dice}")
        elif want_to_play == "LOPETA":
            roll_dice = -1
    return roll_dice


def end_of_turn(score, player_n, other_player):
    sqlqueries.update_score(score, player_n)
    total_score = sqlqueries.get_score(player_n)
    if total_score['score'] > 0 :
        print(Fore.RED + f"Pelaajalla {player_n} on nyt {total_score['score']} Ökyrikas-pistettä!\n" + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + f"Pelaajalla {player_n} on nyt {total_score['score']} Ökyrikas-pistettä!\n" + Style.RESET_ALL)
    total_skips_p1 = sqlqueries.get_effect_skip_turn(player_n)
    total_skips_p2 = sqlqueries.get_effect_skip_turn(other_player)
    if total_skips_p1['effect_skip_turns'] > 0:
        print(f"Pelaajalla {player_n} on nyt {total_skips_p1['effect_skip_turns']} vuoron odotusta.\n")
    if total_skips_p2['effect_skip_turns']> 0:
        print(f"Pelaajalla {other_player} on nyt {total_skips_p2['effect_skip_turns']} vuoron odotusta.\n")



def win_game(player_n, other_player):
    sqlqueries.victory(player_n)
    total_score_player_n = sqlqueries.get_score(player_n)
    total_score_other_player = sqlqueries.get_score(other_player)
    print(f"Pelaaja {player_n} on voittanut pelin ja päässyt ainoana perille Etelänavalle! Hän on Rutikuiva!")
    print(f"Pelaaja {player_n} keräsi {total_score_player_n['score']} Ökypistettä.")
    print(f"Pelaaja {other_player} keräsi {total_score_other_player['score']} Ökypistettä.")
    if total_score_player_n['score'] > total_score_other_player['score']:
        print(f"Pelaaja {player_n} on kerännyt enemmän Ökypisteitä. Hän on Ylivoimainen Mestari päästessään ensimmäisenä Etelänavalle ja kerätessään eniten Ökypisteitä.")
    if total_score_other_player['score'] > total_score_player_n['score']:
        print(f"Pelaaja {other_player} on kerännyt enemmän Ökypisteitä kuin maaliin päässyt {player_n}. Hän on Upporikas!")