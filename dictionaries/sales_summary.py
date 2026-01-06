sales = {
    "apple": [5, 3, 4, 2, 6],      # units sold each day
    "banana": [2, 2, 3, 1, 4],
    "orange": [0, 1, 1, 2, 1],
    "mango": [1, 0, 2, 3, 1]
}

def sales_summary(sales: dict) -> tuple[dict, dict]:
    """
    Compute total and average sales per fruit.

    Args:
        sales (dict): Dictionary where each key is a fruit name (str)
                      and each value is a list of integers representing
                      units sold each day.

    Returns:
        tuple:
            - total_sold (dict): Total units sold per fruit.
            - average_sold (dict): Average units sold per day per fruit.

    Example:
        >>> sales_summary(sales)
        (
            {'apple': 20, 'banana': 12, 'orange': 5, 'mango': 7},
            {'apple': 4.0, 'banana': 2.4, 'orange': 1.0, 'mango': 1.4}
        )
    """
    # Step 1: Compute total units sold
    total_sold: dict = {}
    for fruit, units_sold in sales.items():
        total_sold[fruit] = 0
        for units in units_sold:
            total_sold[fruit] += units

    # Step 2: Count days per fruit
    count_dict: dict = {}
    for fruit, units_sold in sales.items():
        count_dict[fruit] = 0
        for _ in units_sold:
            count_dict[fruit] += 1

    # Step 3: Compute average units sold per day
    average_sold: dict = {}
    for fruit in total_sold:
        average_sold[fruit] = total_sold[fruit] / count_dict[fruit]

    return total_sold, average_sold

if __name__ == "__main__":
    total, average = sales_summary(sales)
    print("Total Sold:", total)
    print("Average Sold:", average)

