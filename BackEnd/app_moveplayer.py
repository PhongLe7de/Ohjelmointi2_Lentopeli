
from app_card import co_card, surprise_card
from app_gameboard_Phong import check_player, game_board, initialize, register_player
import database

game_spaces = [f"space{i}" for i in range(1, 45)]

def player_location(player_name):
    sql = f"SELECT location from game WHERE player_name='{player_name}'"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def player_mainland(ICAO):
    sql = f"SELECT continent, latitude_deg, longitude_deg from airport WHERE ident='{ICAO}'"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def player_space(player_name, ICAO):
    for i in range(len(game_spaces)):
        space = game_spaces[i]
        sql = f"SELECT * from gameboard WHERE {space} = '{ICAO}'"
        cursor = database.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0:
            print(f"The value {ICAO} was found in the column {space}.")
            result = space
            break
    else:
        result = None
        print(f"The value {ICAO} was not found in any of the columns.")
    return result


class Game:
    def __init__(self, gameid):
        game_spaces = [f"space{i}" for i in range(1, 45)]
        self.board = []
        for space in game_spaces:
            sql = f"SELECT {space} FROM gameboard WHERE id={gameid}"
            cursor = database.connection.cursor(dictionary=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                self.board.append(row)
    def __repr__(self):
        return f"{self.board}"

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        sql_id = f"SELECT gameid FROM game WHERE player_name='{player_name}'"
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql_id)
        id_result = cursor.fetchall()
        self.gameid = id_result[0]['gameid']
        self.game = Game(self.gameid)
        sql = f"SELECT location FROM game WHERE player_name = '{player_name}'"
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchone()
        self.location = result['location']

    def __repr__(self):
        return f"{self.player_name}, {self.gameid}, {self.location}"
    def move_player(self, dice):
        player_index = None
        for space in self.game.board:
            if list(space.values())[0] == self.location:
                player_index = self.game.board.index(space)
                break
        if player_index is not None:
            if player_index <= 2:
                if dice < 0:
                    new_index = 0
                else:
                    new_index = player_index + dice
            else:
                new_index = player_index + dice
        elif player_index >= len(self.game.board):
            new_index = 44
        new_location = self.game.board[new_index]
        new_icao = list(new_location.values())[0]
        sql = f"UPDATE game SET location = '{new_icao}' WHERE player_name = '{self.player_name}'"
        cursor = database.connection.cursor()
        cursor.execute(sql)
        database.connection.commit()
        return new_location

    def get_effect(self):
        sql = f"""SELECT effect_skip_turns FROM game WHERE game.player_name = "{self.player_name}" """
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql)
        skip_turn = cursor.fetchone()
        return skip_turn #Tämä return muodossa {"effect_skip_turns": 0}
    def effect_skip_turn_update(self, effect):
        sql_skip_turn = f"""UPDATE game SET effect_skip_turns = effect_skip_turns + {effect} WHERE game.player_name = '{self.player_name}' """
        cursor = database.connection.cursor()
        cursor.execute(sql_skip_turn)
        database.connection.commit()
        return {"message": "odotusarvo päivitetty"}

    def get_score(self):
        sql = (f"""SELECT score FROM game WHERE player_name = "{self.player_name}" """)
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def update_score(self, points):
        sql = f"""UPDATE game SET score = score + {points} WHERE player_name = "{self.player_name}" """
        cursor = database.connection.cursor()
        cursor.execute(sql)
        database.connection.commit()
        sql_updated = (f"""SELECT score FROM game WHERE player_name = "{self.player_name}" """)
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql_updated)
        updated_score = cursor.fetchone()
        return updated_score
