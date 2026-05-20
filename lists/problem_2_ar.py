'''
students = [
    ["Alice", 88],
    ["Bob", 72],
    ["Charlie", 95],
    ["Diana", 61]
]
Write a function that returns:

Name of the student with the highest score
List of names of students who scored above 75
Average score rounded to 1 decimal place
'''

students = [
    ["Alice", 88],
    ["Bob", 72],
    ["Charlie", 95],
    ["Diana", 61]
]


def answer(students: list[list[str | int]]) -> tuple[str, list[str], float]:

    curr_max = students[0][1]
    max_name = students[0][0]
    above_75 = []
    sum_scores = 0

    for student in students:
        if curr_max < student[1]:
            curr_max = student[1]
            max_name = student[0]
        if student[1] > 75:
            above_75.append(student[0])
        sum_scores += student[1]
    avg_score = round(sum_scores / len(students), 1)
    return max_name, above_75, avg_score


if __name__ == '__main__':
    answer(students=students)
