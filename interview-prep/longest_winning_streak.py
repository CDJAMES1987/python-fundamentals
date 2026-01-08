"""
Problem:

You are tracking a player’s betting history. Each bet has:
- stake: the amount wagered
- odds: decimal odds
- outcome: 1 if the bet won, 0 if lost

Write a function `longest_winning_streak(bets)` that returns the length of the **longest consecutive winning streak**.

bets is a list of tuples: (stake, odds, outcome)

Return an integer representing the maximum number of consecutive wins.

If no bets are given, return 0.

Example:
bets = [(100, 2.0, 1), (50, 3.0, 1), (200, 1.5, 0), (100, 2.0, 1), (50, 1.8, 1), (100, 2.5, 1)]
longest_winning_streak(bets)

returns 3

"""


def longest_winning_streaks(bets: list[tuple[int, float, int]]) -> int:

    winning_streak: int = 0
    max_streak: int = 0

    if not bets:
        return 0

    for stake, odds, outcome in bets:
        if outcome == 1:
            winning_streak += 1
        else:
            winning_streak = 0

        if winning_streak > max_streak:
            max_streak = winning_streak

    return max_streak


if __name__ == "__main__":
    bets = [(100, 2.0, 1), (50, 3.0, 1), (200, 1.5, 0),
            (100, 2.0, 1), (50, 1.8, 1), (100, 2.5, 1)]

    output = longest_winning_streaks(bets=bets)
    print(output)
