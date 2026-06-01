'''
Problem 1

Write three functions:

multiply(a, b) — returns a * b, with b defaulting to 2
sum_all(*args) — returns the sum of any number of arguments
describe(**kwargs) — returns a formatted string from keyword 
arguments e.g. describe(name="Alice", age=30) → "name: Alice, age: 30"
'''


def multiply(a: int, b: int = 2) -> int:
    return a * b


def sum_all(*args: int) -> int:
    return sum(args)


def describe(**kwargs: dict[str, int]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())


if __name__ == "__main__":
    multiply(a=2)
    sum_all(4, 2)
    describe(name="Alice", age=30)
