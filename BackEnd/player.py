import database

game_spaces = ['space1', 'space2', 'space3', 'space4', 'space5', 'space6', 'space7', 'space8', 'space9', 'space10',
               'space11', 'space12', 'space13', 'space14', 'space15', 'space16', 'space17', 'space18', 'space19',
               'space20', 'space21', 'space22', 'space23', 'space24', 'space25', 'space26', 'space27', 'space28',
               'space29', 'space30', 'space31', 'space32', 'space33', 'space34', 'space35', 'space36', 'space37',
               'space38', 'space39', 'space40', 'space41', 'space42', 'space43', 'space44']
class Player:
    def __init__(self, name, gameid):
        self.name = name
        self.gameid = gameid

    def player_location(self):
        sql = f"""
        SELECT location from game WHERE player_name='{self.name}'
        """
        cursor = database.connection.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result #Tämän tulos {'location':'ICAO'}

    def player_space(self, ICAO):
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
            new_location_sql = f"""SELECT {game_spaces[new_index]} FROM gameboard WHERE id ='{self.gameid}'"""
            cursor = database.connection.cursor()
            cursor.execute(new_location_sql)
            result = cursor.fetchone()
            print(result[0])
            sql = f"""UPDATE game SET location = '{result[0]}' WHERE player_name = '{self.name}' """
            cursor = database.connection.cursor()
            cursor.execute(sql)
            database.connection.commit()
            print("Tulos päivitetty")
        else:
            new_index = 43
        return game_spaces[new_index]

player = Player('Ida', 2)
print(player.player_location())
# location = player.player_location()
#print(player.player_space('OBBI'))
print(player.player_move(4))
print(player.player_location())
