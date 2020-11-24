// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var labelsData = [];
var list = document.getElementsByName("histolabel");
var i = 1;
for (i = 0; i < list.length; i++) {
  labelsData.push(list[i].value);
}
var dataData = [];
var listData = document.getElementsByName("histodata");
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
  type: 'bar',
  data: {
    labels: labelsData,
    datasets: [{
      label: "Totale",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: dataData,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 12
        }
      }],
      yAxes: [{
        ticks: {
          min: minData,
          max: maxData,
          maxTicksLimit: 2
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
