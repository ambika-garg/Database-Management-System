/* eslint-disable object-curly-newline */

/* global Chart */

/**
 * --------------------------------------------------------------------------
 * CoreUI Boostrap Admin Template (v3.2.0): main.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

/* eslint-disable no-magic-numbers */
// random Numbers
var random = function random() {
  return Math.round(Math.random() * 100);
}; // eslint-disable-next-line no-unused-vars


var lineChart = new Chart(document.getElementById('canvas-1'), {
  type: 'line',
  data: {
    labels: ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20'],
    datasets: [{
      label: 'No. of Participants',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      data: [random(), random(), random(), random(), random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var lineChart = new Chart(document.getElementById('canvas-2'), {
  type: 'line',
  data: {
    labels: ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20'],
    datasets: [{
      label: 'No. of Participants Placed',
      backgroundColor: 'rgba(220, 220, 220, 0.2)',
      borderColor: 'rgba(220, 220, 220, 1)',
      pointBackgroundColor: 'rgba(220, 220, 220, 1)',
      pointBorderColor: '#fff',
      data: [random(), random(), random(), random(), random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var barChart = new Chart(document.getElementById('canvas-3'), {
  type: 'bar',
  data: {
    labels: ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20'],
    datasets: [{
      label: 'Male',
      backgroundColor: 'rgba(220, 220, 220, 0.5)',
      borderColor: 'rgba(220, 220, 220, 0.8)',
      highlightFill: 'rgba(220, 220, 220, 0.75)',
      highlightStroke: 'rgba(220, 220, 220, 1)',
      data: [random(), random(), random(), random(), random(), random(), random(), random()]
    }, {
      label: 'Female',
      backgroundColor: 'rgba(151, 187, 205, 0.5)',
      borderColor: 'rgba(151, 187, 205, 0.8)',
      highlightFill: 'rgba(151, 187, 205, 0.75)',
      highlightStroke: 'rgba(151, 187, 205, 1)',
      data: [random(), random(), random(), random(), random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var doughnutChart = new Chart(document.getElementById('canvas-4'), {
  type: 'doughnut',
  data: {
    labels: ['General', 'SC', 'ST', 'OBC'],
    datasets: [{
      data: [random(), random(), random(), random()],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
      hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var radarChart = new Chart(document.getElementById('canvas-5'), {
  type: 'radar',
  data: {
    labels: ['General', 'SC', 'ST', 'OBC'],
    datasets: [{
      label: 'Male',
      backgroundColor: 'rgba(220, 220, 220, 0.2)',
      borderColor: 'rgba(220, 220, 220, 1)',
      pointBackgroundColor: 'rgba(220, 220, 220, 1)',
      pointBorderColor: '#fff',
      pointHighlightFill: '#fff',
      pointHighlightStroke: 'rgba(220, 220, 220, 1)',
      data: [ random(), random(), random(), random()]
    }, {
      label: 'Female',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      pointHighlightFill: '#fff',
      pointHighlightStroke: 'rgba(151, 187, 205, 1)',
      data: [random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var radarChart = new Chart(document.getElementById('canvas-6'), {
  type: 'radar',
  data: {
    labels: ['Punjab', 'J&K', 'Himachal Pradesh', 'Haryana', 'Uttar Pradesh', 'Rajasthan', 'Uttarakhand', 'Delhi', 'Chandigarh'],
    datasets: [{
      label: 'State',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      pointHighlightFill: '#fff',
      pointHighlightStroke: 'rgba(151, 187, 205, 1)',
      data: [random(), random(), random(), random(), random(), random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var pieChart = new Chart(document.getElementById('canvas-7'), {
  type: 'pie',
  data: {
    labels: ['KVIC', 'Tech Mahindra and CSR', 'PCRA', 'MCC', 'Team Lease TATA', 'IBM CRS', 'MBI', 'DIRECTORATE OF URBAN DEVELOPMENT', 'NSDC-SJVN'],
    datasets: [{
      data: [random(), random(), random(), random(), random(), random(), random(), random(), random()],
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#E7E9ED', '#321fdb','#2eb85c','#636f83','#f9b115'],
      hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#E7E9ED', '#321fdb','#2eb85c','#636f83','#f9b115']
    }]
  },
  options: {
    responsive: true
  }
}); // eslint-disable-next-line no-unused-vars

var polarAreaChart = new Chart(document.getElementById('canvas-8'), {
  type: 'polarArea',
  data: {
    labels: ['PCRA', 'Team Lease TATA', 'NSDC-SJVN', 'Tech Mahindra and CSR', 'Team Lease TATA', 'DIRECTORATE OF URBAN DEVELOPMENT', 'Team Lease TATA'],
    datasets: [{
      data: [random(), random(), random(), random(), random(), random(), random()],
      backgroundColor: ['#FF6384', '#4BC0C0', '#FFCE56', '#E7E9ED', '#36A2EB', '#321fdb','#636f83','#2eb85c']
    }]
  },
  options: {
    responsive: true
  }
});
//# sourceMappingURL=charts.js.map