const player1 = document.getElementById('player-1-name')
const player2 = document.getElementById('player-2-name')
const btnSubmit = document.querySelector('input[type=submit]')


const playerName = {
}
btnSubmit.addEventListener('click',(e)=>{
  e.preventDefault()
  playerName.player1 = player1.value
  playerName.player2 = player2.value
})

console.log(playerName);

const getDicePopUpElement = document.getElementById('modal-dice')
const playerWhoPlay = 2;
const handleDiceRolling = (player) => {
  const checkClass = getDicePopUpElement.classList
  if (checkClass[0] === 'open'){
    const randomDiceValue = Math.floor(Math.random() * 6 + 1);
    const randomDiceImg = (player == 1
      ? "diceRed" + randomDiceValue + ".png"
      : "diceBlue" + randomDiceValue + ".png");
    const getDiceImgElement = document.querySelector(".dice-img");
    getDiceImgElement.src = `assets/img/dice/${randomDiceImg}`

    data = {
      player: playerWhoPlay,
      value: randomDiceValue
    }
    const URL = `http://localhost:3000/start_game/`; 
    updateData(URL, player, data)
  } else{
    console.log('window is not open');
  }
};
const getRollfeature = document.querySelector('.roll-feature')
const a = getRollfeature.addEventListener('click',()=>{handleDiceRolling(player)})

const updateData = async (URL, player,data) => {
    console.log(data);
    try {
      const response = await fetch(URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({player, data }),
      });
  
      if (response.ok) {
        console.log(response);
        console.log("update success");
      } else {
        console.log("update fail");
      }
    } catch (error) {
      console.log(error);
    }
};
