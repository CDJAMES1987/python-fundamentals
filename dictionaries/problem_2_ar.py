
'''Write a function that returns:

A dict of each student's average score rounded to 1 decimal place
The top performing student's name
A dict of passing students (average >= 75) with their averages
A dict of each student's highest and lowest score as a tuple
'''
students = {
    "Alice": [88, 92, 79, 95, 83],
    "Bob": [72, 68, 75, 80, 71],
    "Charlie": [95, 98, 92, 97, 99],
    "Diana": [61, 70, 65, 58, 72]
}


def answer(students: dict[str, list[int]]) -> tuple[dict[str, float], str, dict[str, float], dict[str, tuple[int, int]]]:
    q1 = {}

    for key, value in students.items():
        q1[key] = round(sum(value) / len(value), 1)

    q2 = max(q1, key=lambda x: q1[x])

    q3 = {}
    for key, value in q1.items():
        if value >= 75:
            q3[key] = value

    q4 = {}
    for key, value in students.items():
        q4[key] = (max(value), min(value))

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(students=students)
