'''
Problem 1

sales = {
    "January": 12500,
    "February": 9800,
    "March": 15200,
    "April": 11300,
    "May": 17600,
    "June": 14100
}
Write a function that returns:

The month with the highest sales
A new dict with only months where sales exceeded 12000
Total sales across all months
A new dict with each month's sales as a percentage of total sales (rounded to 1 decimal place) e.g. {"January": 15.2, ...}
'''

sales = {
    "January": 12500,
    "February": 9800,
    "March": 15200,
    "April": 11300,
    "May": 17600,
    "June": 14100
}


def answer(sales: dict[str, int]) -> tuple[str, dict[str, int], int, dict[str, float]]:

    # curr_max = sales['January'] fragile, hardcoded, use another approach

    # for key, value in sales.items():
    #     if curr_max < value:
    #         curr_max = value
    #         q1 = key

    q1 = max(sales, key=lambda x: sales[x])

    # overcomplicated, initialzed to 0, then deleting, if still 0
    # The rule: if you're using += or .append(), initialise first.
    # If you're just assigning with =, you don't need to
    #
    # q2 = {}
    # for key, value in sales.items():
    #     if key not in q2:
    #         q2[key] = 0
    #     if value > 12000:
    #         q2[key] = value
    #     if q2[key] == 0:
    #         del q2[key]

    q2 = {}
    for key, value in sales.items():
        if value > 12000:
            q2[key] = value

    # fine, but easier one liner
    # q3 = 0
    # for key, value in sales.items():
    #     q3 += value

    q3 = sum(sales.values())

    q4 = {}
    for key, value in sales.items():
        q4[key] = round((value/q3) * 100, 1)

    return q1, q2, q3, q4


if __name__ == '__main__':
    answer(sales=sales)
