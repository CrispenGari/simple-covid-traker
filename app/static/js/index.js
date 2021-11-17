const deaths = [
    {% for item in deaths %}
      "{{ item }}",
     {% endfor %}
]
const confirmed = [
    {% for item in confirmed %}
      "{{ item }}",
     {% endfor %}
]

const recoveries = [
    {% for item in recoveries %}
      "{{ item }}",
     {% endfor %}
]
const labels = [
  {% for item in provinces %}
      "{{ item }}",
  {% endfor %}
]

const data = {
  labels,
  datasets:[
  {
      label: "deaths",
      fillColor: "red",
      data : deaths
  },
  {
      label: "recoveries",
      fillColor: "green",
      data : recoveries
  },
  {
      label: "confirmed",
      fillColor: "orange",
      data : confirmed
  }
  ]
}
const chart = document.getElementById("chart").getContext("2d");
steps = 20;
max = 1000;
// draw bar chart
new Chart(chart).Bar(data, {
  scaleOverride: true,
  scaleSteps: steps,
  scaleStepWidth: Math.ceil(max / steps),
  scaleStartValue: 0,
  scaleShowVerticalLines: true,
  scaleShowGridLines: true,
  barShowStroke: true,
  scaleShowLabels: true,
});