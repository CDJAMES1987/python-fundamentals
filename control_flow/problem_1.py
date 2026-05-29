'''
Problem 1 — while loop

Write a function that takes a positive integer n and returns a list of all numbers from n down to 1 using a while loop.
countdown(10)  →  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''

print('Enter postive integer:')
user_input = input()
user_input = int(user_input)

if user_input <= 0:
    raise ValueError('Input value must be non-negative')
else:
    print('Value entered correctly')


def countdown(n: int) -> list[int]:
    output = []
    while n > 0:
        output.append(n)
        n -= 1

    return output


if __name__ == '__main__':
    countdown(n=user_input)
