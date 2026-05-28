'''
Problem 3

visited_alice = {"Paris", "London", "Tokyo", "New York", "Sydney"}
visited_bob = {"London", "Berlin", "Tokyo", "Dubai", "Paris"}
visited_charlie = {"Sydney", "Dubai", "Cairo", "Tokyo", "Rome"}

Write a function that returns:

Cities visited by all three
Cities visited by Alice or Bob but not Charlie
Cities only Alice has visited
Number of cities visited by at least two people
All unique cities visited across everyone

'''

visited_alice = {"Paris", "London", "Tokyo", "New York", "Sydney"}
visited_bob = {"London", "Berlin", "Tokyo", "Dubai", "Paris"}
visited_charlie = {"Sydney", "Dubai", "Cairo", "Tokyo", "Rome"}


def answer(visited_alice: set[str], visited_bob: set[str], visited_charlie: set[str]) -> tuple[set[str], set[str], set[str], int, set[str]]:
    q1 = visited_alice.intersection(visited_bob, visited_charlie)
    q2 = (visited_alice | visited_bob) - visited_charlie
    q3 = visited_alice.difference(visited_bob, visited_charlie)
    q4 = len((visited_alice & visited_bob) | (visited_alice &
             visited_charlie) | (visited_bob & visited_charlie))
    q5 = visited_alice.union(visited_bob, visited_charlie)
    return q1, q2, q3, q4, q5


if __name__ == '__main__':
    answer(visited_alice=visited_alice, visited_bob=visited_bob,
           visited_charlie=visited_charlie)
