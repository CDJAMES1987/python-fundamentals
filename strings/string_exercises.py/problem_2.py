'''words = ["hello", "world", "python", "is", "great"]
Write a function that returns:

A single string of all words joined by a hyphen e.g. "hello-world-python-is-great"
A list of all words reversed e.g. ["olleh", "dlrow", ...]
A list of all words in uppercase
The longest word in the list
'''

words = ["hello", "world", "python", "is", "great"]


def answer(words: list[str]) -> tuple[str, list[str], list[str], str]:
    q2 = []
    q3 = []
    max_word = words[0]
    q1 = '-'.join(words)

    for word in words:
        q2.append(word[::-1])
        q3.append(word.upper())
        if len(max_word) < len(word):
            max_word = word
    return q1, q2, q3, max_word


if __name__ == '__main__':
    answer(words=words)
