const getDicePopUpElement = document.getElementById('modal-dice')
const getRollfeature = document.querySelector('.roll-feature')

getRollfeature.addEventListener('click',()=>{handleDiceRolling(currentPlayer)})
let currentPlayer = 0;

const handleDiceRolling = async(player) => {

  const player01 = document.getElementById('player-1-name')
  const player02 = document.getElementById('player-2-name')
  const listPlayer = [player01.value, player02.value]
  console.log(listPlayer);
  const checkClass = getDicePopUpElement.classList

  if (checkClass[0] === 'open'){
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
    updateData(data)
    // getEffect(data)
    getCoCard()
    getSurpriseCard()


    currentPlayer = currentPlayer === 0 ? 1 : 0

  } else{
    console.log('window is not open');
  }
};

const updateData = async (data) => {
    try {
      const response = await fetch('http://localhost:3000/move_player/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({data})
      });
      if (response.ok) {
        result = await response.json()
        console.log("update success");
        console.log(result);
      } else {
        console.log("update fail");
      }
    } catch (error) {
      console.log(error);
    }
};

const getEffect = async (data)=>{
  try {
    const response = await fetch('http://localhost:3000/effect/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({data})
    });
    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.log(error);
  }
}


async function getCoCard(){
  try {
    const response = await fetch(`http://127.0.0.1:3000/get_co_card`);
    const jsonData = await response.json();
    return jsonData
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