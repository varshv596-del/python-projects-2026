from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

DATA_FILE = "expenses.json"


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])

        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                expenses = json.load(file)
        else:
            expenses = []

        expenses.append({
            "name": name,
            "amount": amount
        })

        with open(DATA_FILE, "w") as file:
            json.dump(expenses, file, indent=4)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            expenses = json.load(file)
    else:
        expenses = []

    total = sum(item["amount"] for item in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)