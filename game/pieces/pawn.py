from game.pieces.piece import Piece
from game.pieces.piece_rules import en_passant

class Pawn(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "P"
        elif colour == "black":
            symbol = "p"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")
        
        super().__init__("Pawn", colour, symbol)
        
    def check_legal_move(self, start, end, board, status):
        start_row = start[0]
        start_col = start[1]
        end_row   = end[0]
        end_col   = end[1]
        
        target_square = board.grid[end_row][end_col]

        if en_passant.check_en_passant(start, end, board, status):
            return True

        if start == end:
            #print("same-square move")
            return False
        
        # Forwards move (no capturing)
        if start_col == end_col:
            if self.colour == "white":
                if   start_row - end_row == 1 and target_square is None:
                    return True
                elif start_row - end_row == 2 and target_square is None and start_row == 6 and board.grid[end_row+1][end_col] is None:
                    return True
                else:
                    return False
            elif self.colour == "black":
                if   end_row - start_row == 1 and target_square is None:
                    return True
                elif end_row - start_row == 2 and target_square is None and start_row == 1 and board.grid[end_row-1][end_col] is None:
                    return True
                else: 
                    return False        
        # Diagonal by one (capturing)
        elif abs(start_col - end_col) == 1:
            if target_square is None:
                return False
            elif self.colour == "white":
                if start_row - end_row == 1 and target_square.colour == "black":
                    return True
                else:
                    return False
            elif self.colour == "black":
                if end_row - start_row == 1 and target_square.colour == "white":
                    return True
                else:
                    return False
        else:
            return False

        return True