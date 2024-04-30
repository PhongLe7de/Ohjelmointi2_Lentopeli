const map = L.map('map').setView([20, 0], 1);
let player1 = document.querySelector("#player-1-name");
let player2 = document.querySelector("#player-2-name");
let form7 = document.querySelector("#form7");
//console.log(player1, player1.value)

//L.marker([60, 20]).addTo(map).bindPopup("<b>The World!</b><br>Time has stopped!").openPopup();
//L.marker([27, -82], {icon: L.icon({iconUrl: "jotaro.jpg", iconSize: [80, 80]})}).addTo(map);
//L.circle([50, 20], {color: 'red', fillColor: '#f03', fillOpacity: 0.5,radius: 500}).addTo(map).bindPopup("pie");
//L.polygon([[51.509, -0.08], [30, 50], [10, 0]], {color: "rgb(50,5,5)"}).addTo(map).bindPopup("Pony gone.");
//L.polygon([[0, -50], [50, -50], [10, -60]], {color: "rgb(5,5,50)"}).addTo(map).bindPopup("Pony gone.");
//map.on('click', (e)=>{L.popup().setLatLng(e.latlng).setContent("You clicked the map at " + e.latlng.toString()).openOn(map);});
//L.marker([50,-50], {opacity: 1, zIndexOffset: 100, riseOnHover: true, riceOffSet:1000}).addTo(map);
//L.marker([10,-50], {riseOnHover: true}).addTo(map);
/*
let adobe = L.marker([0,0],{transparent: true});
adobe.addTo(map);

var layer = L.marker([50,60]).addTo(map);
layer.addTo(map);
*/

form7.addEventListener("submit", formGetter);
async function formGetter(e){
    e.preventDefault();
    const game1 = await fetch(`http://127.0.0.1:3000/start_game/${player1.value}/${player2.value}`);
    const game2 = await game1.json();
    console.log("HERE", game2.gameid);
    drawTheRoute(game2.gameid);
}


//let formi = formGetter();
//console.log(formi);
async function drawTheRoute(gameid){
    const route1 = await fetch(`http://127.0.0.1:3000/gameboard/${gameid}`);
    const route2 = await route1.json();
    let cordinates = [];
    for(i of route2){
        cordinates.push([i.latitude_deg, i.longitude_deg]);
    }
    L.polyline(cordinates, {color: "rgb(100,100,100)"}).addTo(map);
    for(let place of cordinates){
        //L.marker(place, {icon: L.icon({iconUrl: "jotaro.jpg", iconSize: [100,100]}), opacity: 100}).addTo(map);
        L.marker(place).addTo(map);
    }
}
//drawTheRoute();


L.geoJson(continentAF, {style: {color:"rgb(200,0,0)"}}).addTo(map);
L.geoJson(continentAN, {style: {color:"rgb(0,0,256)"}}).addTo(map);
L.geoJson(continentAS, {style: {color:"rgb(100,0,100)"}}).addTo(map);
L.geoJson(continentEU, {style: {color:"rgb(100,100,250)"}}).addTo(map);
L.geoJson(continentNA, {style: {color:"rgb(150,150,0)"}}).addTo(map);
L.geoJson(continentOC, {style: {color:"rgb(250,150,50)"}}).addTo(map);
L.geoJson(continentSA, {style: {color:"rgb(0,250,0)"}}).addTo(map);



L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);