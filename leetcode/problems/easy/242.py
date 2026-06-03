'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 0
            s_dict[c] += 1
        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1
        return s_dict == t_dict


if __name__ == '__main__':
    sol = Solution()
    sol.isAnagram(s="anagram", t="nagaram")

'''
# Intuition
Initial intuition was to use set operators and compare the sets,
but this didn't cover edge cases like s = "abb" and t = "aab"
where the resulting sets would be equal but not anagrams. Changed to
a frequency counting approach using dictionaries.

# Approach
Initialize empty dictionaries, increment a counter for each character
in each string, then compare the two dictionaries for equality.

# Complexity
- Time complexity: O(n) — two passes through the strings, dict comparison is O(1)

- Space complexity: O(1) — dict size is bounded by the alphabet size (26 lowercase
  English letters), so space does not grow with input size. If Unicode characters
  were allowed, this would be O(n).

'''
