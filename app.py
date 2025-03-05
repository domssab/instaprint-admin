from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    data = {
        "total_sales": 1234.56,
        "printed_pages": 564,
        "files_uploaded": 7654,
        "current_balance": 4235.00,
        "sales_history": [
            {"method": "GCash Payment", "amount": 1234.56, "date": "9/18/2024", "time": "11:52 PM"},
            {"method": "Manual Payment", "amount": 1234.56, "date": "9/18/2024", "time": "11:52 PM"}
        ],
        "sales_chart": [random.randint(500, 2000) for _ in range(12)]  # Mock sales data
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)