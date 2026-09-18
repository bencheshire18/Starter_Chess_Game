def check_for_checkmate(board, status):
    checkmate_counter = 0
    for rows in range(8):
        for cols in range(8):
            check_start = [rows, cols]
            checking_piece = board.grid[rows][cols]
            if checking_piece is not None and checking_piece.colour == status.active_player:
                checking_legal_moves = checking_piece.get_legal_moves(check_start, board, status, False)
                checking_legal_moves = board.trim_legal_moves(check_start, checking_legal_moves, status)
                if checking_legal_moves != []:
                    checkmate_counter += 1

    return checkmate_counter