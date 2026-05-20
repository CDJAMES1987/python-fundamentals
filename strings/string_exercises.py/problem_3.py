'''
Problem 3


text = "Hello World this is Python Programming"
Write a function that returns:

A list of words that start with a capital letter
The text as a single lowercase string with all spaces replaced by underscores
How many times the letter "o" appears in the text (case insensitive)
'''

text = "Hello World this is Python Programming"


def answer(text: str) -> tuple[list[str], str, int]:
    q1 = []
    q2 = text.lower().replace(" ", "_")

    for word in text.split(" "):
        if word[0].isupper():
            q1.append(word)

    q3 = text.lower().count('o')

    return q1, q2, q3


if __name__ == '__main__':
    answer(text=text)
