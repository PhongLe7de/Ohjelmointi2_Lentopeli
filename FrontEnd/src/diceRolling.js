const handleDiceRolling = (player) =>{
    const player = player
    const randomDiceValue = Math.floor(Math.random()* 6 + 1)
    const randomDiceImg = player = 1 ? "diceRed"+randomDiceValue+".png" : "diceBlue"+randomNumber+".png" 
    const getDiceImgElement = document.getElementsByClassName("diceValueImage")
    getDiceImgElement.setAttribute("scr",`assets/img/dice/${randomDiceImg}`)
    return randomDiceValue
} 

export default handleDiceRolling