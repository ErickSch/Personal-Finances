

// Day expenses START 
const dayExpenses = document.getElementById('dayExpenses');


// new Chart(dayExpenses, {
//     type: 'line',
//     data: {
//     labels: [{% for expense in todays_expenses %}'{{expense.type}}',{% endfor %}],
//     datasets: [{
//         label: 'Daily Totals (MXP)',
//         data: [{% for expense in todays_expenses %}'{{expense.total}}',{% endfor %}],
//         borderWidth: 1,
//         pointBackgroundColor: 'rgba(255, 159, 64, 0.5)',
//         pointBorderColor: 'rgba(255, 159, 64)',
//     }]
//     },
//     options: {
//     scales: {
//         y: {
//         beginAtZero: true
//         }
//     }
//     }
// });
// statistics.js

document.addEventListener('DOMContentLoaded', function() {

  /////////////////////////////////////////
  // LINE CHART - todaysExpensesLineChart -
  const todaysExpensesLineChart = document.getElementById('todaysExpensesLineChart');
  new Chart(todaysExpensesLineChart, {
    type: 'line',
    data: {
      labels: todays_expenses_labels,
      datasets: [{
        label: 'Today\s Expenses (MXP)',
        data: todays_expenses_data,
        borderWidth: 1,
        pointBackgroundColor: 'rgba(255, 159, 64, 0.5)',
        pointBorderColor: 'rgba(255, 159, 64)',
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  ////////////////////////////////////
  // BAR CHART - dailyTotalsBarChart -

  const dailyTotalsBarChart = document.getElementById('dailyTotalsBarChart');
  new Chart(dailyTotalsBarChart, {
      type: 'bar',
      data: {
      labels: daily_expenses_labels,
      datasets: [{
          label: 'Daily Totals (MXP)',
          data: daily_expenses_data,
          borderWidth: 1,
          backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
      ],
      borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
      ],
      }]
      },
      options: {
      scales: {
          y: {
          beginAtZero: true
          }
      }
      }
  });

  //////////////////////////////////////////////
  // DOUGHNUT CHART - todaysTotalDoughnutChart -


  const todaysTotalDoughnutChart = document.getElementById('todaysTotalDoughnutChart');
  new Chart(todaysTotalDoughnutChart, {
      type: 'doughnut',
      data: {
      labels: month_expenses_per_type_types,
      datasets: [{
          label: 'Type totals (MXP)',
          labels: {
            render: 'label'
          },
          data: month_expenses_per_type_totals,
          borderWidth: 1,
          backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
      ],
      borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
      ],
      cutout: '30%',
      // borderRadius: 5,
      weight: 0.5,
      hoverOffset: 4,
      }],
      },
      labels: {
        render: 'label'
      } 
  });










});

