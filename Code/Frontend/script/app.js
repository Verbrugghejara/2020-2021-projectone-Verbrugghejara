'use strict';

const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);
let currentTempID;
let data2;

const backend_IP = 'http://localhost:5000';
const backend = backend_IP + '/api/v1';

//#region ***  DOM references ***

//#endregion

//#region ***  Callback-Visualisation - show___ ***
const showTemperatuur = function (jsonObject) {
  currentTempID = jsonObject.BakID;
  get_temp();
};

const showLastTemp = function (jsonObject) {
  console.log(jsonObject)
  console.log(jsonObject.temperatuur.temperatuur);
  const temp = jsonObject.temperatuur.temperatuur;
  const temphtml = document.querySelector('.js-temp');
  const temphtml2 = document.querySelector('.js-temp2');
  temphtml.innerHTML = Math.round(temp * 10) / 10;
  temphtml.innerHTML += ' °C';
  temphtml2.innerHTML = Math.round(temp * 10) / 10;
  temphtml2.innerHTML += ' °C';
};
const showData2 = function (data) {
  console.log('data1');
  data2 = data;
};
const showData = function (data1) {
  console.log('data');
  console.log(data1);
  console.log(data2);
  let data = [];
  let datatwee = [];
  for (const gewicht of data1.gewicht_drinken) {
    data.push(gewicht.gewicht);
  }
  for (const gewicht of data2.gewicht_voer) {
    datatwee.push(gewicht.gewicht);
  }
  console.log(data);
  console.log(datatwee);
  drawChart(data, datatwee);
};

const drawChart = function (data1, data2) {
  var options = {
    series: [
      {
        name: 'Drinken',
        data: data1,
      },
      {
        name: 'Voer',
        data: data2,
      },
    ],
    chart: {
      height: 328,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2,
      },
      toolbar: {
        show: false,
      },
    },
    colors: ['#77B6EA', '#545454'],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth',
    },
    title: {
      align: 'None',
    },
    grid: {
      borderColor: '#e7e7e7',
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5,
      },
    },
    markers: {
      size: 0.5,
    },
    xaxis: {
      categories: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
      min: 0,
      max: 25,
    },
    yaxis: {
      min: 0,
      max: 5,
      labels: {
        formatter: function (val) {
          return val.toFixed(0);
        },
      },
    },
    legend: {
      position: 'top',
      horizontalAlign: 'left',
      floating: true,
      offsetY: 0,
      offsetX: 0,
    },
  };

  var chart = new ApexCharts(document.querySelector('.js-chart'), options);
  chart.render();
};
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***
// const callbackdrinken = function (){
//   console.log('er ging iets mis drinken')
// }
// const callbackvoer = function (){
//   console.log('er ging iets mis voer')
// }
//#endregion

//#region ***  Data Access - get___ ***

const get_last_temp = function () {
  handleData(`http://${lanIP}/api/v1/temperatuur`, showTemperatuur, null, 'POST');
};
const get_temp = function () {
  handleData(`http://${lanIP}/api/v1/temperatuur/${currentTempID}`, showLastTemp);
};

const get_gewicht_drinken = function () {
  handleData(`http://${lanIP}/api/v1/gewicht/drinken`, showData);
  console.log("gewicht drinken")
};
const get_gewicht_voer = function () {
  handleData(`http://${lanIP}/api/v1/gewicht/voer`, showData2);
  console.log('gewicht voer')
};

// const getValue = function (radio) {
//   socket.emit('F2B_keuze', { KattenluikOptieID: `${radio.getAttribute('id')}`, Optie: `${radio.value}` });
//   console.log(radio)
//   // console.log(radio.getAttribute('id'));
//   radio.classList.add('c-option--select');
// };
// socket.emit('F2B_keuze',{})
//#endregion

//#region ***  Event Listeners - listenTo___ ***
const listenToSocket = function () {
  console.log('verbonden met socket webserver');
  socket.on('B2F_gewichten', function (jsonObject) {
    console.log(jsonObject.gewicht1);
    console.log(jsonObject.gewicht2);
    if (jsonObject.gewicht1 < 1000) {
      document.querySelector('.js-gewicht-drinken').innerHTML = Math.round(jsonObject.gewicht1 * 1) / 1;
      document.querySelector('.js-gewicht-drinken').innerHTML += ' gram';
      document.querySelector('.js-gewicht-drinken2').innerHTML = Math.round(jsonObject.gewicht1 * 1) / 1;
      document.querySelector('.js-gewicht-drinken2').innerHTML += ' gram';
    }
    if (jsonObject.gewicht2 < 1000) {
      document.querySelector('.js-gewicht-voer').innerHTML = Math.round(jsonObject.gewicht2 * 1) / 1;
      document.querySelector('.js-gewicht-voer').innerHTML += ' gram';
      document.querySelector('.js-gewicht-voer2').innerHTML = Math.round(jsonObject.gewicht2 * 1) / 1;
      document.querySelector('.js-gewicht-voer2').innerHTML += ' gram';
    }
    if (jsonObject.gewicht1 >= 1000) {
      let gewicht = jsonObject.gewicht1 / 1000;
      document.querySelector('.js-gewicht-drinken').innerHTML = Math.round(gewicht * 100) / 100;
      document.querySelector('.js-gewicht-drinken').innerHTML += ' kg';
      document.querySelector('.js-gewicht-drinken2').innerHTML = Math.round(gewicht * 100) / 100;
      document.querySelector('.js-gewicht-drinken2').innerHTML += ' kg';
    }
    if (jsonObject.gewicht2 >= 1000) {
      let gewicht = jsonObject.gewicht2 / 1000;
      document.querySelector('.js-gewicht-voer').innerHTML = Math.round(gewicht * 100) / 100;
      document.querySelector('.js-gewicht-voer').innerHTML += ' kg';
      document.querySelector('.js-gewicht-voer2').innerHTML = Math.round(gewicht * 100) / 100;
      document.querySelector('.js-gewicht-voer2').innerHTML += ' kg';
    }
  });
  socket.on('B2F_motion_detect', function (json){
    console.log('motion')
    const htmlmotion = document.querySelectorAll('.js-motion')
    for (const html of htmlmotion){
      html.innerHTML = json['tijd']
    }
  })
  socket.on('B2F_motion_all', function(json){
    let htmlstring = ``
    // console.log('motion all')
    // console.log(json)
    // console.log(json['datum'])
    const htmlmotion = document.querySelector('.js-motion-all')
    htmlstring += `<p>${json['datum']} <br> ${json['tijd']}</p>`
    htmlmotion.innerHTML += htmlstring
  })
};
const listenToChangeOption = function () {
  const buttons = document.querySelectorAll('.js-optie');
  for (const btn of buttons) {
    btn.addEventListener('click', function (e) {
      console.log('verandert');
      console.log(btn)
      resetButton()
      
      socket.emit('F2B_keuze', { KattenluikOptieID: `${btn.getAttribute('id')}`, Optie: `${btn.value}` });
  // console.log(radio.getAttribute('id'));
      //Loop over alle radiobuttons, en klasse verwijderen
      let radioButton = e.target;

      radioButton.parentNode.classList.add('c-option--select');
    });
  }
};
const listenToChangeOption2 = function () {
  const buttons = document.querySelectorAll('.js-optie2');
  for (const btn of buttons) {
    btn.addEventListener('click', function (e) {
      console.log('verandert');
      console.log(btn)
      resetButton2()
      
      socket.emit('F2B_keuze', { KattenluikOptieID: `${btn.getAttribute('id')}`, Optie: `${btn.value}` });
      //Loop over alle radiobuttons, en klasse verwijderen
      let radioButton = e.target;
      console.log('e')
      console.log(radioButton.value)
      if (radioButton.value != undefined){
        console.log('add class')
        radioButton.classList.add('c-button__select');
      }
      if (radioButton.value == undefined){
        radioButton.parentNode.classList.add('c-button__select');
        console.log('false')
      }
    });
  }
};
//#endregion

const resetButton = function () {
  const buttons = document.querySelectorAll('.js-optie');
  for (const btn of buttons) {
      console.log('reset');
      btn.parentNode.classList.remove('c-option--select');
  }
};
const resetButton2 = function () {
  const buttons = document.querySelectorAll('.js-optie2');
  for (const btn of buttons) {
      console.log('reset');
      btn.classList.remove('c-button__select');
  }
};

//#region ***  INIT / DOMContentLoaded  ***
const init = function () {
  console.log('DOM geladen');
  // listenToSocket()
  get_gewicht_voer();
  listenToSocket();
  get_last_temp();
  listenToChangeOption();
  listenToChangeOption2();
  get_gewicht_drinken();
};
//#endregion

document.addEventListener('DOMContentLoaded', init);
