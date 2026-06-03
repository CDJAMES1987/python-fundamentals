'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def containsDuplicate(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


'''
# Intuition
Use set operations to remove duplicates, run a conditional check
for similarity

# Approach
Convert list to set, compare length of both, if length is not equal
list contains duplicates

# Complexity
- Time complexity:
len() is O(1) — Python stores the length, no loop needed
set(nums) is O(n) — it loops through once to build the set
len(set(nums)) is O(1) — length already stored

- Space complexity:
O(n) - creates a new set that grows with input size

'''
