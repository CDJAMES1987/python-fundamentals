'''
Problem 3 — elif chains

Write a function grade_calculator(score: int) -> str that returns a letter grade:

90+ → "A"
80-89 → "B"
70-79 → "C"
60-69 → "D"
Below 60 → "F"
'''


def grade_calculator(score: int) -> str:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = 'F'
    return grade


if __name__ == '__main__':
    grade_calculator(score=59)
