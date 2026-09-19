def check_en_passant(start, end, board, status):
    ep = status.en_passant_available
    if not ep or end != ep:
        return False

    piece = board.grid[start[0]][start[1]]
    if piece is None or piece.name != "Pawn":
        return False

    # The ep square must be empty, and the pawn to be captured must be beside the capturer
    if board.grid[end[0]][end[1]] is not None:
        return False
    victim = board.grid[start[0]][end[1]]
    if victim is None or victim.name != "Pawn" or victim.colour == piece.colour:
        return False

    if abs(start[1] - end[1]) != 1:
        return False

    # White just double-pushed -> ep square is on row 5 -> black pawn on row 4 captures
    if end[0] == 5:
        return piece.colour == "black" and start[0] == 4
    # Black just double-pushed -> ep square is on row 2 -> white pawn on row 3 captures
    if end[0] == 2:
        return piece.colour == "white" and start[0] == 3

    return False