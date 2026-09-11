from game.pieces.piece_rules.check_straight import check_straight
from game.pieces.piece_rules.check_diag     import check_diag
from game.pieces.piece          import Piece

class Queen(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "Q"
        elif colour == "black":
            symbol = "q"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")
        
        super().__init__("Queen", colour, symbol)

    def check_legal_moves(self, start, end, board, status):
        start_row = start[0]
        start_col = start[1]
        end_row   = end[0]
        end_col   = end[1]

        target_square = board.grid[end_row][end_col]

        row_diff = start_row - end_row
        col_diff = start_col - end_col

        is_diag = abs(row_diff) == abs(col_diff)
        is_straight = start_row == end_row or start_col == end_col

        if start == end:
            #print("same-square move")
            return False
        elif is_diag:
            row_range, col_range = check_diag(start, end)
        elif is_straight:
            row_range, col_range = check_straight(start, end)
        elif not is_diag and not is_straight:
            #print("Move not geometrically correct")
            return False
        
        look_squares = zip(row_range, col_range)

        for rows, cols, in look_squares:
            if board.grid[rows][cols] is not None:
                #print("Path blocked!")
                return False
            
         # Now we've check all but the final square, we need to see if the final square is occupied by a friendly piece
        if target_square is not None and target_square.colour == self.colour:
            return False
        
        return True