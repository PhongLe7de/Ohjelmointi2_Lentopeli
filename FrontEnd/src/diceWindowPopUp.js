const getDicePopUpElement = document.getElementById('modal-dice')
console.log(getDicePopUpElement);
const handleShowDicePopUp = () =>{  
  const checkClass = getDicePopUpElement.classList
  console.log(checkClass);
  if (checkClass[0] === 'open'){
    getDicePopUpElement.classList.remove('open');
    getDicePopUpElement.classList.add('close')
  } else{
    getDicePopUpElement.classList.remove('close');
    getDicePopUpElement.classList.add('open')
  }
}

const getDiceBtn = document.querySelector('.openwindow')
console.log(getDiceBtn);
getDiceBtn.addEventListener('click',handleShowDicePopUp)

const getPlayernameElement = document.querySelector('.player-dice-rolling')
getPlayernameElement.innerHTML = `${player}`