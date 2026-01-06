"""
Module: employee_metrics.py

Exercise: Above Average Salary

Prompt:
Given a list of Employee objects, calculate the average salary
and return a list of employee names whose salary is greater than
the average salary across all employees.

Constraints:
- Use loops and conditionals (no external libraries for computation).

Example:
>>> employees = [
...     Employee('Chris', 150_000),
...     Employee('Luke', 250_000),
...     Employee('Jamie', 50_000)
... ]
>>> above_average_salary(employees)
['Chris', 'Luke']
"""


class Employee:
    """Represents an employee with a name and salary."""

    def __init__(self, name: str, salary: float):
        """
        Initialize an Employee instance.

        Args:
            name (str): The employee's name.
            salary (float): The employee's salary.
        """
        self.name = name
        self.salary = salary


def above_average_salary(employees: list[Employee]) -> list[str]:
    """
    Calculate the average salary of all employees and return
    a list of employee names with salary greater than the average.

    Args:
        employees (list[Employee]): A list of Employee objects.

    Returns:
        list[str]: Names of employees earning above the average salary.
    """
    list_of_employees: list[str] = []
    sum_of_salary: float = 0.0

    # Calculate total salary
    for employee in employees:
        sum_of_salary += employee.salary

    # Calculate average salary
    average_salary = sum_of_salary / len(employees)

    # Find employees above average
    for employee in employees:
        if employee.salary > average_salary:
            list_of_employees.append(employee.name)

    return list_of_employees


if __name__ == "__main__":
    employees = [
        Employee(name='Chris', salary=150_000.00),
        Employee(name='Luke', salary=250_000.00),
        Employee(name='Jamie', salary=50_000.00)
    ]

    result = above_average_salary(employees=employees)
    print(f"Employees with salaries above average: {result}")
