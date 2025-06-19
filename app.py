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

# Utility functions
# Extract a single transaction
def get_transaction(id):
    for entry in transactions:
        if entry["id"] == id:
            return entry
    return None

# Update a single transaction
def upd_transaction(id, new_entry):
    for entry in transactions:
        if entry["id"] == id:
            entry.update(new_entry)
            break

# Delete a single transaction
def del_transaction(id):
    for i, entry in enumerate(transactions):
        if entry["id"] == id:
            del transactions[i]
            break

# Calculate total amount
def calculate_total_amount(transactions):
    total = 0
    for entry in transactions:
        total += entry["amount"]

    # Handle data type
    if total.is_integer():
        total = int(total)

    return total

# API endpoints
# Read operation
@app.route("/")
def get_transactions():
    # Retrieve and sort transactions by date (latest first)
    sorted_transactions = sorted(transactions, key = lambda x: x["date"], reverse=True)

    # Calculate total amount
    total = calculate_total_amount(sorted_transactions)

    return render_template("transactions.html", transactions=sorted_transactions, show_button=False, total_amount=total)

# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        if len(transactions) == 0:
            id = 1
        else:
            id = max(entry["id"] for entry in transactions) + 1

        date = request.form["date"]
        amount = float(request.form["amount"])

        # Check if amount is a whole number
        if amount.is_integer():
            amount = int(amount)

        # Define and add new entry
        transaction = {
            "id": id,
            "date": date,
            "amount": amount
        }
        transactions.append(transaction)

        return redirect(url_for("get_transactions"))
    
    # GET request
    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        amount = float(request.form["amount"])

        # Check if amount is a whole number
        if amount.is_integer():
            amount = int(amount)

        transaction = {
            "id": int(transaction_id),
            "date": request.form["date"],
            "amount": amount
        }
        upd_transaction(transaction_id, transaction)
        return redirect(url_for("get_transactions"))
    
    # GET request
    transaction = get_transaction(transaction_id)
    return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    del_transaction(transaction_id)
    return redirect(url_for("get_transactions"))

# Search operation
@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        min_amount = float(request.form["min_amount"])
        max_amount = float(request.form["max_amount"])

        # Filter transactions
        filtered_transactions = [entry for entry in transactions if entry["amount"] >= min_amount and entry["amount"] <= max_amount]

        # Sort filtered transactions
        sorted_transactions = sorted(filtered_transactions, key = lambda x: x["amount"], reverse=True)

        # Calculate total amount
        total = calculate_total_amount(sorted_transactions)

        return render_template("transactions.html", transactions=sorted_transactions, show_button=True, total_amount=total)
    return render_template("search.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5001, debug = True)