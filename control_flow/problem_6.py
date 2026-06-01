'''
Problem 6

Write a function remove_duplicates(numbers) that returns a new list with duplicates removed, preserving the original order, using a while loop.

remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])  →  [3, 1, 4, 5, 9
'''


def remove_duplicates(numbers: list[int]) -> list[int]:
    i = 0
    seen = set()
    output = []
    while i < len(numbers):
        number = numbers[i]
        i += 1
        if number in seen:
            continue
        else:
            seen.add(number)
            output.append(number)

    return output


if __name__ == "__main__":
    remove_duplicates(numbers=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
