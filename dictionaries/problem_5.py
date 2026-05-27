'''
Problem 5

orders = {
    "order_001": {"customer": "Alice", "items": ["laptop", "mouse"], "total": 1250.00, "status": "delivered"},
    "order_002": {"customer": "Bob", "items": ["keyboard"], "total": 89.99, "status": "pending"},
    "order_003": {"customer": "Alice", "items": ["monitor", "webcam", "headset"], "total": 650.00, "status": "delivered"},
    "order_004": {"customer": "Charlie", "items": ["laptop"], "total": 999.99, "status": "pending"},
    "order_005": {"customer": "Bob", "items": ["mouse", "keyboard"], "total": 159.99, "status": "delivered"}
}
Write a function that returns:

Total amount spent per customer as a dict
Number of orders per customer as a dict
All pending orders as a dict (same structure as input)
The customer who has spent the most
'''

orders = {
    "order_001": {"customer": "Alice", "items": ["laptop", "mouse"], "total": 1250.00, "status": "delivered"},
    "order_002": {"customer": "Bob", "items": ["keyboard"], "total": 89.99, "status": "pending"},
    "order_003": {"customer": "Alice", "items": ["monitor", "webcam", "headset"], "total": 650.00, "status": "delivered"},
    "order_004": {"customer": "Charlie", "items": ["laptop"], "total": 999.99, "status": "pending"},
    "order_005": {"customer": "Bob", "items": ["mouse", "keyboard"], "total": 159.99, "status": "delivered"}
}


def answer(orders: dict[str, dict[str, str | list[str] | float]]) -> tuple[dict[str, float], dict[str, int], dict[str, dict[str, str | list[str] | float]], str]:
    q1 = {}
    q2 = {}
    q3 = {}
    for key, value in orders.items():
        if value['customer'] not in q1:
            q1[value['customer']] = 0
            q2[value['customer']] = 0
        q1[value['customer']] += value['total']
        q2[value['customer']] += 1

        if value['status'] == 'pending':
            q3[key] = value

    for key, value in q1.items():
        q1[key] = round(value, 2)

    q4 = max(q1, key=lambda x: q1[x])

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(orders=orders)
