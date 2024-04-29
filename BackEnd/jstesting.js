'use strict';

async function startGame(player1, player2){
  try {
    const response = await fetch(`http://127.0.0.1:3000/start_game/${player1}/${player2}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function getScore(player_name) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/score/${player_name}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function updateScore(player_name, points) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/score_update/${player_name}/${points}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function getEffect(player_name) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/effect/${player_name}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function updateEffect(player_name, effect) {
  try {
    const response = await fetch(`http://127.0.0.1:3000/effect_update/${player_name}/${effect}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function movePlayer(player_name, dice){
  try {
    const response = await fetch(`http://127.0.0.1:3000/move_player/${player_name}/${dice}`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function getCoCard(){
  try {
    const response = await fetch(`http://127.0.0.1:3000/get_co_card`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

async function getSurpriseCard(){
  try {
    const response = await fetch(`http://127.0.0.1:3000/get_surprise_card`);
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error);
  }
}

//startGame("Vika", "Testi") // Konsolissa: {gameid: '29', player1: 'Vika', player2: 'Testi'}

//getEffect("Nea") // Konsolissa: {effect_skip_turns: 0}
//updateEffect("Nea", 1) // Konsolissa: {message: 'odotusarvo päivitetty'}

// getScore("Nea"); //Tämän hetkinen score konsolissa: {score: 250}
// updateScore("Nea", 40) //Uusi score konsolissa: {score: 290}

// movePlayer("Nea", 3) // uusi paikka konsolissa: {space29: 'HDAM'}

// getCoCard() // Konsolissa:
// {ID: 13, type: 'Hiilidioksidikortti', flavour_text: 'PR- tiimisi kehottaa sinua parantamaan julkista im…keskelle\nmoottoritietä, joka johtaa hiilinieluun.', effect: 0, score: -30}

//getSurpriseCard() // Konsolissa:
//{ID: 7, type: 'Onnenpekka', flavour_text: 'Imperiumi kasvaa: Hyviä uutisia bisnesmaailmasta! …aavaan kohteeseen. Etene kolme kenttää eteenpäin.', effect: 4, score: 0}
