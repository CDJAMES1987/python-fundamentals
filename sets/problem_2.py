'''
Problem 2

employees_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
employees_b = {"Bob", "Diana", "Frank", "Grace"}
employees_c = {"Alice", "Charlie", "Frank", "Henry"}

Write a function that returns:

Employees who work in all three departments
Employees who work in department A but not B or C
Employees who work in exactly one department
Total number of unique employees across all departments
'''


employees_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
employees_b = {"Bob", "Diana", "Frank", "Grace"}
employees_c = {"Alice", "Charlie", "Frank", "Henry"}


def answer(employees_a: set[str], employees_b: set[str], employees_c: set[str]) -> tuple[set[str], set[str], set[str], int]:

    q1 = employees_a.intersection(employees_b, employees_c)
    q2 = employees_a - (employees_b | employees_c)
    q3 = (employees_a - employees_b - employees_c) | \
        (employees_b - employees_a - employees_c) | \
        (employees_c - employees_a - employees_b)
    q4 = len(employees_a.union(employees_b, employees_c))

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(employees_a=employees_a,
           employees_b=employees_b, employees_c=employees_c)
