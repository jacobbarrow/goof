from game import Game
import approaches

NUM_REPEATS = 10000

players = [
    approaches.Random("rAnDoM"),
    approaches.PlusOne("+1")
]


scores = {}
for player in players:
    scores[player.name] = 0

g = Game(players)


for _ in range(NUM_REPEATS):

    g.play()

    for player in players:
        scores[player.name] += player.score

    g.reset()

print("Mean Scores:")
for player, total_score in scores.items():
    print(f'{player}\t {round(total_score / NUM_REPEATS)}')