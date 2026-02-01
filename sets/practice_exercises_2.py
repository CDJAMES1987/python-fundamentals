"""
Print the first duplicate value.

Rules:
- You may use ONLY one set
- No dictionaries
- Stop as soon as you find the duplicate
"""
nums = [5, 1, 2, 1, 5]
seen = set()

for x in nums:
    if x in seen:
        break
    seen.add(x)

"""
Return a set of ALL values that appear more than once.

Rules:
- You may use at most TWO sets
- One pass through the list
- No dictionaries
"""

nums = [5, 1, 2, 1, 5, 3, 2, 6]
nums_set = set()


def get_duplicates(nums: list[int]) -> set:

    for num in nums:
        if num in nums_set:
            break
        nums_set.add(num)

    return nums_set


output = get_duplicates(nums=nums)
print(output)

"""
Print each character and its index.
"""

text = "code"

# Write your solution below
for i, s in enumerate(text):
    print(i, s)

"""
Print only even numbers.
"""

nums = [1, 2, 3, 4, 5, 6]

# Write your solution below

for num in nums:
    if num % 2 == 0:
        print(num)

"""
Print numbers until you hit a number greater than 4.
Then stop.
"""

nums = [1, 2, 3, 5, 6, 2]

# Write your solution below

for num in nums:
    if num < 4:
        print(num)
    else:
        break

"""
Print all numbers less than 5.
If you encounter a number equal to 7, stop the loop entirely.

Expected behavior with the given list:
- Print 1, 2, 3, 4
- Stop when 7 is encountered
"""

nums = [1, 2, 3, 7, 4, 2, 8]

for num in nums:
    if num == 7:
        break
    if num < 5:
        print(num)

"""
Question 1: Basic String Manipulation (Easy)
Write a function that takes a string and returns it reversed, but with words in their original order.
"""


def reverse_string(string: str) -> str:

    string = string.split(sep=None)
    reversed_words = []

    for s in string:
        reversed_words.append("".join(reversed(s)))
    reversed_words = " ".join(reversed_words)
    return reversed_words


string = "hello world"
output = reverse_string(string=string)
print(output)

"""
Question 2: Two Sum (Easy-Medium)
Write a function that finds the two numbers in a list that sum to a target value. Return their indices.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # because nums[0] + nums[1] = 2 + 7 = 9
"""


def two_sum(nums: list[int], target: int) -> list[int] | None:
    output = []
    for i, num_1 in enumerate(nums):
        for j, num_2 in enumerate(nums):
            if num_1 + num_2 == target and i != j:
                return [i, j]


nums = [3, 2, 4]
target = 6
x = two_sum(nums=nums, target=target)
print(x)


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


nums = [3, 2, 4]
target = 6
x = two_sum(nums=nums, target=target)
print(x)
