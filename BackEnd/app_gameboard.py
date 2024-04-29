import json

from flask import Flask, Response
from flask_cors import CORS

import airports
import database

app = Flask(__name__)
cors = CORS(app)
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
    insert_to_database(board)
    return board



@app.route('/gameboard')
def gameboard():
    try:
        result = initialize()
        result_json = json.dumps(result)
        return Response(response=result_json, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
