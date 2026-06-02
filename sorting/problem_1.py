'''
Problem 1

employees = [
    {"name": "Charlie", "salary": 88000, "years": 8},
    {"name": "Alice", "salary": 95000, "years": 5},
    {"name": "Diana", "salary": 81000, "years": 6},
    {"name": "Bob", "salary": 72000, "years": 3},
    {"name": "Eve", "salary": 102000, "years": 2}
]
Write a function that returns:

Employees sorted by salary descending
Employees sorted by years ascending, then name alphabetically (two-key sort)
The top 2 highest paid employees (just their names)
Employees sorted by salary but with a custom rule:
anyone with 5+ years gets sorted as if their salary is 10% higher
'''
employees = [
    {"name": "Charlie", "salary": 88000, "years": 8},
    {"name": "Alice", "salary": 95000, "years": 5},
    {"name": "Diana", "salary": 81000, "years": 6},
    {"name": "Bob", "salary": 72000, "years": 3},
    {"name": "Eve", "salary": 102000, "years": 2}
]


def employee_sorting(employees: list[dict[str, str | int]]) -> tuple[list[dict[str, str | int]], list[dict[str, str | int]], list[str], list[dict[str, str | int]]]:
    q1 = sorted(employees, key=lambda x: x['salary'], reverse=True)
    q2 = sorted(employees, key=lambda x: (x['years'], x['name']))
    q3 = [employee['name'] for employee in q1[:2]]
    q4 = sorted(
        employees, key=lambda x: (
            x['salary'] * 1.10 if x['years'] > 5 else x['salary']))
    return q1, q2, q3, q4


if __name__ == '__main__':
    employee_sorting(employees=employees)
