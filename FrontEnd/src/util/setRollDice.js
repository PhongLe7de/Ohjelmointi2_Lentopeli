const getDicePopUpElement = document.getElementById('modal-dice')
const getRollfeature = document.querySelector('.roll-feature')

getRollfeature.addEventListener('click', () => { handleDiceRolling(currentPlayer) })
let currentPlayer = 0;

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

    currentPlayer === 0 ? playerSkipTurns = player01Data.effect : player02Data.effect
    console.log(listPlayer[currentPlayer]);
    console.log('start', playerSkipTurns);
    if (playerSkipTurns > 0) {

      currentPlayer === 0
        ? player01Data.effect = playerSkipTurns
        : player02Data.effect = playerSkipTurns
      playerSkipTurns = playerSkipTurns - 1
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
      const response = await handlePostData(data);
      console.log(response);

      movePlayerMarker(response.Player, response.space);

      const playerData = {
        score: response['update_score']['score'],
        effect: response['get_effect']['effect_skip_turns'],
        mainland: response['space']['continent'],
        co2: response['co_card'],
        surprise: response['surprise_card']
      }
      console.log(playerData);

      const playerMainland = playerData.mainland
      if (currentPlayer === 0) {
        player01Data.score = playerData.score
        player01Data.effect = playerData.effect
        const checkFunction = player01Data.mainland.includes(playerMainland)
        if (checkFunction === false) { player01Data.mainland.push(playerMainland) }

      } else {
        player02Data.score = playerData.score
        player02Data.effect = playerData.effect
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
      } else {
        console.log('mainland not found');
      }
    })

    player02Data.mainland.forEach(item => {
      const getmainland = mainlandStampsP2.getElementsByClassName(`${item}-stamp`)
      if (getmainland) {
        getmainland[0].src = `assets/leimat/${item}_saavutettu.png`
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

