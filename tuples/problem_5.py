'''races = (
    ("Alice", "5K", 22.5),
    ("Bob", "10K", 55.3),
    ("Alice", "10K", 48.2),
    ("Charlie", "5K", 19.8),
    ("Bob", "5K", 21.1),
    ("Charlie", "10K", 52.6)
)
Each tuple is (runner, race_type, time_in_minutes).

Write a function that returns:

The fastest time per race type as a dict e.g. {"5K": 19.8, "10K": 48.2}
The fastest runner per race type as a dict e.g. {"5K": "Charlie", "10K": "Alice"}
All of Alice's races sorted by time ascending
'''
races = (
    ("Alice", "5K", 22.5),
    ("Bob", "10K", 55.3),
    ("Alice", "10K", 48.2),
    ("Charlie", "5K", 19.8),
    ("Bob", "5K", 21.1),
    ("Charlie", "10K", 52.6)
)


def answer(races: tuple[tuple[str, str, float]]) -> tuple[dict[str, float], dict[str, str], list[tuple[str, str, float]]]:
    q1 = {}
    q2 = {}

    for runner, race_type, time_in_minutes in races:
        if race_type not in q1:
            q1[race_type] = time_in_minutes
            q2[race_type] = runner
        elif time_in_minutes < q1[race_type]:
            q1[race_type] = time_in_minutes
            q2[race_type] = runner

    q3 = sorted([r for r in races if r[0] == 'Alice'], key=lambda x: x[2])

    return q1, q2, q3


if __name__ == '__main__':
    answer(races=races)
