from game.pieces.piece_rules.check_diag import check_diag
from game.pieces.piece      import Piece

class Bishop(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "B"
        elif colour == "black":
            symbol = "b"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")
        
        super().__init__("Bishop", colour, symbol)
    
    def check_legal_moves(self, start, end, board, status):
        start_row = start[0]
        start_col = start[1]
        end_row   = end[0]
        end_col   = end[1]

        target_square = board.grid[end_row][end_col]

        if start == end:
            return False

        row_diff = start_row - end_row
        col_diff = start_col - end_col

        is_diag = abs(row_diff) == abs(col_diff)

        if not is_diag:
            return False
        
        row_range, col_range = check_diag(start, end)

        # Check square returned from check_diag
        look_squares = zip(row_range, col_range)
        for rows, cols, in look_squares:
            if board.grid[rows][cols] is not None:
                #print("Path blocked!")
                return False

        # Check if target square is occupied by friendly piece
        if target_square is not None and target_square.colour == self.colour:
            #print("End square is friendly piece")
            return False
        
        return True