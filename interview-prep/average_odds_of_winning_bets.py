"""
Problem:

You are given a list of bets, where each bet is represented by a tuple:
- stake: the amount wagered (integer)
- odds: decimal odds (float)
- outcome: 1 if the bet won, 0 if lost

Write a function `average_odds_of_winning_bets(bets)` that returns the
average odds of all winning bets.

- If there are no winning bets, return 0.0.

bets is a list of tuples: (stake, odds, outcome)

Return:
- A float representing the average odds of winning bets.

Example:
bets = [(100, 2.0, 1), (50, 3.0, 0), (200, 1.5, 1), (100, 2.5, 1)]
average_odds_of_winning_bets(bets)

returns 2.0
"""


def average_odds_of_winning_bets(bets: list[tuple[int, float, int]]) -> float:

    if not bets:
        return 0.0

    total_odds: float = 0
    total_winning_bets: int = 0
    for stake, odds, outcome in bets:
        if outcome == 1:
            total_odds += odds
            total_winning_bets += 1

    average_odds_of_winning_bets = total_odds / total_winning_bets

    return average_odds_of_winning_bets


if __name__ == "__main__":

    bets = [(100, 2.0, 1), (50, 3.0, 0), (200, 1.5, 1), (100, 2.5, 1)]
    output = average_odds_of_winning_bets(bets)
    print(output)
