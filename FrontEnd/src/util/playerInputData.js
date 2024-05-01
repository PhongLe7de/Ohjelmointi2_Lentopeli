// const player01 = document.getElementById('player-1-name')
// const player02 = document.getElementById('player-2-name')

const inputPlayerElement = document.getElementsByClassName('input-player')
const playerNameSubmitBtn = inputPlayerElement[0].querySelector('input[type=submit]')

// let player1Name
// let player2Name
// player01.addEventListener('change',(e)=>{
//     player1Name = e.target.value
//     console.log(player1Name);
// })

// player02.addEventListener('change',(e)=>{
//      player2Name = e.target.value
//     console.log(player2Name);
// })
let gameboardArraywait = []

const playerName1 = {
    player1_name: '1234526728921',
    player2_name: '1987625423221'
}


const URL_UPDATE_PLAYERNAME = 'http://localhost:3000/start_game/'; //waiting for URL from BackEnd
const URL_GET_GAMEBOARD = 'http://localhost:3000/gameboard/'; //waiting for URL from BackEnd

const handlePlayerInput = playerNameSubmitBtn.addEventListener('click', async(e) => {
    e.preventDefault()
    const gameboardId = await inputPlayerData(URL_UPDATE_PLAYERNAME, playerName1)
    const gameboardArray = await getGameBoard(URL_GET_GAMEBOARD,gameboardId)
})

const inputPlayerData = async (URL, data) => {
    console.log(data);
    try {
        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        })
        if (response.ok) {
            const result = await response.json()
            const gameId = result.gameid
            console.log(result);
            return gameId
        } else {
            console.log('Fetch API FAIL')
        } 
    } catch (error) {
        console.error(error);
    }
}

const getGameBoard = async (URL, id) => {
    try {
        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id })
        })
        if (response.ok) {
            const result = await response.json()
            console.log(result);
        } else {
            console.log('Fetch API FAIL')
        } 
    } catch (error) {
        console.error(error);
    }
}



