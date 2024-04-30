
// console.log('a');
// const getDicePopUpElement = document.getElementById('btn-dice-section')
// console.log(getDicePopUpElement);
const player = 2;
const handleDiceRolling = () => {
  const checkClass = getDicePopUpElement.classList
  if (checkClass[0] === 'open'){
    const randomDiceValue = Math.floor(Math.random() * 6 + 1);
    const randomDiceImg = (player == 1
      ? "diceRed" + randomDiceValue + ".png"
      : "diceBlue" + randomDiceValue + ".png");
    const getDiceImgElement = document.querySelector(".dice-img");
    getDiceImgElement.src = `assets/img/dice/${randomDiceImg}`
    return randomDiceValue;
  } else{
    console.log('window is not open');
  }
};

// const handleShowDicePopUp = () =>{  
//   const checkClass = getDicePopUpElement.classList
//   console.log(checkClass);
//   if (checkClass[0] === 'open'){
//     getDicePopUpElement.classList.remove('open');
//     getDicePopUpElement.classList.add('close')
//   } else{
//     getDicePopUpElement.classList.remove('close');
//     getDicePopUpElement.classList.add('open')
//   }
// }

// const getDiceBtn = document.querySelector('.btn-dice')
// getDiceBtn.addEventListener('click',handleShowDicePopUp)

// const getRollfeature = document.querySelector('.roll-feature')
// getRollfeature.addEventListener('click',handleDiceRolling)

// const getPlayernameElement = document.querySelector('.player-dice-rolling')
// getPlayernameElement.innerHTML = `${player}`


