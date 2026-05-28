'''
Problem 1

Take your solutions from the strings Problem 1 and rewrite them using comprehensions where possible:

sentence = "the quick brown fox jumps over the lazy dog"

Return:

The sentence in title case
Number of words
A list of all words longer than 3 characters — use a list comprehension
The sentence with "fox" replaced by "cat"
'''
sentence = "the quick brown fox jumps over the lazy dog"


def answer(sentence: str) -> tuple[str, int, list[str], str]:
    q1 = sentence.title()
    q2 = len(sentence.split())
    q3 = [word for word in sentence.split() if len(word) > 3]
    q4 = sentence.replace('fox', 'cat')
    return q1, q2, q3, q4


if __name__ == "__main__":
    answer(sentence=sentence)
