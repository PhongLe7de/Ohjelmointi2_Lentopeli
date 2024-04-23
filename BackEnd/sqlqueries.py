import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)
def airport1():
    sql_airport1 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', country.continent FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country
    WHERE airport.name like "%Svalbard%";""")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_airport1)
    start = cursor.fetchone()
    return start

#Seuraavasta Venäjä pois lähinnä koska se on sekä EU että AS
def airport2(item):
    sql_airport2 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', country.continent FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country 
    WHERE airport.continent='{item}' and type='large_airport' and country.name!='Russia'
    GROUP BY country.name ORDER BY RAND() LIMIT 7;""")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_airport2)
    result = cursor.fetchall()
    return result
def airport3():
    sql_airport3 = (f"""SELECT airport.name as 'airport name', country.name as 'country name', country.continent FROM airport 
    INNER JOIN country ON airport.iso_country=country.iso_country 
    WHERE airport.continent='AN' and type='medium_airport' 
    ORDER BY RAND() LIMIT 1;""")
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_airport3)
    end = cursor.fetchone()
    return end


def player_register(player_n):
    sql_player_register = f"""INSERT INTO game_player (player_name) VALUES ('{player_n}');"""
    cursor = connection.cursor()
    cursor.execute(sql_player_register)


def  player_check(player_n):
    sql_player_check = f"""SELECT player_name FROM game_player WHERE player_name='{player_n}';"""
    cursor = connection.cursor()
    cursor.execute(sql_player_check)
    return cursor.fetchall()


def get_score(player_n):
    sql_update_score = (f"""SELECT score FROM game_player WHERE player_name = "{player_n}" """)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_update_score)
    result = cursor.fetchone()
    return result


def update_score(points, player_n):
    sql_update_score = f"""UPDATE game_player SET score = score + {points} WHERE player_name = "{player_n}" """
    cursor = connection.cursor()
    cursor.execute(sql_update_score)
    connection.commit()


def get_effect_skip_turn(player_n):
    sql_get_effect = f"""SELECT effect_skip_turns FROM game_player WHERE player_name = "{player_n}" """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_get_effect)
    skip_turn = cursor.fetchone()
    return skip_turn


def effect_skip_turn_update(effect, player_n):
    sql_skip_turn = f"""UPDATE game_player SET effect_skip_turns = effect_skip_turns + {effect} WHERE game_player.player_name = '{player_n}' """
    cursor = connection.cursor()
    cursor.execute(sql_skip_turn)
    connection.commit()


def card_sql():
    card_sql = '''SELECT * from cards WHERE type='Sabotaasi' or type='Huonoa tuuria' or 
    type='Onnenpekka' ORDER BY RAND() LIMIT 1'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result


def co_card_sql():
    card_sql = '''SELECT * from cards WHERE type='Hiilidioksidikortti' ORDER BY RAND() LIMIT 1'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result


def remove_players():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''DELETE FROM game_player''')

def nouda():
    card_sql = '''SELECT player_name, score, victory from game_player'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchall()
    return result

def victory(voittaja):
    cursor = connection.cursor()
    cursor.execute(f'''UPDATE game_player SET victory=1 WHERE player_name = "{voittaja}"''')