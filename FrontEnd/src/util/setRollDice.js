const getDicePopUpElement = document.getElementById('modal-dice')
const getRollfeature = document.querySelector('.roll-feature')

getRollfeature.addEventListener('click', () => { handleDiceRolling(currentPlayer) })
let currentPlayer = 0;
let skipTurns;

let player01Data = {
  mainland: [],
  score: 0,
  effect: 0
}

let player02Data = {
  mainland: [],
  score: 0,
  effect: 0
}

const handleDiceRolling = async (player) => {
  const getPlayernameElement = document.querySelector('.player-dice-rolling')
  const player01 = document.getElementById('player-1-name')
  const player02 = document.getElementById('player-2-name')
  const listPlayer = [player01.value, player02.value]
  getPlayernameElement.innerHTML = `${listPlayer[currentPlayer]}`
  const checkClass = getDicePopUpElement.classList
  let playerSkipTurns

  if (checkClass[0] === 'open') {

    playerSkipTurns = currentPlayer === 0 ? player01Data.effect : player02Data.effect;
    console.log(listPlayer[currentPlayer]);
    console.log('start', playerSkipTurns);
    console.log(listPlayer[1])
    if (playerSkipTurns > 0) {
      if (currentPlayer === 0) {
        data = {
          currentPlayer: listPlayer[currentPlayer],
          value: -1,
        };
        skipTurns = await handleSkipTurns(data);
        console.log(skipTurns);
        player01Data.effect = skipTurns['effect_skip_turns'];
      } else {
        data = {
          currentPlayer: listPlayer[1],
          value: -1,
        };
        skipTurns = await handleSkipTurns(data);
        console.log(skipTurns);
        player02Data.effect = skipTurns['effect_skip_turns'];
      }
    }
    else {
      const randomDiceValue = Math.floor(Math.random() * 6 + 1);
      const randomDiceImg = (player === 0
          ? "diceRed" + randomDiceValue + ".png"
          : "diceBlue" + randomDiceValue + ".png");
      const getDiceImgElement = document.querySelector(".dice-img");
      getDiceImgElement.src = `assets/img/dice/${randomDiceImg}`

      data = {
        currentPlayer: listPlayer[currentPlayer],
        value: randomDiceValue
      }
      const response = await handlePostData(data)
      console.log(response)
      console.log(response.Player)
      console.log(response.space)

      movePlayerMarker(response.Player, response.space);
      const playerData = {
        icao: response['ident'],
        score: response['update_score']['score'],
        co_effect: response['co_effect'],
        surprise_effect: response['surprise_effect'],
        // effect: response['final_effect_value']['effect_skip_turns'],
        mainland: response['space']['continent'],
        co2: response['co_card'],
        surprise: response['surprise_card']
      }
      console.log(playerData);



      const playerMainland = playerData.mainland
      if (currentPlayer === 0) {
        player01Data.score = playerData.score
        switch (playerData.surprise_effect) {
          case 1:
            data = {
              currentPlayer: listPlayer[1],
              value: 1
            }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player02Data.effect = skipTurns['effect_skip_turns']
            // player02Data.effect++;
            break;
          case 2:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: 1
            }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player01Data.effect = skipTurns['effect_skip_turns']
            break;
          case 3:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: -3
            }
            const back = await handlePostData(data)
            console.log(back)
            break;
          case 4:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: 3
            }
            const forward = await handlePostData(data)
            console.log(forward)
            break;
          default:
            // Handle other cases if needed
            break;
        }
        switch (playerData.co_effect) {
          case 1:
            data = {
              currentPlayer: listPlayer[0],
              value: 1
            }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player02Data.effect = skipTurns['effect_skip_turns']
            break;
          case 2:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: 1
            }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player01Data.effect = skipTurns['effect_skip_turns']
            break;
          case 3:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: -3
            }
            const back = await handlePostData(data)
            console.log(back)
            break;
          case 4:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: 3
            }
            const forward = await handlePostData(data)
            console.log(forward)
            break;
          default:
            // Handle other cases if needed
            break;
        }
        const checkFunction = player01Data.mainland.includes(playerMainland)
        if (checkFunction === false) {
          player01Data.mainland.push(playerMainland)
        }

      } else {
        player02Data.score = playerData.score
        console.log(playerData.surprise_effect)
        switch (playerData.surprise_effect) {
          case 1:
            data = {
              currentPlayer: listPlayer[0],
              value: 1
            }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player01Data.effect = skipTurns['effect_skip_turns']
            break;
          case 2:
            data = {
              currentPlayer: listPlayer[1],
              value: 1
            }
            console.log(listPlayer[1])
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player02Data.effect = skipTurns['effect_skip_turns']
            break;
          case 3:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: -3
            }
            const back = await handlePostData(data)
            console.log(back)
              //KORJAA TÄMÄ SAATANA
            break;
          case 4:
            data = {
              currentPlayer: listPlayer[currentPlayer],
              value: 3
            }
            const forward = await handlePostData(data)
            console.log(forward)
            break;
          default:
            // Handle other cases if needed
            break;
        }
      switch (playerData.co_effect) {
        case 1:
          data = {
            currentPlayer: listPlayer[0],
            value: 1
          }
          skipTurns = await handleSkipTurns(data)
          console.log(skipTurns)
          player01Data.effect = skipTurns['effect_skip_turns']
          break;
        case 2:
          data = {
            currentPlayer: listPlayer[1],
            value: 1
          }
            skipTurns = await handleSkipTurns(data)
            console.log(skipTurns)
            player02Data.effect = skipTurns['effect_skip_turns']
          break;
        case 3:
          data = {
            currentPlayer: listPlayer[currentPlayer],
            value: -3
          }
          const back = await handlePostData(data)
          console.log(back)
          break;
        case 4:
          data = {
            currentPlayer: listPlayer[currentPlayer],
            value: 3
          }
          const forward = await handlePostData(data)
          console.log(forward)
          break;
        default:
          // Handle other cases if needed
          break;
      }
        const checkFunction = player02Data.mainland.includes(playerMainland)
        if (checkFunction === false) { player02Data.mainland.push(playerMainland) }
      }

    }
    //Stamp
    const mainlandStampsP1 = document.getElementById('passport-1')
    const mainlandStampsP2 = document.getElementById('passport-2')

    player01Data.mainland.forEach(item => {
      const getmainland = mainlandStampsP1.getElementsByClassName(`${item}-stamp`)
      if (getmainland) {
        getmainland[0].src = `assets/leimat/${item}_saavutettu.png`
        if (getmainland[6]){
          alert("WINNER")
        }
      } else {
        console.log('mainland not found');
      }
    })

    player02Data.mainland.forEach(item => {
      const getmainland = mainlandStampsP2.getElementsByClassName(`${item}-stamp`)
      if (getmainland) {
        getmainland[0].src = `assets/leimat/${item}_saavutettu.png`
        if (getmainland[6]){
          alert("WINNER")
        }
      } else {
        console.log('mainland not found');
      }
    })
    console.log(player01Data.score);
    //score
    const scoreP1 = document.getElementById('p1-points')
    const scoreP2 = document.getElementById('p2-points')
    scoreP1.innerHTML = `${player01Data.score}`
    scoreP2.innerHTML = `${player02Data.score}`

    //effect p1-wait
    const waitP1 = document.getElementById('p1-wait')
    const waitP2 = document.getElementById('p2-wait')

    waitP1.innerHTML = `${player01Data.effect}`
    waitP2.innerHTML = `${player02Data.effect}`


    console.log('1 after', player01Data.effect);
    console.log('2 after', player02Data.effect);

    if(player01Data.mainland.length === 3){
      whoWins1();
    }
    else if(player02Data.mainland.length === 3){
      whoWins2();
    }


    currentPlayer = currentPlayer === 0 ? 1 : 0

  } else {
    console.log('window is not open');
  }
};


const handlePostData = async (data) => {
  try {
    const response = await fetch('http://localhost:3000/move_player/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data })
    });
    if (response.ok) {
      result = await response.json()
      console.log("update success");
      return result
    } else {
      console.log("update fail");
    }
  } catch (error) {
    console.log(error);
  }
};

const handleSkipTurns = async function updateEffect(data) {
  try {
    const response = await fetch('http://127.0.0.1:3000/effect_update/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data })
    });
    if (response.ok) {
      result = await response.json()
      console.log("update success");
      return result
    } else {
      console.log("update fail");
    }
  } catch (error) {
    console.log(error);
  }
};

