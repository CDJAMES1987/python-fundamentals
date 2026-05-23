'''
 Problem 2:

records = [
    ("Alice", 88, "Math"),
    ("Bob", 72, "Science"),
    ("Charlie", 95, "Math"),
    ("Diana", 61, "Science"),
    ("Eve", 91, "Math")
]
Write a function that returns:

A list of tuples containing only students who scored above 80
The average score per subject as a dict e.g. {"Math": 91.3, "Science": 66.5}
The top student per subject as a dict e.g. {"Math": "Charlie", "Science": "Bob"}
'''

records = [
    ("Alice", 88, "Math"),
    ("Bob", 72, "Science"),
    ("Charlie", 95, "Math"),
    ("Diana", 61, "Science"),
    ("Eve", 91, "Math")
]


def answer(records: list[tuple[str, int, str]]) -> tuple[list[tuple[str, int, str]], dict[str, float], dict[str, str]]:

    q1 = []
    q2 = {}
    q3 = {}

    for name, grade, subject in records:
        if grade > 80:
            q1.append((name, grade, subject))

    for name, grade, subject in records:
        if subject not in q2:
            q2[subject] = []
        q2[subject].append(grade)

    for subject in q2:
        q2[subject] = round(sum(q2[subject]) / len(q2[subject]), 1)

    for name, grade, subject in records:
        if subject not in q3:
            q3[subject] = (name, grade)
        elif grade > q3[subject][1]:
            q3[subject] = (name, grade)

    return q1, q2, q3


if __name__ == '__main__':
    answer(records=records)
