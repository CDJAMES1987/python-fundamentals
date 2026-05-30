'''
Problem 4 — combined

numbers = [4, 15, 7, 22, 3, 18, 11, 9, 25, 6, 14, 8]
Write a function that:

Loops through the list using a while loop
Skips any number below 5 using continue
Stops the loop if it encounters a number above 20 using break
For each number that passes, categorises it using elif:
5-9 → "small"
10-14 → "medium"
15-20 → "large"
Returns a dict of {number: category} for all processed numbers
'''

numbers = [4, 15, 7, 22, 3, 18, 11, 9, 25, 6, 14, 8]


def answer(numbers: list[int]) -> dict[int, str]:
    q1 = {}
    i = 0
    while i < len(numbers):
        number = numbers[i]
        i += 1
        if number < 5:
            continue
        if number > 20:
            break
        if number >= 15:
            q1[number] = 'large'
        elif number >= 10:
            q1[number] = 'medium'
        elif number >= 5:
            q1[number] = 'small'

    return q1


if __name__ == "__main__":
    answer(numbers=numbers)
