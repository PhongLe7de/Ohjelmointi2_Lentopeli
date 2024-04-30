
// const stampAPIFectch = async(url) =>{
//     try {
//         const response = await  fetch(url,{
//             method: 'GET'
//         })
//         if(response.ok){
//             const result = response.json()

//         }
//     } catch (error) {
        
//     }
// }
stampList = {
    player1: ['EU', 'AF', 'SA'],
    player2: ['EU', 'AF', 'NA', 'SA']
}
console.log(stampList);
const mainlandStampsP1= document.getElementById('passport-1')
stampList.player1.forEach(mainland => {
    const getmainland = mainlandStampsP1.getElementsByClassName(`${mainland}-stamp`)
    if(getmainland){
        getmainland[0].src = `assets/leimat/${mainland}_saavutettu.png`
    }else{
        console.log('mainland not found');
    }
})

const mainlandStampsP2= document.getElementById('passport-2')
// const a = mainlandStampsP2.getElementsByClassName('EU-stamp')
stampList.player2.forEach(mainland => {
    const getmainland = mainlandStampsP2.getElementsByClassName(`${mainland}-stamp`)
    if(getmainland){
        getmainland[0].src = `assets/leimat/${mainland}_saavutettu.png`
    }else{
        console.log('mainland not found');
    }
})
