import game.constants as c

def evaluate(board):
    # Start by going through all squares and just counting up material
    score = 0
    for row in range (8):
        for col in range(8):
            active_piece = board.grid[row][col]
            if active_piece is not None: symbol = str.upper(active_piece.symbol)
            if active_piece is not None:
                if active_piece.colour == "white":
                    score += c.PIECE_VALUES[symbol]
                else:
                    score -= c.PIECE_VALUES[symbol]

    # Now I want to prioritise pawns in the middle of the board
    for row in [3, 4]:
        for col in [3, 4]:
            active_piece = board.grid[row][col]
            if active_piece is not None:
                if active_piece.name == "Pawn":
                    if active_piece.colour == "white":
                        score += c.CENTRAL_PAWN
                    else:
                        score -= c.CENTRAL_PAWN

    # penalise knights on the edge of the board
    for row in range(8):
        for col in [0, 7]:
            active_piece = board.grid[row][col]
            if active_piece is not None:
                if active_piece.name == "Knight":
                    if active_piece.colour == "white":
                        score += c.EDGE_KNIGHT
                    else:
                        score -= c.EDGE_KNIGHT
    for col in range(1, 7):
        for row in [0, 7]:
            active_piece = board.grid[row][col]
            if active_piece is not None:
                if active_piece.name == "Knight":
                    if active_piece.colour == "white":
                        score += c.EDGE_KNIGHT
                    else:
                        score -= c.EDGE_KNIGHT
    return score