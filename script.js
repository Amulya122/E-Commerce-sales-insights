fetch("http://127.0.0.1:5000/api/kpis")
.then(response => response.json())
.then(data => {
    document.getElementById("sales").innerText =
        "Total Sales: ₹" + data.total_sales;
    document.getElementById("orders").innerText =
        "Total Orders: " + data.total_orders;
    document.getElementById("aov").innerText =
        "Average Order Value: ₹" + data.avg_order_value;
});

fetch("http://127.0.0.1:5000/api/sales_by_month")
.then(response => response.json())
.then(data => {
    new Chart(document.getElementById("chart"), {
        type: "line",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Monthly Sales",
                data: Object.values(data),
                borderColor: "blue",
                fill: false
            }]
        }
    });
});