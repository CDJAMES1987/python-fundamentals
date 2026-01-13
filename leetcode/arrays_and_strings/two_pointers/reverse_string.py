class Solution:
    def reverse_string(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def main():
    s = ['h', 'e', 'l', 'l', 'o']
    solution = Solution()
    solution.reverse_string(s=s)
    print(s)


if __name__ == '__main__':
    main()
