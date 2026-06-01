'''
Problem 2

Write a function process_students that:

Takes a required name argument
Takes an optional scores argument (default to an empty list)
Takes any number of keyword arguments for extra student info
Returns a dict with:
"name": the student's name
"average": average of scores rounded to 1 decimal, or None if no scores
Any extra keyword arguments merged in

'''
from typing import Any


def process_students(name: str, scores: list[int] | None = None, **kwargs) -> dict[str, Any]:
    students = {}
    students['name'] = name
    if scores is None:
        students['average'] = None
    else:
        students['average'] = round(sum(scores) / len(scores), 1)

    for key, value in kwargs.items():
        students[key] = value

    return students


if __name__ == "__main__":
    process_students("Alice", [88, 92, 79], grade="A", year=2)
    process_students("Bob")
