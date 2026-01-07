"""
Problem: Max Drawdown in Betting

You are tracking a player's betting history. Each bet contains:

- stake: amount wagered (int)
- odds: decimal odds (float)
- outcome: 1 if the bet won, 0 if it lost

Profit rules:
- If outcome == 1: profit = stake * (odds - 1)
- If outcome == 0: profit = -stake

Cumulative profit is the running total profit after each bet.

Max drawdown is defined as the largest drop from any historical peak
in cumulative profit to a subsequent trough.

Requirements:
- Write a function that takes a list of bets.
- Return the maximum drawdown as a float.
- If the player never experiences a drawdown, return 0.0.
- If no bets are given, return 0.0.
- Do not use external libraries.
- Aim for a single pass through the data.

Example:
bets = [
    (100, 2.0, 1),
    (50, 3.0, 0),
    (200, 1.5, 1),
    (100, 2.0, 0)
]

Cumulative profit progression:
- After bet 1: 100
- After bet 2: 50
- After bet 3: 150
- After bet 4: 50

Max drawdown: 100.0
"""


def max_drawdown(bets: list[tuple[int, float, int]]) -> float:

    if not bets:
        return 0.0

    cumulative_profit: float = 0.0
    max_profit: float = 0.0
    max_drawdown: float = 0.0

    for stake, odds, outcome in bets:
        # Update cumulative profit based on win or loss
        if outcome == 1:
            cumulative_profit += stake * (odds - 1)
        else:
            cumulative_profit += -stake

        # Update peak profit if cumulative is higher
        if cumulative_profit > max_profit:
            max_profit = cumulative_profit

        # Compute current drawdown and update max_drawdown
        current_drawdown = max_profit - cumulative_profit
        if current_drawdown > max_drawdown:
            max_drawdown = current_drawdown

    return max_drawdown


if __name__ == "__main__":

    bets = [
        (100, 2.0, 1),
        (50, 3.0, 0),
        (200, 1.5, 1),
        (100, 2.0, 0)
    ]
    output = max_drawdown(bets=bets)
    print(output)
