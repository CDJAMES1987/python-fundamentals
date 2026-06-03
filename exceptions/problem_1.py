'''
Problem 1

def divide(a, b):
    pass

def get_list_item(lst, index):
    pass

def convert_to_int(value):
    pass

Implement all three with proper error handling:

divide — handle division by zero, return None if it occurs
get_list_item — handle index out of range, return None if it occurs
convert_to_int — handle invalid conversion, return None if it occurs
'''


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_list_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


if __name__ == '__main__':
    divide(4, 0)
    get_list_item(lst=[1, 2, 3], index=2)
    convert_to_int('A')
