from flask import Flask
import airports
import database
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def insert_to_database(airports):
    space_list = [f"space{i}" for i in range(1, 45)]
    space_columns = ""
    for column_name in space_list:
        space_columns += column_name + ", "
    space_columns = space_columns[:-2]
    placeholders = ", ".join(["%s"] * 44)
    sql_insert = f"""INSERT INTO gameboard ({space_columns}) VALUES ({placeholders})"""
    values = tuple(airport['ident'] for airport in airports)
    cursor = database.connection.cursor()
    cursor.execute(sql_insert, values)
    database.connection.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    last_gameid = cursor.fetchone()[0]
    return last_gameid


def initialize():
    board = []
    sql_start = airports.airport1()  # Svalbard eka ruutu
    board.append(sql_start)
    continents = ['EU', 'AS', 'OC', 'AF', 'NA', 'SA']  # Yksi kenttä/maa
    continents_airports = []
    for item in continents:
        sql_continents = airports.airport2(item)
        continents_airports.append(sql_continents)
    # Jotta maanosat ei ole omissa listoissaan, purku:
    for continent in continents_airports:
        for airport in continent:
            board.append(airport)
    sql_end = airports.airport3()  # Maali Antarcticassa
    board.append(sql_end)
    gameid = insert_to_database(board)
    return gameid

#Kun tarvitsee pelikenttiä testaukseen:
# @app.route('/gameboard')
# def get_gameboard():
#     try:
#         result = initialize()
#         return result
#     except:
#         return {"Error": "Invalid parameters", "Status": 400}

def check_player(player_name):
    sql_player_check = f"SELECT player_name FROM game WHERE player_name='{player_name}';"
    cursor = database.connection.cursor()
    cursor.execute(sql_player_check)
    result = cursor.fetchone()
    print(result)
    print("SQL Query:", sql_player_check)
    print("Fetched Results:", result)
    if result:
        return True
    else:
        return False

def register_player(player_name, gameid):
    sql_player_register = f"INSERT INTO game (gameid, player_name, location) VALUES ({gameid}, '{player_name}', 'ENSB');"
    cursor = database.connection.cursor()
    cursor.execute(sql_player_register)
    database.connection.commit()

@app.route('/start_game/<player1_name>/<player2_name>')
def start(player1_name, player2_name):
    try:
        player1_check = check_player(player1_name)
        player2_check = check_player(player2_name)
        print(player1_check, player2_check)
        if player1_check:
            if player2_check:
                return {"status": "error", "message": "Molemmat pelaajanimet varattuja"}
            else:
                return {"status": "error", "message": f"Pelaajanimi {player1_name} on varattu"}
        elif player2_check:
            if player1_check:
                return {"status": "error", "message": "Molemmat pelaajanimet varattuja"}
            else:
                return {"status": "error", "message": f"Pelaajanimi {player2_name} on varattu"}
        else:
            gameid = initialize()
            register_player(player1_name, gameid)
            register_player(player2_name, gameid)
            return {"gameid": f'{gameid}', "player1": f'{player1_name}', "player2": f'{player2_name}'}
    except:
        return {"Error": "Invalid parameters", "Status": 400}

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


