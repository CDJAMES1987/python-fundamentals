'''
Problem 4

employees = {
    "Alice": {"department": "Engineering", "salary": 95000, "years": 5},
    "Bob": {"department": "Marketing", "salary": 72000, "years": 3},
    "Charlie": {"department": "Engineering", "salary": 88000, "years": 8},
    "Diana": {"department": "Marketing", "salary": 81000, "years": 6},
    "Eve": {"department": "Engineering", "salary": 102000, "years": 2}
}
Write a function that returns:

Average salary per department as a dict
The most senior employee (most years) per department as a dict e.g. {"Engineering": "Charlie", "Marketing": "Diana"}
A list of employees due for a raise — more than 4 years but salary below 90000
Total salary cost per department as a dict
'''
employees = {
    "Alice": {"department": "Engineering", "salary": 95000, "years": 5},
    "Bob": {"department": "Marketing", "salary": 72000, "years": 3},
    "Charlie": {"department": "Engineering", "salary": 88000, "years": 8},
    "Diana": {"department": "Marketing", "salary": 81000, "years": 6},
    "Eve": {"department": "Engineering", "salary": 102000, "years": 2}
}


def answer(employees: dict[str, dict[str, str | int]]) -> tuple[dict[str, float], dict[str, str], list[str], dict[str, float]]:
    q1 = {}
    dept_counts = {}

    for key, value in employees.items():
        if value['department'] not in q1:
            q1[value['department']] = 0
        q1[value['department']] += value['salary']

        if value['department'] not in dept_counts:
            dept_counts[value['department']] = 0
        dept_counts[value['department']] += 1

    for dept in q1:
        q1[dept] = round(q1[dept] / dept_counts[dept], 1)

    q2 = {}
    for key, value in employees.items():
        if value['department'] not in q2:
            q2[value['department']] = (key, value['years'])
        elif value["years"] > q2[value['department']][1]:
            q2[value['department']] = (key, value["years"])

    for key, value in q2.items():
        q2[key] = value[0]

    q3 = []
    for key, value in employees.items():
        if value["salary"] < 90000:
            if value["years"] > 4:
                q3.append(key)

    q4 = {}
    for key, value in employees.items():
        if value["department"] not in q4:
            q4[value['department']] = 0
        q4[value['department']] += value['salary']

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(employees=employees)
