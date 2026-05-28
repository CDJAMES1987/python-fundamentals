'''
Problem 3

students = {
    "Alice": [88, 92, 79, 95, 83],
    "Bob": [72, 68, 75, 80, 71],
    "Charlie": [95, 98, 92, 97, 99],
    "Diana": [61, 70, 65, 58, 72]
}

Write a function using comprehensions that returns:

A dict of each student's average score rounded to 1 decimal place
A list of students who are passing (average >= 75)
A dict of each student's highest score
A dict where failing students (average < 75) map to their scores list
'''

students = {
    "Alice": [88, 92, 79, 95, 83],
    "Bob": [72, 68, 75, 80, 71],
    "Charlie": [95, 98, 92, 97, 99],
    "Diana": [61, 70, 65, 58, 72]
}


def answer(students: dict[str, list[int]]) -> tuple[dict[str, float], list[str], dict[str, int], dict[str, list[int]]]:
    q1 = {key: round(sum(value) / len(value), 1)
          for key, value in students.items()}
    q2 = [key for key, value in q1.items() if value >= 75]
    q3 = {key: max(value) for key, value in students.items()}
    q4 = {key: value
          for key, value in students.items() if sum(value) / len(value) < 75}

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(students=students)
