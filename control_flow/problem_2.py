'''
Problem 2 — break and continue


numbers = [3, 7, 2, 15, 8, 4, 19, 11, 6, 13]
Write two separate functions:

find_first_over_10(numbers) — return the first number greater than 10, use break
skip_evens(numbers) — return a list of only odd numbers using continue (no if filter — must use continue to skip evens)
'''
numbers = [3, 7, 2, 15, 8, 4, 19, 11, 6, 13]


def find_first_over_10(numbers: list[int]) -> int:
    q1 = None
    for number in numbers:
        if number > 10:
            q1 = number
            break
    return q1


def skip_evens(numbers: list[int]) -> list[int]:
    q2 = []
    for number in numbers:
        if number % 2 == 0:
            continue
        q2.append(number)
    return q2


if __name__ == '__main__':
    find_first_over_10(numbers=numbers)
    skip_evens(numbers=numbers)
