from flask import Flask, Response
import database
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
            new_index = player_index + dice
        elif player_index >= len(self.game.board):
            new_index = 43
        new_location = self.game.board[new_index]
        new_icao = list(new_location.values())[0]
        sql = f"UPDATE game SET location = '{new_icao}' WHERE player_name = '{self.player_name}'"
        cursor = database.connection.cursor()
        cursor.execute(sql)
        database.connection.commit()
        return new_location

    def get_effect(self):
        sql = f"""SELECT effect_skip_turns FROM game_player WHERE player_name = "{self.player_name}" """
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
        return result #Return muodossa {"score": 0}

    def update_score(self, points):
        sql = f"""UPDATE game SET score = score + {points} WHERE player_name = "{self.player_name}" """
        cursor = database.connection.cursor()
        cursor.execute(sql)
        database.connection.commit()
        sql_updated = (f"""SELECT score FROM game WHERE player_name = "{self.player_name}" """)
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql_updated)
        updated_score = cursor.fetchone()
        return updated_score #Tämä return { "score": 60 }


@app.route('/move_player/<player_name>/<int:dice>')
def change_location(player_name, dice):
    try:
        app_player = Player(player_name)
        result = app_player.move_player(dice)
        jsonresult = json.dumps(result)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

@app.route('/effect/<player_name>/')
def player_effect(player_name):
    try:
        app_player = Player(player_name)
        result = app_player.get_effect()
        jsonresult = json.dumps(result)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

@app.route('/effect_update/<player_name>/<int:effect>')
def player_effect_update(player_name, effect):
    try:
        app_player = Player(player_name)
        result = app_player.effect_skip_turn_update(effect)
        jsonresult = json.dumps(result)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}


@app.route('/score/<player_name>')
def player_score(player_name):
    try:
        app_player = Player(player_name)
        result = app_player.get_score()
        jsonresult = json.dumps(result)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

@app.route('/score_update/<player_name>/<int:points>')
def player_score_update(player_name, points):
    try:
        app_player = Player(player_name)
        result = app_player.update_score(points)
        jsonresult = json.dumps(result)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
