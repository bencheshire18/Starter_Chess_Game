def check_for_checkmate(board, status):
    for row in range(8):
        for col in range(8):
            piece = board.grid[row][col]
            if piece is None or piece.colour != status.active_player:
                continue

            legal_moves = piece.get_legal_moves([row, col], board, status, False)
            if legal_moves:
                return False, False

    if status.in_check:
        return True, False
    return False, True