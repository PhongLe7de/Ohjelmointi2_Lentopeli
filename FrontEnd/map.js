const map = L.map('map').setView([20, 0], 3.4);

L.marker([60, 20]).addTo(map).bindPopup("<b>The World!</b><br>Time has stopped!").openPopup();
L.marker([27, -82], {icon: L.icon({iconUrl: "jotaro.jpg", iconSize: [80, 80]})}).addTo(map);
L.circle([50, 20], {color: 'red', fillColor: '#f03', fillOpacity: 0.5,radius: 500}).addTo(map).bindPopup("pie");
L.polygon([[51.509, -0.08], [30, 50], [10, 0]], {color: "rgb(50,5,5)"}).addTo(map).bindPopup("Pony gone.");
L.polygon([[0, -50], [50, -50], [10, -60]], {color: "rgb(5,5,50)"}).addTo(map).bindPopup("Pony gone.");
map.on('click', (e)=>{L.popup().setLatLng(e.latlng).setContent("You clicked the map at " + e.latlng.toString()).openOn(map);});





function drawTheRoute(route){
    L.polyline(route, {color: 'red'}).addTo(map);
    for(let place of route){
        L.marker(place).addTo(map);
    }
}
const testRoute = [[4,6],[50,50],[-40,40]];
drawTheRoute(testRoute);

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