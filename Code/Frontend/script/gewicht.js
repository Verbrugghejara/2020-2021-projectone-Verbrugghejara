'use strict';

const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const backend_IP = 'http://localhost:5000';
const backend = backend_IP + '/api/v1';




//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
    console.log('DOM geladen');
    socket.on('B2F_set_gram',function(json){
        console.log('set gram')
        console.log(json)
        const gewicht_drink = json['gewichtdrink']
        const gewicht_voer = json['gewichtvoer']
        if (gewicht_drink == null){
            gewicht_drink = 0
        }
        if (gewicht_voer == null){
            gewicht_voer =0
        }
        document.querySelector('.js-gewicht-drinkbak').value = gewicht_drink
        document.querySelector('.js-gewicht-voerbak').value = gewicht_voer
    })
    document.querySelector('.js-button-opslaan').addEventListener('click', function(){
        console.log('click')
        const drinkbak = document.querySelector('.js-gewicht-drinkbak').value
        
        const voerbak = document.querySelector('.js-gewicht-voerbak').value
        console.log(drinkbak)
        console.log(voerbak)
        // const body = JSON.stringify({
        //     Gewicht_drinkbak: document.querySelector('.js-gewicht-drinkbak').value,
        //     Gewicht_voerbak: document.querySelector('js-gewicht-voerbak').value
        // })
        socket.emit('F2B_gewicht_bak',{Gewicht_drinkbak: `${drinkbak}`,Gewicht_voerbak: `${voerbak}`})
    })
  };
  //#endregion
  
  document.addEventListener('DOMContentLoaded', init);
  