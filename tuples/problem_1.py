'''
Problem 1

point = (3, 7)
person = ("Alice", 30, "Engineer")
coordinates = [(1, 2), (3, 4), (5, 6)]
Write a function that:

Swaps the values in point and returns as a tuple e.g. (7, 3)
Unpacks person into separate variables and returns a formatted string: "Alice is 30 years old and works as an Engineer"
Returns a list of all x-coordinates from coordinates e.g. [1, 3, 5]
'''

point = (3, 7)
person = ("Alice", 30, "Engineer")
coordinates = [(1, 2), (3, 4), (5, 6)]


def answer(tup1: tuple[int, int], tup2: tuple[str, int, str],
           tup3: list[tuple[int, int]]) -> tuple[tuple[int, int], str, list[int]]:

    p1, p2 = tup1
    q1 = p2, p1

    name, age, title = tup2
    q2 = f'{name} is {age} years old and works as an {title}'

    q3 = []
    for coords in tup3:
        x, y = coords
        q3.append(x)

    return q1, q2, q3


if __name__ == "__main__":
    answer(tup1=point, tup2=person, tup3=coordinates)
