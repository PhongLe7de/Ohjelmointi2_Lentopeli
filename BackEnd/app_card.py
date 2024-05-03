from flask import Flask, Response
import database
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
def surprise_card():
    card_sql = """SELECT * from cards WHERE type='Sabotaasi' or type='Huonoa tuuria' or 
    type='Onnenpekka' ORDER BY RAND() LIMIT 1"""
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result
    #Tämän return muodossa:
# {
#     "ID": 10,
#     "type": "Hiilidioksidikortti",
#     "flavour_text": "Lennoistasi on aiheutunut päästöjä, joilla on vaikutus ilmastoon. Tuloksena on\npaikallinen rankkasade.",
#     "effect": 0,
#     "score": 10
# }


def co_card():
    card_sql = "SELECT * from cards WHERE type='Hiilidioksidikortti' ORDER BY RAND() LIMIT 1"
    cursor = database.connection.cursor(dictionary=True)
    cursor.execute(card_sql)
    result = cursor.fetchone()
    return result
    #Tämän return muodossa:
    # {
    #     "ID": 12,
    #     "type": "Hiilidioksidikortti",
    #     "flavour_text": "Lennoistasi on aiheutunut päästöjä, joilla on vaikutus ilmastoon. Tuloksena on\npaikallinen hurrikaani. Lennot perutaan. Joudut odottamaan vuoron verran sään\nlaantumista jatkaaksesi",
    #     "effect": 2,
    #     "score": 50
    # }

# @app.route('/get_co_card')
# def player_co_card():
#     try:
#         co = co_card()
#         jsonresult = json.dumps(co)
#         return Response(response=jsonresult, mimetype="application/json")
#     except:
#         return {"Error": "Invalid parameters", "Status": 400}

# @app.route('/get_surprise_card')
# def player_surprise_card():
#     try:
#         surprise = surprise_card()
#         jsonresult = json.dumps(surprise)
#         return Response(response=jsonresult, mimetype="application/json")
#     except:
#         return {"Error": "Invalid parameters", "Status": 400}


# if __name__ == "__main__":
#     app.run(use_reloader=True, host='127.0.0.1', port=3000)