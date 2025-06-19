# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Extract a single transaction
def get_transaction(id):
    for transaction in transactions:
        if transaction["id"] == id:
            return transaction
    return None

# Update a single transaction
def upd_transaction(id, new_transaction):
    for transaction in transactions:
        if transaction["id"] == id:
            transaction.update(new_transaction)
            break

def del_transaction(id):
    for i, transaction in enumerate(transactions):
        if transaction["id"] == id:
            del transactions[i]
            break
        
# Read operation
@app.route("/")
def get_transactions():
    sorted_transactions = sorted(transactions, key = lambda x: x["date"], reverse=True)
    return render_template("transactions.html", transactions=sorted_transactions)

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        if len(transactions) == 0:
            id = 1
        else:
            id = max(entry["id"] for entry in transactions) + 1
        date = request.form["date"]
        amount = request.form["amount"]
        transaction = {
            "id": id,
            "date": date,
            "amount": amount
        }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))
    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        transaction = {
            "id": transaction_id,
            "date": request.form["date"],
            "amount": request.form["amount"]
        }
        upd_transaction(transaction_id, transaction)
        return redirect(url_for("get_transactions"))
    transaction = get_transaction(transaction_id)
    return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    del_transaction(transaction_id)
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5001, debug = True)