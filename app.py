from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv("../data/ecommerce_sales.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

@app.route("/api/kpis")
def get_kpis():
    return jsonify({
        "total_sales": int(df["total_price"].sum()),
        "total_orders": int(df["order_id"].nunique()),
        "avg_order_value": round(df["total_price"].mean(), 2)
    })

@app.route("/api/sales_by_month")
def sales_by_month():
    monthly_sales = df.groupby(
        df["order_date"].dt.to_period("M")
    )["total_price"].sum()

    return jsonify({str(k): int(v) for k, v in monthly_sales.items()})

if __name__ == "__main__":
    app.run(debug=True)