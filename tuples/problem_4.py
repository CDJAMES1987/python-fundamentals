'''
Problem 4


products = (
    ("Apple", 1.50, 100),
    ("Banana", 0.75, 150),
    ("Cherry", 3.00, 50),
    ("Date", 5.00, 30),
    ("Elderberry", 2.50, 80)
)
Each tuple is (name, price, quantity).

Write a function that returns:

Products sorted by price ascending
The most expensive product name only (just the string)
Total inventory value — sum of price * quantity for all products
All products with quantity above 75, sorted by quantity descending
'''

products = (
    ("Apple", 1.50, 100),
    ("Banana", 0.75, 150),
    ("Cherry", 3.00, 50),
    ("Date", 5.00, 30),
    ("Elderberry", 2.50, 80)
)


def answer(products: tuple[tuple[str, float, int]]) -> tuple[list[tuple[str, float, int]], str, float, list[tuple[str, float, int]]]:

    q1 = sorted(products, key=lambda x: x[1])
    q2 = q1[-1][0]
    q3 = []
    q4 = []

    for name, price, quantity in products:
        q3.append(price * quantity)
        if quantity > 75:
            q4.append((name, price, quantity))

    q3 = sum(q3)
    q4 = sorted(q4, key=lambda x: x[2], reverse=True)

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(products=products)
