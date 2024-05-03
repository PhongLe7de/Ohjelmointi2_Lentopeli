'use strict';
const winning = document.getElementById("win");
const play1name = document.getElementById("p1-name");
const play2name = document.getElementById("p2-name");
console.log(player01Data.score, player02Data.score);
console.log(player01Data.mainland.length);

/*
function whoWins() {
   console.log(player01Data.mainland.length);
   if (player01Data.mainland.length === 2) {
      if (player01Data.score > player02Data.score) {
        const result_p1 = document.createElement("p");
        result_p1.innerHTML = `Pelaaja ${play1name.innerHTML} on Ökyrikas ja Rutikuiva`;
        document.getElementById("print").appendChild(result_p1);
          console.log(player01Data.score, player02Data.score);
     } else {
        const result_p1 = document.createElement("p");
        result_p1.innerHTML = `Pelaaja ${play1name.innerHTML} on Rutikuiva`;
        document.getElementById("print").appendChild(result_p1);

        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Upporikas`;
        document.getElementById("print").appendChild(result_p2);
        console.log(player01Data.score, player02Data.score);
      }
   } else {
      if (player02Data.score > player01Data.score) {
        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Ökyrikas ja Rutikuiva`;
        document.getElementById("print").appendChild(result_p2);
          console.log(player01Data.score, player02Data.score);
     } else {
        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Rutikuiva`;
        document.getElementById("print").appendChild(result_p2);

        const result_p1 = document.createElement("p");
        result_p1.innerHTML = `Pelaaja ${play1name.innerHTML} on Upporikas`;
        document.getElementById("print").appendChild(result_p1);
        console.log(player01Data.score, player02Data.score);

      }
   }
}

 */

function whoWins1(){
    if (player01Data.score > player02Data.score) {
        const result_p1 = document.createElement("p");
        result_p1.innerHTML = `Pelaaja ${play1name.innerHTML} on Ökyrikas ja Rutikuiva`;
        document.getElementById("print").appendChild(result_p1);
        console.log(player01Data.score, player02Data.score);
    } else {
        const result_p1 = document.createElement("p");
        result_p1.innerHTML = `Pelaaja ${play1name.innerHTML} on Rutikuiva`;
        document.getElementById("print").appendChild(result_p1);

        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Upporikas`;
        document.getElementById("print").appendChild(result_p2);
        console.log(player01Data.score, player02Data.score);
    }
}

function whoWins2(){
    if (player02Data.score > player01Data.score) {
        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Ökyrikas ja Rutikuiva`;
        document.getElementById("print").appendChild(result_p2);
        console.log(player01Data.score, player02Data.score);
    } else {
        const result_p2 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play2name.innerHTML} on Rutikuiva`;
        document.getElementById("print").appendChild(result_p2);

        const result_p1 = document.createElement("p");
        result_p2.innerHTML = `Pelaaja ${play1name.innerHTML} on Upporikas`;
        document.getElementById("print").appendChild(result_p1);
        console.log(player01Data.score, player02Data.score);
    }
}



