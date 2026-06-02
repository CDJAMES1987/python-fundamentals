'''
Problem 2 — solve this completely on your own:

products = [
    {"name": "Laptop", "price": 999.99, "rating": 4.5, "stock": 15},
    {"name": "Phone", "price": 699.99, "rating": 4.8, "stock": 30},
    {"name": "Monitor", "price": 449.99, "rating": 4.2, "stock": 8},
    {"name": "Keyboard", "price": 89.99, "rating": 4.6, "stock": 50},
    {"name": "Mouse", "price": 49.99, "rating": 4.1, "stock": 100}
]
Return:

Products sorted by rating descending
Products sorted by price ascending
Top 3 products by rating (names only)
Products sorted by stock ascending, but out of stock items (stock=0) always go last
'''
products = [
    {"name": "Laptop", "price": 999.99, "rating": 4.5, "stock": 15},
    {"name": "Phone", "price": 699.99, "rating": 4.8, "stock": 30},
    {"name": "Monitor", "price": 449.99, "rating": 4.2, "stock": 8},
    {"name": "Keyboard", "price": 89.99, "rating": 4.6, "stock": 50},
    {"name": "Mouse", "price": 49.99, "rating": 4.1, "stock": 0}

]


def products_func(products: list[dict[str, str | float | int]]) -> tuple[list[dict[str, str | float | int]], list[dict[str, str | float | int]], list[str], list[dict[str, str | float | int]]]:
    q1 = sorted(products, key=lambda x: x['rating'], reverse=True)
    q2 = sorted(products, key=lambda x: x['price'])
    q3 = [product['name'] for product in q1[:3]]
    q4 = sorted(products, key=lambda x: float('inf')
                if x['stock'] == 0 else x['stock'])

    return q1, q2, q3, q4


if __name__ == '__main__':
    products_func(products=products)
