function loadAnalyticsData() {
  fetch("/api/analytics")
    .then((response) => response.json())
    .then((data) => {
      const analyticsDataContainer = document.getElementById(
        "analyticsDataContainer"
      );

      analyticsDataContainer.innerHTML = `
                <h3>Analytics Data</h3>
                <p>Total Visitors: ${data.totalVisitors}</p>
                <p>Page Views: ${data.pageViews}</p>
                <!-- Add more metrics as needed -->
            `;

      renderAnalyticsChart(data);
    })
    .catch((error) => {
      console.error("Error fetching analytics data:", error);
    });
}

function renderAnalyticsChart(data) {
  const analyticsChartCanvas = document
    .getElementById("analyticsChart")
    .getContext("2d");
  new Chart(analyticsChartCanvas, {
    type: "bar",
    data: {
      labels: ["Visitors", "Page Views"],
      datasets: [
        {
          label: "Analytics Data",
          data: [data.totalVisitors, data.pageViews],
          backgroundColor: [
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 99, 132, 0.2)",
          ],
          borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 99, 132, 1)"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
