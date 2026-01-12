"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        output = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output.append(nums[left] ** 2)
                left += 1
            else:
                output.append(nums[right] ** 2)
                right -= 1
        output = output[::-1]  # reverse list
        return output


def main():
    nums = [-4, -1, 0, 3, 10]
    solution = Solution()
    output = solution.sorted_squares(nums=nums)
    print(output)


if __name__ == "__main__":
    main()
