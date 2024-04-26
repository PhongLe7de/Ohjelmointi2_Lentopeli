from flask import Flask
import database

app = Flask(__name__)

game_spaces = [f"space{i}" for i in range(1, 45)]

def player_location(player_name):
    sql = f"SELECT location from game WHERE player_name='{player_name}'"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result #Tämän tulos {'location':'ICAO'}

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

def player_move(self, dice,):
    location = self.player_location()
    space = self.player_space(location['location'])
    current_index = game_spaces.index(space)
    print(current_index)
    if current_index is not None and current_index < 43:
        new_index = current_index + dice
        print(game_spaces[new_index])
        new_location_sql = f"SELECT {game_spaces[new_index]} FROM gameboard WHERE id ='{self.gameid}'"
        cursor = database.connection.cursor()
        cursor.execute(new_location_sql)
        result = cursor.fetchone()
        print(result[0])
        sql = f"UPDATE game SET location = '{result[0]}' WHERE player_name = '{self.name}'"
        cursor = database.connection.cursor()
        cursor.execute(sql)
        database.connection.commit()
        print("Tulos päivitetty")
    else:
        new_index = 43
    return game_spaces[new_index]

@app.route('/player_location/<player_name>/')
def player_location(player_name):
    try:
        result = player_location(player_name)
        return result
    except:
        return {"Error": "Invalid parameters", "Status": 400}


@app.route('/move_player/<player_name>')
def move_player(player_name):
    try:
        result = move_player(player_name)
        return result
    except:
        return {"Error": "Invalid parameters", "Status": 400}

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


player_location('Nea')

