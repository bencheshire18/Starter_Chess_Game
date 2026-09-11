from game.pieces.piece_rules.check_straight import check_straight
from game.pieces.piece import Piece
class Rook(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "R"
        elif colour == "black":
            symbol = "r"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")
        
        super().__init__("Rook", colour, symbol)

    def check_legal_moves(self, start, end, board, status):

        start_row = start[0]
        start_col = start[1]
        end_row   = end[0]
        end_col   = end[1]

        target_square = board.grid[end_row][end_col]

        # Checking start and end square are on the same rank or file
        if start_row != end_row and start_col != end_col:
            return False
    
        if start == end:
            #print("Start square is same as end square")
            return False

        row_range, col_range = check_straight(start, end)
        
        look_squares = zip(row_range, col_range)

        for rows, cols, in look_squares:
            if board.grid[rows][cols] is not None:
                #print("Path blocked!")
                return False

        # Now we've check all but the final square, we need to see if the final square is occupied by a friendly piece
        if target_square is not None and target_square.colour == self.colour:
            return False
        
        else:
            return True