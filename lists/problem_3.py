'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Write a function that:

Returns the sum of each row as a list e.g. [6, 15, 24]
Returns the diagonal elements (top-left to bottom-right) as a list e.g. [1, 5, 9]
Returns a flattened version of the matrix (one single list) e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def answer(matrix: list[list[int]]) -> tuple[list[int], list[int], list[int]]:

    sum_list = []
    diag_list = []
    diag_list_2 = []
    flat_list = []

    for element in matrix:
        result = sum(element)
        sum_list.append(result)

        flat_list.extend(element)

    for i, element in enumerate(matrix):
        diag_list.append(element[i])

    for i, element in enumerate(matrix):
        diag_list_2.append(element[len(matrix) - 1 - i])

    return sum_list, flat_list, diag_list, diag_list_2


if __name__ == '__main__':
    answer(matrix=matrix)
