
import database


def surprise_card():
    card_sql = """SELECT * from cards WHERE type='Sabotaasi' or type='Huonoa tuuria' or
    type='Onnenpekka' ORDER BY RAND() LIMIT 1"""
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result


def co_card():
    card_sql = "SELECT * from cards WHERE type='Hiilidioksidikortti' ORDER BY RAND() LIMIT 1"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result
