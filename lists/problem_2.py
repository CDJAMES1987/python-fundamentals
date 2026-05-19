'''
Problem 2

students = [
    ["Alice", 88],
    ["Bob", 72],
    ["Charlie", 95],
    ["Diana", 61]
]
Write a function that:

Returns the name of the student with the highest score
Returns a list of names of students who scored above 75
Returns the average score (rounded to 1 decimal place)
'''
students = [
    ["Alice", 88],
    ["Bob", 72],
    ["Charlie", 95],
    ["Diana", 91]
]


def answer(students: list[str | int]) -> tuple[str, list[str], float]:

    max_score = students[0][1]
    name = students[0][0]
    above_75 = []
    sum_scores = 0

    for scores in students:
        if max_score < scores[1]:
            max_score = scores[1]
            name = scores[0]
        if scores[1] > 75:
            above_75.append(scores[0])
        sum_scores += scores[1]
    avg_score = round(sum_scores / len(students), 1)
    result = name, above_75, avg_score
    return result


if __name__ == '__main__':
    answer(students=students)
