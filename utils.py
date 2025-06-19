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