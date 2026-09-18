import random
import sys

for i in range(10000):
    all_legal_moves = [
        [[0, 0], [0, 1]], [[0, 0], [0, 2]], [[0, 0], [0, 3]],
        [[1, 0], [1, 4]], [[1, 0], [1, 5]], [[1, 0], [1, 6]],
        [[2, 0], [2, 7]], [[2, 0], [2, 8]], [[2, 0], [2, 9]],
    ]

    # pick a random starter from all_legal_moves
    starter = random.choice(all_legal_moves)[0]

    # pick a random end that relates to that starter
    options = [move[1] for move in all_legal_moves if move[0] == starter]
    end = random.choice(options)

    if starter[0] != end[0]:
        print("Failed!!")
        sys.exit()

print("Succeeded")
