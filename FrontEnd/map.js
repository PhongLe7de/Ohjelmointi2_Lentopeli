const map = L.map("map").setView([20, 0], 1);
let player1html = document.querySelector("#player-1-name");
let player2html = document.querySelector("#player-2-name");
let form7 = document.querySelector("#form7");

class Player {
  constructor(name, icao, gameid) {
    this.name = name;
    this.icao = icao;
    this.gameid = gameid;
    this.cordinates = [78.246101379395, 15.465600013733];
    this.playerMarker = L.marker(this.cordinates);
  }
  cordinateFinder() {
    for (let i of gameRoute) {
      if (i.ident == this.icao) {
        this.cordinates = [i.latitude_deg, i.longitude_deg];
      }
    }
  }
  moveMarker() {
    this.playerMarker._latlng.lat = this.cordinates[0];
    this.playerMarker._latlng.lon = this.cordinates[1];
    this.playerMarker.addTo(map);
  }
}

var player1Name;
var player2Name;
var player1Marker = L.marker([78.246101379395, 15.465600013733], {icon: L.icon({iconUrl: "red_plane_left.png", iconSize: [50,50]})}).addTo(map);
var player2Marker = L.marker([78.246101379395, 15.465600013733], {icon: L.icon({iconUrl: "blue_plane_right.png", iconSize: [50,50]})}).addTo(map);

function movePlayerMarker(player, place){
    if(player == player1Name) {
        console.log('test')
        player1Marker.setLatLng([place.latitude_deg, place.longitude_deg]);
    }
    else if(player == player2Name){
        player2Marker.setLatLng([place.latitude_deg, place.longitude_deg]);
    }
}

let gameRoute;

form7.addEventListener("submit",()=>{handlePlayerInput() });
    const handlePlayerInput = playerNameSubmitBtn.addEventListener('click', async(e) => {
        const playerNameList= {
            player1_name: player01.value,
            player2_name: player02.value
        }
        e.preventDefault()
        document.getElementById('p1-name').innerHTML = `${playerNameList.player1_name}`
        document.getElementById('p2-name').innerHTML = `${playerNameList.player2_name}`
        const gameboardId = await inputPlayerData(URL_UPDATE_PLAYERNAME, playerNameList)
        const gameboardArray = await getGameBoard(URL_GET_GAMEBOARD,gameboardId.gameid)
        drawTheRoute(gameboardArray)
    })
//   try {
//     const response = await fetch(`http://127.0.0.1:3000/start_game/`, {
//       method: "GET",
//       headers: {
//         "Content-Type": "application/json",
//       },
//     });
//     if (response.ok) {
//       const result = await response.json();
//       const gameId = result.gameid;
//       console.log(result);
//       return gameId;
//     } else {
//       console.log("Fetch API FAIL");
//     }
//   } catch (error) {
//     console.error(error);
//   }
//   const game2 = await game1.json();
//   player1_name = game2["data"]["player1_name"];
//   player2_name = game2["data"]["player2_name"];

//   if (game2.gameid) {
//     try {
//       const response = await fetch(`http://127.0.0.1:3000/gameboard/`, {
//         method: "GET",
//         headers: {
//           "Content-Type": "application/json",
//         },
//       });
//       if (response.ok) {
//         const result = await response.json();
//         console.log(result);
//         const player1 = new Player(game2.player1_name, "ENSB", game2.gameid);
//         const player2 = new Player(game2.player2_name, "ENSB", game2.gameid);
//         drawTheRoute();
//       } else {
//         console.log("Fetch API FAIL");
//       }
//     } catch (error) {
//       console.error(error);
//     }

//     const route1 = await fetch(`http://127.0.0.1:3000/gameboard/`);
//     gameRoute = await route1.json();
//   } else {
//     alert("Be more original, dumbass");
//   }
// }

// async function drawTheRoute() {
//   //console.log(gameRoute);
//   let cordinates = [];
//   for (i of gameboardArray) {
//     cordinates.push([i.latitude_deg, i.longitude_deg]);
//   }
//   L.polyline(cordinates, { color: "rgb(100,100,250)" }).addTo(map);
//   for (let place of cordinates) {
//     //L.marker(place, {icon: L.icon({iconUrl: "jotaro.jpg", iconSize: [100,100]}), opacity: 100}).addTo(map);
//     //L.marker(place).addTo(map);
//   }
// }

L.geoJson(continentAF, { style: { color: "rgb(200,0,0)" } }).addTo(map);
L.geoJson(continentAN, { style: { color: "rgb(0,0,256)" } }).addTo(map);
L.geoJson(continentAS, { style: { color: "rgb(100,0,100)" } }).addTo(map);
L.geoJson(continentEU, { style: { color: "rgb(100,100,250)" } }).addTo(map);
L.geoJson(continentNA, { style: { color: "rgb(180, 180, 100)" } }).addTo(map);
L.geoJson(continentOC, { style: { color: "rgb(250,150,50)" } }).addTo(map);
L.geoJson(continentSA, { style: { color: "rgb(0,250,0)" } }).addTo(map);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

async function drawTheRoute(gameboardArray) {
    //console.log(gameRoute);
    let cordinates = [];
    for (i of gameboardArray) {
    cordinates.push([i.latitude_deg, i.longitude_deg]);
    }
    L.polyline(cordinates, { color: "rgb(190,157,184,1)" }).addTo(map);
    for (let place of cordinates) {
    //L.marker(place, {icon: L.icon({iconUrl: "jotaro.jpg", iconSize: [100,100]}), opacity: 100}).addTo(map);
    //L.marker(place).addTo(map);
    }
}