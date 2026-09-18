from game.pieces.piece import Piece

class Knight(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "N"
        elif colour == "black":
            symbol = "n"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")

        super().__init__("Knight", colour, symbol)
    
    def check_legal_move(self, start, end, board, status):

        if start == end:
            return False

        start_row = start[0]
        end_row   = end[0]
        start_col = start[1]
        end_col   = end[1]

        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)

        is_l_shape = row_diff * col_diff == 2

        if not is_l_shape:
            #print("Geometrically incorrect")
            return False
        
        target_square = board.grid[end_row][end_col]

        if target_square is not None and target_square.colour == self.colour:
            #print("Square occupied by friendly piece")
            return False
        
        return True