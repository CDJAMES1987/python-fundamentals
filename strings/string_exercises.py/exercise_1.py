"""
Docstring for strings.string_exercises.py.exercise_1

Problem 1: Reverse Words in a String
Difficulty: Easy
Problem:
Given a string s, reverse the order of words.
Examples:
pythonInput: "the sky is blue"
Output: "blue is sky the"

Input: "  hello world  "
Output: "world hello"
# Note: Reduce multiple spaces to single space

Input: "a good   example"
Output: "example good a"
Constraints:

Input may contain leading/trailing spaces
Multiple spaces between words should be reduced to one
"""


def reverse_string(s: str) -> str:
    s = s.strip()
    words = s.split()
    words = words[::-1]
    return ' '.join(words)


def main():
    s = "a good   example"
    output = reverse_string(s=s)
    print(output)


if __name__ == '__main__':
    main()
