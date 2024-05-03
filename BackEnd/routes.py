
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from app_card import co_card, surprise_card
from app_moveplayer import Player, player_mainland, player_space
from app_gameboard_Phong import check_player, register_player, initialize, game_board
import json
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/move_player/', methods=['POST'])
@cross_origin(origin='*')
def change_location():
    print('ok')
    response = request.json
    print(response )
    player_name = response['data']['currentPlayer']
    dice = response['data']['value']
    try:
        app_player = Player(player_name)
        get_score = app_player.get_score()

        ident = app_player.move_player(dice)
        keys = ident.keys()
        spaceKeys = list(keys)
        spaceKey = spaceKeys[0]
        
        co = co_card()

        random_card = random.randint(0,1)
        if random_card == 1 :
            surprise = surprise_card()
        else:
            surprise = {
                "ID": 0,
                "type": "null",
                "flavour_text": "null",
                "effect": 0,
                "score": 0
            }

        effects = co['effect'] + surprise['effect']
        scores = co['score'] + surprise['score']
        updateScore = app_player.update_score(scores)

        updateEffect = app_player.effect_skip_turn_update(effects)
        getEffect = app_player.get_effect()
        


        space = player_mainland(ident[spaceKey])

        result = {
            'Player':player_name,
            'initial_score': get_score,
            'ident': ident,
            'update_score': updateScore,
            'co_card':co,
            'surprise_card': surprise,
            'final_effect_value': effects,
            'get_effect': getEffect,
            'updata_effect': updateEffect,
            'space': space
        }

        return result
    except:
        return {"Error": "Invalid parameters", "Status": 400}

@app.route('/effect/', methods=['POST'])
@cross_origin(origin='*')
def player_effect():
    try:
        response = request.json
        player_name = response['data']['currentPlayer']
        print(player_name)
        app_player = Player(player_name)
        print(app_player)
        result = app_player.get_effect()
        
        return result
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

@app.route('/start_game/' ,methods=['POST'])
@cross_origin(origin='*')
def start():
    try:
        response = request.json
        player1_name=response['data']['player1_name']
        player2_name=response['data']['player2_name']

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

@app.route('/gameboard/', methods=['POST'])
@cross_origin(origin='*')

def get_gameboard():
    try:
        response = request.json
        print(response)
        id = response['id']
        result = game_board(id)
        print(result)
        return result
    except:
        return {"Error": "Invalid parameters", "Status": 400}
    
@app.route('/get_co_card')
@cross_origin(origin='*')

def player_co_card():
    try:
        co = co_card()
        jsonresult = json.dumps(co)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

@app.route('/get_surprise_card')
@cross_origin(origin='*')

def player_surprise_card():
    try:
        surprise = surprise_card()
        jsonresult = json.dumps(surprise)
        return Response(response=jsonresult, mimetype="application/json")
    except:
        return {"Error": "Invalid parameters", "Status": 400}

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)