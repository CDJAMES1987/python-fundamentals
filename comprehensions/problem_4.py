'''
Problem 4 — harder, combining comprehensions with nested data:

orders = [
    {"customer": "Alice", "items": ["laptop", "mouse"], "total": 1250.00},
    {"customer": "Bob", "items": ["keyboard"], "total": 89.99},
    {"customer": "Alice", "items": ["monitor"], "total": 650.00},
    {"customer": "Charlie", "items": ["laptop", "webcam"], "total": 1100.00},
    {"customer": "Bob", "items": ["mouse", "headset"], "total": 259.99}
]

Write a function using comprehensions that returns:

A list of all customers who spent over 500 total (across all orders)
A flat list of all items ordered across all orders e.g. ["laptop", "mouse", "keyboard", ...]
A dict of total spent per customer
A list of orders with more than one item
'''
orders = [
    {"customer": "Alice", "items": ["laptop", "mouse"], "total": 1250.00},
    {"customer": "Bob", "items": ["keyboard"], "total": 89.99},
    {"customer": "Alice", "items": ["monitor"], "total": 650.00},
    {"customer": "Charlie", "items": ["laptop", "webcam"], "total": 1100.00},
    {"customer": "Bob", "items": ["mouse", "headset"], "total": 259.99}
]


def answer(orders: list[dict[str, str | list[str] | float]]) -> tuple[list[str], list[str], dict[str, float], list[dict[str, str | list[str] | float]]]:

    q3 = {}
    for order in orders:
        if order['customer'] not in q3:
            q3[order['customer']] = 0
        q3[order['customer']] += order['total']

    q1 = [key for key, value in q3.items() if value > 500]
    q2 = [item for order in orders for item in order['items']]
    q4 = [order for order in orders if len(order['items']) > 1]

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(orders=orders)
