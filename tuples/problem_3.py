'''
Problem 3

students = (
    ("Alice", 88),
    ("Bob", 72),
    ("Charlie", 95),
    ("Diana", 61)
)
Write a function that:

Returns the data sorted by score in descending order (as a list of tuples)
Returns only the names as a tuple
Returns the highest and lowest scoring student as a tuple of two tuples e.g. (("Charlie", 95), ("Diana", 61))
'''
students = (
    ("Alice", 88),
    ("Bob", 72),
    ("Charlie", 95),
    ("Diana", 61)
)


def answer(students: tuple[tuple[str, int]]) -> tuple[list[tuple[str, int]], tuple[str, ...], tuple[tuple[str, int], tuple[str, int]]]:
    q1 = []
    q2 = []
    max_grade = students[0][1]
    max_name = students[0][0]
    min_grade = students[0][1]
    min_name = students[0][0]

    for name, grade in students:
        q1.append((name, grade))
        q2.append(name)

        if max_grade < grade:
            max_grade = grade
            max_name = name

        if min_grade > grade:
            min_grade = grade
            min_name = name

    q1.sort(key=lambda x: x[1], reverse=True)
    q2 = tuple(q2)
    q3 = ((max_name, max_grade), (min_name, min_grade))

    return q1, q2, q3


if __name__ == '__main__':
    answer(students=students)
