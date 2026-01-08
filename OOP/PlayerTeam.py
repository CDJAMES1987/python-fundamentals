"""
Classes: Player and Team

Player:
Attributes: name, position, points (default 0)
Methods: score_points(n), reset_points()

Team:
Attributes: name, players (list of Player objects)
Methods: add_player(player), total_points() (sum of all players’ points), top_scorer() (returns Player object with highest points)

Practice: Interacting objects, looping over a list of objects, calling methods on contained objects.
"""


class Player:
    def __init__(self, name: str, position: str, points: int = 0) -> None:
        self.name: str = name
        self.position: str = position
        self.points: int = points

    def score_points(self, n_points: int) -> None:
        self.points += n_points

    def reset_points(self) -> None:
        self.points = 0


class Team:
    def __init__(self, name: str, players: list[Player]) -> None:
        self.name: str = name
        self.players: list[Player] = players

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def total_points(self) -> int:
        total_points: int = 0

        for player in self.players:
            if player.points < 0:
                raise ValueError("Points cannot be negative")
            total_points += player.points
        return total_points

    def top_scorer(self) -> Player:
        if not self.players:
            raise ValueError("Team has no players")

        max_points: int = -1
        top_player: Player | None = None

        for player in self.players:
            if player.points > max_points:
                max_points = player.points
                top_player = player

        return top_player


def main():
    # Create some Player objects
    player1 = Player(name='Chris', position='Guard', points=10)
    player2 = Player(name='John', position='Forward', points=100)
    player3 = Player(name='Mike', position='Center', points=20)

    # Create a Team with the players
    team = Team(name='Eagles', players=[player1, player2, player3])

    # Use Team methods
    print(f"Total points: {team.total_points()}")
    top_scorer = team.top_scorer()
    print(f"Top scorer: {top_scorer.name} with {top_scorer.points} points")


if __name__ == "__main__":
    main()
