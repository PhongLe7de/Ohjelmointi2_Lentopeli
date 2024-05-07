'use strict'

async function gameScores() {
  try {
    const response = await fetch(`http://127.0.0.1:3000/gamescores`);
    const jsonData = await response.json();
    console.log(jsonData);
    return jsonData
  } catch (error) {
    console.log(error);
  }
}

async function displayGameList() {
  const gameData = await gameScores();

  console.log(gameData[1]);
  gameData.map((player) => {
    console.log(player)
    const gameList = document.getElementById('game-list');
    const createElement = document.createElement('li')
    const playerName = document.createTextNode(`Pelaajan nimi: ${player.player_name}  Pelaajan pisteet: ${player.score}`)
    console.log(playerName)
    createElement.appendChild(playerName)
    gameList.appendChild(createElement)

  });
}

displayGameList()