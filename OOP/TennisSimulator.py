"""
Practice Question: Simplified Tennis Match Simulation

Scenario:
You need to simulate a tennis match between two players.
Each player has a serve win probability (a number between 0 and 1).
The match is best-of-3 sets. Each set is made of games, each game is made of points.

Simplified rules:
A game is won when a player reaches 4 points and leads by 2 points.
A set is won when a player reaches 6 games and leads by 2 games.
The match is won when a player wins 2 sets.

Simulate the match point by point, keeping track of:
Points won in each game
Games won in each set
Sets won
"""

import random


class Player:
    def __init__(self, name: str, prob: float) -> None:
        self.name = name
        self.prob = prob

        if 0 < self.prob > 1:
            raise ValueError("Value not between 0 and 1")


class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    def point_played(self) -> tuple[str, int]:
        player_1: Player = self.players[0]
        player_2: Player = self.players[1]

        if player_1.prob > random.random():
            return player_1.name
        else:
            return player_2.name

    def simulate_game(self, n_games: int, lead_required: int) -> Player:
        games_won: int = 0
        games_lead: int = 0

        game_state = {self.players[0].name: 0, self.players[1].name: 0}

        for x in range(10):
            player_name = self.point_played()
            game_state[player_name] += 1
        return game_state


player_1 = Player(name='Chris', prob=0.4)
player_2 = Player(name='John', prob=0.6)

players = [player_1, player_2]

game_1 = Game(players=players)
x = game_1.simulate_game(n_games=0, lead_required=1)
print(x)

grid = ([1, 2, 3], [4, 5, 6])

for i in grid[0]:
    for j in grid[1]:
        print(i, j)
