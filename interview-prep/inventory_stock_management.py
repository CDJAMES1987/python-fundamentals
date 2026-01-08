"""
Problem:

You have a list of inventory transactions, where each transaction is represented by a dictionary with the following keys:

- `product_id`: a unique identifier for the product (string)
- `quantity`: the number of items added or removed (integer; positive for addition, negative for removal)
- `timestamp`: the time of the transaction (string in ISO format)

Write a function `net_inventory(transactions)` that returns the net quantity of each product after all transactions.

- If a product has never been added, it should not appear in the final result.
- The function should return a dictionary where the keys are the `product_id` and the values are the net quantities (integers).

Example:

transactions = [
    {"product_id": "A123", "quantity": 10, "timestamp": "2024-01-01T10:00:00Z"},
    {"product_id": "A123", "quantity": -4, "timestamp": "2024-01-02T12:00:00Z"},
    {"product_id": "B456", "quantity": 5, "timestamp": "2024-01-03T09:00:00Z"},
    {"product_id": "A123", "quantity": 2, "timestamp": "2024-01-04T15:00:00Z"}
]
net_inventory(transactions)

# returns {'A123': 8, 'B456': 5}
"""


def net_inventory(transactions: list[dict[str, object]]) -> dict[str, int]:
    # Output dictionary to store net quantities
    net_inventory: dict[str, int] = {}

    # Loop through each transaction
    for transaction in transactions:
        product_id = transaction["product_id"]
        quantity = transaction["quantity"]

        # Initialize the product in the dictionary if it doesn't exist
        if product_id not in net_inventory:
            net_inventory[product_id] = 0

        # Add the quantity to the net inventory
        net_inventory[product_id] += quantity

    return net_inventory


if __name__ == "__main__":
    transactions = [
        {"product_id": "A123", "quantity": 10,
            "timestamp": "2024-01-01T10:00:00Z"},
        {"product_id": "A123", "quantity": -4,
            "timestamp": "2024-01-02T12:00:00Z"},
        {"product_id": "B456", "quantity": 5, "timestamp": "2024-01-03T09:00:00Z"},
        {"product_id": "A123", "quantity": 2, "timestamp": "2024-01-04T15:00:00Z"}
    ]

    output = net_inventory(transactions)
    print(output)
