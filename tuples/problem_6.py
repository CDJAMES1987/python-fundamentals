'''Problem 6


inventory = (
    ("Laptop", "Electronics", 999.99, 15),
    ("Phone", "Electronics", 699.99, 30),
    ("Desk", "Furniture", 349.99, 10),
    ("Chair", "Furniture", 199.99, 25),
    ("Monitor", "Electronics", 449.99, 20),
    ("Bookshelf", "Furniture", 149.99, 8)
)

Each tuple is (name, category, price, stock).

Write a function that returns:

Total value per category (price × stock) as a dict e.g. {"Electronics": 123.0, "Furniture": 456.0}
The cheapest item per category as a dict e.g. {"Electronics": "Phone", "Furniture": "Bookshelf"}
All items sorted by stock ascending
Categories where total stock exceeds 50 as a list of strings
'''

inventory = (
    ("Laptop", "Electronics", 999.99, 15),
    ("Phone", "Electronics", 699.99, 30),
    ("Desk", "Furniture", 349.99, 10),
    ("Chair", "Furniture", 199.99, 25),
    ("Monitor", "Electronics", 449.99, 20),
    ("Bookshelf", "Furniture", 149.99, 8)
)


def answer(inventory: tuple[tuple[str, str, float, int]]) -> tuple[dict[str, float], dict[str, str], list[tuple[str, str, float, int]], list[str]]:
    q1 = {}
    q2 = {}
    q4 = {}

    for name, category, price, stock in inventory:
        if category not in q1:
            q1[category] = 0
        q1[category] += price * stock

        if category not in q2:
            q2[category] = (price, name)

        elif price < q2[category][0]:
            q2[category] = (price, name)

    q2 = {cat: val[1] for cat, val in q2.items()}

    q3 = sorted(inventory, key=lambda x: x[3])

    for name, category, price, stock in inventory:
        if category not in q4:
            q4[category] = 0
        q4[category] += stock

    result = []
    for category, total in q4.items():
        if total > 50:
            result.append(category)

    return q1, q2, q3, result


if __name__ == '__main__':
    answer(inventory=inventory)
