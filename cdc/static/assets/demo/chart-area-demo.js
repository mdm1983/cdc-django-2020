// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var labelsData = [];
var list = document.getElementsByName("linelabel");
var i = 1;
for (i = 0; i < list.length; i++) {
  labelsData.push(list[i].value);
}
var dataData = [];
var listData = document.getElementsByName("linedata");
var maxData = 0;
var minData = 0;
for (i = 0; i < listData.length; i++) {
  dataData.push(listData[i].value);
  if (Number(listData[i].value)>maxData){
    maxData = Number(listData[i].value);
  } 
  if (Number(listData[i].value)<minData){
    minData = Number(listData[i].value);
  }
}
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: labelsData,
    datasets: [{
      label: "Balance",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: dataData,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: minData,
          max: maxData,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
