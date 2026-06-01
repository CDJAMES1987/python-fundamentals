'''Problem 3

Write a function filter_and_transform that:

Takes a list of numbers
Takes an optional min_val (default 0) — filter out anything below this
Takes an optional transform (default None) — a function to apply to each number
Takes an optional reverse (default False) — whether to sort descending
Returns the filtered, transformed, sorted list
'''


def filter_and_transform(numbers: list[int | float], min_value: int = 0, transform=None, reverse=False) -> list[int]:
    filtered = []
    for number in numbers:
        if number >= min_value:
            filtered.append(number)
    transformed = []
    if transform is not None:
        for number in filtered:
            transformed.append(transform(number))
    else:
        transformed = filtered
    return sorted(transformed, reverse=reverse)


if __name__ == '__main__':
    filter_and_transform([1, 2, 3, 4, 5], min_value=2, reverse=True)
