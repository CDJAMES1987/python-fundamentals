'''
Problem 5

Write a function find_index(numbers, target) that returns the index of the first occurrence of target in the list using a while loop. Return -1 if not found.

find_index([4, 7, 2, 9, 1, 5], 9)  →  3
find_index([4, 7, 2, 9, 1, 5], 6)  →  -1

'''


def find_index(numbers: list[int], target: int) -> int:
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if number == target:
            return i
        i += 1
    else:
        return -1


if __name__ == "__main__":
    find_index(numbers=[4, 7, 2, 9, 1, 5], target=9)
