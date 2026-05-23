'''
Problem 3

text = "the quick brown fox jumps over the lazy dog the fox"
Write a function that returns:

A dict of word frequencies e.g. {"the": 3, "fox": 2, ...}
The top 3 most frequent words as a list of tuples sorted by frequency descending e.g. [("the", 3), ("fox", 2), ...]
A dict of word frequencies but only for words longer than 3 characters
The number of unique words
'''

text = "the quick brown fox jumps over the lazy dog the fox"


def answer(text: str) -> tuple[dict[str, int], list[tuple[str, int]], dict[str, int], int]:
    q1 = {}
    for s in text.split(sep=' '):
        if s not in q1:
            q1[s] = 0
        q1[s] += 1

    # wrong: sorted(q1) sorts keys only, returns list of strings not tuples
    # also missing [:3] to get top 3 only
    # q2 = sorted(q1, key=lambda x: q1[x], reverse=True)
    q2 = sorted(q1.items(), key=lambda x: x[1], reverse=True)[:3]

    q3 = {}
    for s in text.split():  # text.split(sep=' ') is the same as text.split(), no need for sep arg
        if len(s) > 3:
            if s not in q3:
                q3[s] = 0
            q3[s] += 1

    # wrong: overcomplicated, q4 is not defined yet so len(q4) would error
    # q4 = 0
    # for keys in q1.keys():
    #     q4 += 1
    q4 = len(q1)

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(text=text)
