import card
import functions
import sqlqueries
import intro
from colorama import Fore, Style

#ASCII art by figlet
print(Fore.CYAN + """
█████                            █████                                ████   ███ 
░░███                            ░░███                                 ░░███  ░░░  
 ░███         ██████  ████████   ███████    ██████  ████████   ██████  ░███  ████ 
 ░███        ███░░███░░███░░███ ░░░███░    ███░░███░░███░░███ ███░░███ ░███ ░░███ 
 ░███       ░███████  ░███ ░███   ░███    ░███ ░███ ░███ ░███░███████  ░███  ░███ 
 ░███      █░███░░░   ░███ ░███   ░███ ███░███ ░███ ░███ ░███░███░░░   ░███  ░███ 
 ███████████░░██████  ████ █████  ░░█████ ░░██████  ░███████ ░░██████  █████ █████
░░░░░░░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░   ░░░░░░   ░███░░░   ░░░░░░  ░░░░░ ░░░░░ 
                                                    ░███                          
                                                    █████                         
                                                   ░░░░░                          """ + Style.RESET_ALL)


print("Ökyrikas ja Rutikuiva")
see_intro = input("Haluatko lukea intro-tekstin? K / E : ").upper()
if see_intro == "K":
    intro.intro()


begin_game = input("Haluatko aloittaa pelin? K / E : ").upper()
while begin_game != "K" and begin_game != "E":
    begin_game = input("Haluatko aloittaa pelin? K / E : ").upper()
if begin_game == "E":
    print("Et halunnut pelata peliä.")
else:
    print("Peli alkaa! ")

    instructions="Suoraan peliin (PELI) vai toiminto- ohjeet (OHJE) tai poistaa edelliset pelaajat (POISTA) tai hakea vanhat pelit (NOUDA): "
    see_instructions = input(instructions).upper()
    while True:
        if see_instructions == "PELI":
            print("Siirrytään suoraan peliin!")
            break
        elif see_instructions == "POISTA":
            sqlqueries.remove_players()
        elif see_instructions == "NOUDA":
            nouda = sqlqueries.nouda()
            for x in nouda:
                print(x)
        elif see_instructions == "OHJE":
            functions.instructions()
        see_instructions = input(instructions).upper()

    player_1 = input("Pelaaja nro 1 nimi: ")
    while sqlqueries.player_check(player_1):
        player_1 = input("Tämä nimi on jo käytössä. Anna uusi pelaaja nro 1 nimi: ")
    else:
        sqlqueries.player_register(player_1)

    player_2 = input("Pelaaja nro 2 nimi: ")
    while sqlqueries.player_check(player_2):
        player_2 = input("Tämä nimi on jo käytössä. Anna uusi pelaaja nro 2 nimi: ")
    else:
        sqlqueries.player_register(player_2)

    game = functions.create_gameboard()
    print("Tässä pelissä pelikenttä on seuraavanlainen:")
    for item in game:
        print(item)

    print(f"Pelaajia on kaksi. Pelaajat {player_1} ja {player_2}.\n")

    visited_continents_p1 = []
    visited_continents_p2 = []
    location_p1 = location_p2 = 0
    location = [0, 0]

    print(f"Pelaaja: {player_1}\nLentokenttä: {game[location_p1]['airport name']}\nMaa: {game[location_p1]['country name']}\nMaanosa: {game[location_p1]['continent']}\n\n")
    print(f"Pelaaja: {player_2}\nLentokenttä: {game[location_p2]['airport name']}\nMaa: {game[location_p2]['country name']}\nMaanosa: {game[location_p2]['continent']}\n\n")


    def game_turn(player, visited_continents, other_player, id):
        global continue_game
        effect = sqlqueries.get_effect_skip_turn(player)['effect_skip_turns']
        if effect > 0:
            print(f"Pelaaja {player}: Olet menettänyt vuoron. Et saa heittää noppaa.")
            sqlqueries.effect_skip_turn_update(-1, player)
        else:
            steps_player = functions.game_progress(player)
            if steps_player == None:
                print("Oho, noin ei saa tehä. Menetät vuoron! :)")
            else:
                location[id] += steps_player

                if steps_player < 0:
                    print(f"Pelaaja {player} haluaa lopettaa pelin.")
                    continue_game = False
                elif location[id] >= 43:
                    print(f"{player} on saapunut maaliin: Lentokenttä: {game[43]['airport name']}\nMaa: {game[43]['country name']}\nMaanosa: {game[43]['continent']}")
                    functions.win_game(player, other_player)
                    continue_game = False
                else:
                    print(f"{player} saapui lentokentälle {game[location[id]]['airport name']}, joka on maassa {game[location[id]]['country name']} ja maanosassa {game[location[id]]['continent']}.")
                    points = card.co_card(player)

                    surprise_card = card.card_on_airport(player, other_player)
                    if surprise_card == 3:
                        location[id] += 3
                        print(f"{player} siirtyi kolme askelta eteenpäin.")
                        print(
                            f"{player} saapui lentokentälle {game[location[id]]['airport name']}, joka on maassa {game[location[id]]['country name']} ja maanosassa {game[location[id]]['continent']}.")
                    elif surprise_card == -3:
                        location[id] -= 3
                        print(
                            f"{player} siirtyi kolme askelta taaksepäin.")
                        print(
                            f"{player} saapui lentokentälle {game[location[id]]['airport name']}, joka on maassa {game[location[id]]['country name']} ja maanosassa {game[location[id]]['continent']}.")

                    if game[location[id]]['continent'] not in visited_continents:
                        visited_continents.append(game[location[id]]['continent'])
                        print(f"{player} on käynyt seuraavissa maanosissa: {visited_continents}.")
                    else:
                        print(f"{player} on käynyt seuraavissa maanosissa: {visited_continents}.")
                    functions.end_of_turn(points, player, other_player)
        print(Fore.CYAN + """
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
        """ + Style.RESET_ALL)


    continue_game = True
    while continue_game:
        game_turn(player_1, visited_continents_p1, player_2, 0)
        if continue_game:
            game_turn(player_2, visited_continents_p2, player_1, 1)