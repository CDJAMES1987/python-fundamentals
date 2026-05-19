'''
Problem Statement
I'd like you to write a function that accepts two lists-of-lists of numbers and 
returns one list-of-lists with each of the corresponding numbers in the two given 
lists-of-lists added together.

It should work something like this:

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
add(matrix1, matrix2)
[[3, -3], [-3, 3]]
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Bonus 1
For the first bonus, modify your add function to accept and "add" any number of lists-of-lists.

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]

'''


def add(matrix1: list[int, int], matrix2: list[int, int]) -> list[int, int]:

    result = []

    for i, j in zip(matrix1, matrix2):
        row = []
        for a, b in zip(i, j):
            row.append(a + b)
        result.append(row)

    return result


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

if __name__ == '__main__':
    add(matrix1, matrix2)
