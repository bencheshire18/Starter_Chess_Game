def check_en_passant(start, end, board, status):
    start_row = start[0]
    start_col = start[1]

    if status.en_passant_available != []:
        en_passant_col = status.en_passant_available[1]

    if end == status.en_passant_available and abs(start_col - en_passant_col) == 1 and abs(end[0] - start_row) == 1:
        return True
