'''
Problem 4

Write a function stats that takes any number of numbers and returns a dict with:

"count" — how many numbers
"sum" — total
"mean" — average rounded to 2 decimal places
"min" — smallest
"max" — largest
"range" — difference between max and min

'''


def stats(*args: int) -> dict[str, int]:
    stat_dict = {}
    stat_dict['count'] = len(args)
    stat_dict['sum'] = sum(args)
    stat_dict['mean'] = round(sum(args) / len(args), 2)
    stat_dict['min'] = min(args)
    stat_dict['max'] = max(args)
    stat_dict['range'] = max(args) - min(args)
    return stat_dict


if __name__ == '__main__':
    stats(4, 2, 7, 9, 1, 5)
