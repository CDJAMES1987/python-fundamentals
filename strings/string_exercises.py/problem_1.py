'''
Problem 1


sentence = "the quick brown fox jumps over the lazy dog"
Write a function that returns:

The sentence in title case (every word capitalised)
The number of words in the sentence
A list of all words longer than 3 characters
The sentence with "fox" replaced by "cat"

'''

sentence = "the quick brown fox jumps over the lazy dog"


def answer(sentence: str) -> tuple[str, int, list[str], str]:
    q1 = sentence.title()
    q2 = len(sentence.split())

    q3 = []
    for word in sentence.split():
        if len(word) > 3:
            q3.append(word)

    q4 = sentence.replace('fox', 'cat')

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(sentence=sentence)
