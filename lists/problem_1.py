'''
Problem 1

Given this list:

numbers = [5, 2, 8, 1, 9, 3]
Write code to:

Get the last element without using index -1 ... actually use -1, that's the right way
Get the first 3 elements
Get the last 2 elements
Sort it in descending order
Add the number 7 to the end
'''
numbers = [5, 2, 8, 1, 9, 3]


def answer(nums: list) -> tuple[int, list[int], list[int], list[int], list[int]]:
    nums = nums.copy()
    answer_1 = nums[-1]
    answer_2 = nums[:3]
    answer_3 = nums[-2:]
    answer_4 = sorted(nums, reverse=True)
    nums.append(7)
    answer_list = (answer_1, answer_2, answer_3, answer_4, nums)
    return answer_list


if __name__ == '__main__':
    x = answer(nums=numbers)
    print(x)
