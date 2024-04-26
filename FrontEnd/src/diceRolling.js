import axios from "axios";

const URL = ''; //waiting for URL from BackEnd
export const handleDiceRolling = (player) => {
  const player = player;
  const randomDiceValue = Math.floor(Math.random() * 6 + 1);
  const randomDiceImg = (player = 1
    ? "diceRed" + randomDiceValue + ".png"
    : "diceBlue" + randomNumber + ".png");
  const getDiceImgElement = document.getElementsByClassName("diceValueImage");
  getDiceImgElement.setAttribute("scr", `assets/img/dice/${randomDiceImg}`);
  return randomDiceValue;
};

const handleShowDicePopUp = () =>{
  const getDicePopUpElement = document.getElementById('modal-dice')
  getDicePopUpElement.classList.add('open')
}

const handleCloseDicePopUp = () =>{
  const getDicePopUpElement = document.getElementById('modal-dice')
  getDicePopUpElement.classList.add('close')
}

const getDiceBtn = document.getElementById('btn-dice')
getDiceBtn.addEventListener('click',handleShowDicePopUp)

// const popUpRollWindow = ()


