'''
Problem 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Write a function using comprehensions that returns:

A list of squares of all even numbers
A dict mapping each number to its square e.g. {1: 1, 2: 4, ...}
A set of all odd numbers
A list of "even" or "odd" for each number e.g. ["odd", "even", "odd", ...]
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def answer(numbers: list[int]) -> tuple[list[int], dict[int, int], set[int], list[str]]:
    q1 = [number ** 2 for number in numbers if number % 2 == 0]
    q2 = {number: number ** 2 for number in numbers}
    q3 = {number for number in numbers if number % 2 != 0}
    q4 = ["even" if number % 2 == 0 else "odd" for number in numbers]
    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(numbers=numbers)
