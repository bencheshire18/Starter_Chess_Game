def castle(self, moving_piece, status, start, end):
    if status.active_player == "white":
        if start == [7, 4] and moving_piece.symbol == "K":
            if end == [7, 6] and status.kingside_white_castling_available  == True:
                self.move_piece([7, 7], [7 , 5], status)

    if status.active_player == "white":
        if start == [7, 4] and moving_piece.symbol == "K":
            if end == [7, 2] and status.queenside_white_castling_available == True:
                self.move_piece([7, 0], [7 , 3], status)

    if status.active_player == "black":
        if start == [0, 4] and moving_piece.symbol == "k":
            if end == [0, 6] and status.kingside_black_castling_available  == True:
                self.move_piece([0, 7], [0 , 5], status)

    if status.active_player == "black":
        if start == [0, 4] and moving_piece.symbol == "k":
            if end == [0, 2] and status.queenside_black_castling_available == True:
                self.move_piece([0, 0], [0 , 3], status)

def remove_castling_rights(moving_piece, status, start):
    if moving_piece.symbol == "K":
        status.kingside_white_castling_available = False
        status.queenside_white_castling_available = False

    elif moving_piece.symbol == "k":
        status.kingside_black_castling_available = False
        status.queenside_black_castling_available = False

    elif moving_piece.symbol == "R":
        if start == [7, 7]:
            status.kingside_white_castling_available = False
        elif start == [7, 0]:
            status.queenside_white_castling_available = False

    elif moving_piece.symbol == "r":
        if start == [0, 7]:
            status.kingside_black_castling_available = False
        elif start == [0, 0]:
            status.queenside_black_castling_available = False

def castling_through_check(board, start, end, status):
    if start[0] == 7 and end[1] == 6:
        start_row = start[0]
        start_col = start[1]
        end_row = 7
        end_col = 5
        
        # Take the piece from the start position
        moving_piece = board.grid[start_row][start_col]
        end_square   = board.grid[end_row  ][end_col  ]

        # Place it at the destination
        board.grid[end_row][end_col] = moving_piece
        # Clear the starting square
        board.grid[start_row][start_col] = None

        result = board.is_check(status)

        board.grid[start_row][start_col] = moving_piece
        board.grid[end_row][end_col] = end_square

        return result

    elif start[0] == 7 and end[1] == 2:
        start_row = start[0]
        start_col = start[1]
        end_row = 7
        end_col = 3
        
        # Take the piece from the start position
        moving_piece = board.grid[start_row][start_col]
        end_square   = board.grid[end_row  ][end_col  ]

        # Place it at the destination
        board.grid[end_row][end_col] = moving_piece
        # Clear the starting square
        board.grid[start_row][start_col] = None

        result = board.is_check(status)

        board.grid[start_row][start_col] = moving_piece
        board.grid[end_row][end_col] = end_square

        return result

    elif start[0] == 0 and end[1] == 6:
        start_row = start[0]
        start_col = start[1]
        end_row = 0
        end_col = 5
        
        # Take the piece from the start position
        moving_piece = board.grid[start_row][start_col]
        end_square   = board.grid[end_row  ][end_col  ]

        # Place it at the destination
        board.grid[end_row][end_col] = moving_piece
        # Clear the starting square
        board.grid[start_row][start_col] = None

        result = board.is_check(status)

        board.grid[start_row][start_col] = moving_piece
        board.grid[end_row][end_col] = end_square

        return result

    elif start[0] == 0 and end[1] == 2:
        start_row = start[0]
        start_col = start[1]
        end_row = 0
        end_col = 3
        
        # Take the piece from the start position
        moving_piece = board.grid[start_row][start_col]
        end_square   = board.grid[end_row  ][end_col  ]

        # Place it at the destination
        board.grid[end_row][end_col] = moving_piece
        # Clear the starting square
        board.grid[start_row][start_col] = None

        result = board.is_check(status)

        board.grid[start_row][start_col] = moving_piece
        board.grid[end_row][end_col] = end_square

        return result