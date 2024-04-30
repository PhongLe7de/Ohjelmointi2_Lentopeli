const handleShowDicePopUp = () =>{  
  const checkClass = getDicePopUpElement.classList
  if (checkClass[0] === 'open'){
    getDicePopUpElement.classList.remove('open');
    getDicePopUpElement.classList.add('close')
  } else{
    getDicePopUpElement.classList.remove('close');
    getDicePopUpElement.classList.add('open')
  }
}

const getDiceBtn = document.querySelector('.btn-dice')
getDiceBtn.addEventListener('click',handleShowDicePopUp)

const getPlayernameElement = document.querySelector('.player-dice-rolling')
getPlayernameElement.innerHTML = `${player}`


