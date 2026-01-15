"""
Exercise 1: Create and Inspect a Set

Create a set from the list below.
Print the set and its length.
"""

import gc
nums = [1, 2, 2, 3, 4, 4, 5]

# Write your solution below
nums_set = set(nums)
print(nums_set)
print(len(nums_set))

"""
Exercise 2: Membership Testing

Check whether 3 and 10 exist in the set below.
Print the results.
"""

s = {2, 4, 6, 8}

# Write your solution below

print(3 in s)   # True
print(10 in s)  # False

"""
Exercise 3: Add and Remove Elements

Starting with the set below:
- Add "green"
- Remove "blue"
- Print the final set
"""

colors = {"red", "blue"}

# Write your solution below
colors.add("green")
colors.remove("blue")
print(colors)

"""
Exercise 4: Union

Create a set containing all unique elements from both sets.
"""

a = {1, 2, 3}
b = {3, 4, 5}

# Write your solution below
c = a.union(b)
print(c)

"""
Exercise 5: Intersection

Create a set of elements that appear in both sets.
"""

a = {1, 2, 3}
b = {3, 4, 5}

# Write your solution below

print(a.difference(b))

"""
Exercise 6: Difference

Create a set of elements that are in a but not in b.
"""

a = {1, 2, 3}
b = {3, 4, 5}

# Write your solution below
a.difference(b)

"""
Exercise 7: Symmetric Difference

Create a set of elements that are in either a or b, but not both.
"""

a = {1, 2, 3}
b = {3, 4, 5}

# Write your solution below
a.symmetric_difference(b)

"""
Exercise 8: Remove Duplicates While Preserving Order

Given the list below, return a new list with duplicates removed
while preserving the original order.

Expected output:
[1, 2, 3, 4]
"""

nums = [1, 2, 2, 3, 1, 4]

# Write your solution below

set(nums)

"""
Exercise 9: Find Common Elements Between Lists

Find the common elements between the two lists and return them as a set.
"""

list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "kiwi", "cherry"]

# Write your solution below

list_inter = set(list1).intersection(set(list2))
list_inter

"""
Exercise 10: Check for Overlap

Write a function that returns True if two lists share
at least one element.

The solution should run in O(n + m) time.
"""


def has_overlap(a: list[int], b: list[int]) -> bool:
    a = set(a)
    b = set(b)

    return bool(a.intersection(b))


# Write your solution below
output = has_overlap(a=list1, b=list2)

"""
Exercise 11: Count Unique Words

Given the sentence below, return the number of unique words.
"""

text = "the cat and the dog and the cat"

# Write your solution below
words = text.split()
word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

print(word_count)
