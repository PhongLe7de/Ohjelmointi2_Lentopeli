
import airports
import database

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

def airport_icao(icao):
    sql = f"SELECT airport.ident, airport.latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{icao}'"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def game_board(gameid):
    sql = f"SELECT * FROM gameboard WHERE id={gameid}"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql)
    board = cursor.fetchone()
    space_list = [f"space{i}" for i in range(1, 45)]
    icao_list = []
    for key, value in board.items():
        if key.startswith('space'):
            icao_list.append(value)
    airport_list = []
    for icao in icao_list:
        airport_list.append(airport_icao(icao))
    return airport_list


def check_player(player_name):
    sql_player_check = f"SELECT player_name FROM game WHERE player_name='{player_name}';"
    cursor = database.connection.cursor()
    cursor.execute(sql_player_check)
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def register_player(player_name, gameid):
    sql_player_register = f"INSERT INTO game (gameid, player_name, location) VALUES ({gameid}, '{player_name}', 'ENSB');"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql_player_register)
    database.connection.commit()

def game_score():
    sql_game = f"SELECT * from game"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(sql_game)
    result = cursor.fetchall()
    return result



