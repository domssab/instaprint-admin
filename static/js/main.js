var ctx = document.getElementById("salesChart").getContext("2d");
var chart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
            label: "Sales",
            data: {{ data.sales_chart | tojson }},
            backgroundColor: "red"
        }]
    }
});