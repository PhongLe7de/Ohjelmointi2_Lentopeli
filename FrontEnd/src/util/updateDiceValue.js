const URL = ''; //waiting for URL from BackEnd

const player = 2;
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
      value: randomDiceValue
    }

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
        method: "PATCH",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({ player, data }),
      });

      if (response.ok) {
        console.log("update success");
      } else {
        console.log("update fail");
      }
    } catch (error) {
      console.log(error);
    }
};