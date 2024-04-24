import database

import airports

class GameBoard:

    def __init__(self):
        self.board = []
        self.initialize()

    def initialize(self):
        sql_start = airports.airport1()  # Svalbard eka ruutu
        self.board.append(sql_start)
        continents = ['EU', 'AS', 'OC', 'AF', 'NA', 'SA']  # Yksi kenttä/maa
        continents_airports = []
        for item in continents:
            sql_continents = airports.airport2(item)
            continents_airports.append(sql_continents)
        # Jotta maanosat ei ole omissa listoissaan, purku:
        for continent in continents_airports:
            for airport in continent:
                self.board.append(airport)
        sql_end = airports.airport3()  # Maali Antarcticassa
        self.board.append(sql_end)

    def insert_to_gameboard(self, airports):
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


game = GameBoard()
print(game.board)
game.insert_to_gameboard(game.board)
