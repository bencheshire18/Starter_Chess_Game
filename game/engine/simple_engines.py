import random

def make_random_move(all_legal_moves, board, status):
    # pick a random starter from all_legal_moves
    start = random.choice(all_legal_moves)[0]

    # pick a random end that relates to that starter
    options = [move[1] for move in all_legal_moves if move[0] == start]
    end = random.choice(options)

    board.move_piece(start, end, status)