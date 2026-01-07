"""
Problem:

You are tracking bets for a sportsbook. Each bet has:
-stake: the amount wagered
-odds: decimal odds
-outcome: 1 if the bet won, 0 if lost

Write a function expected_profit(bets) that returns total profit 
and ROI (total profit divided by total stake).

bets is a list of tuples (stake, odds, outcome)

Return two floats (total_profit, roi)

If no bets are given, return (0.0, 0.0)

Example:
bets = [(100, 2.0, 1), (50, 3.0, 0), (200, 1.5, 1)]
expected_profit(bets)  

returns (150.0, 0.428)

"""


def expected_profit(bets: list[tuple[int, float, int]]) -> tuple[float, float]:
    """
    Expected profit takes in a list of bets containing the wager, odds, and outcome
    and returns the total profit and roi for all bets

    Args:
        bets: list[tuple[int, float, int]] -> stake, odds, outcome

    Returns:
        tuple[float, float]: total_profit, roi

    """

    if not bets:
        return 0.0, 0.0

    amount_won: float = 0.0
    amount_lost: float = 0.0
    total_profit: float = 0.0

    # Calculate total profits
    for bet in bets:
        if bet[2] == 1:
            amount_won += bet[0] * (bet[1] - 1)
        else:
            amount_lost += bet[0]
    total_profit = amount_won - amount_lost

    # Calculate total stake
    total_stake: int = 0
    for bet in bets:
        total_stake += bet[0]

    # Calculate ROI
    roi = total_profit / total_stake

    return total_profit, roi


if __name__ == "__main__":
    bets = [(100, 2.0, 1), (50, 3.0, 0), (200, 1.5, 1)]
    total_profit, roi = expected_profit(bets=bets)
    print(f"Total Profit: {total_profit}")
    print(f"ROI: {roi}")
