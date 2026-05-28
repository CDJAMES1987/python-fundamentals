'''
Problem 1

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9, 10]
list3 = [1, 3, 5, 7, 9, 11, 13]

Write a function that returns:

Elements that appear in all three lists
All unique elements across all three lists
Elements in list1 that don't appear in list2 or list3
Elements that appear in exactly two of the three lists
'''


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9, 10]
list3 = [1, 3, 5, 7, 9, 11, 13]


def answer(list1: list[int], list2: list[int], list3: list[int]) -> tuple[set[int], set[int], set[int], set[int]]:
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    q1 = set1.intersection(set2, set3)
    q2 = set1.union(set2, set3)
    q3 = set1.difference(set2).difference(set3)
    q4 = (set1 & set2 - set3) | (set1 & set3 - set2) | (set2 & set3 - set1)

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(list1=list1, list2=list2, list3=list3)
