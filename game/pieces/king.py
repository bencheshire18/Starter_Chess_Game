from game.pieces.piece import Piece
from game.pieces.piece_rules import castling

class King(Piece):
    def __init__(self, colour):
        if colour == "white":
            symbol = "K"
        elif colour == "black":
            symbol = "k"
        else:
            raise ValueError("Invalid colour, only 'white' or 'black' acceptable")
        
        super().__init__("King", colour, symbol)
    
    def check_legal_move(self, start, end, board, status):
        start_row = start[0]
        start_col = start[1]
        end_row   = end[0]
        end_col   = end[1]

        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)

        is_one_away = max(row_diff, col_diff) == 1

        target_square = board.grid[end_row][end_col]

        if self.colour == "white" and status.kingside_white_castling_available == True and status.in_check == False:
            if start == [7, 4] and end == [7, 6] and board.grid[7][5] is None and castling.castling_through_check(board, start, end, status) == False:
                return True

        if self.colour == "white" and status.queenside_white_castling_available == True and status.in_check == False:
            if start == [7, 4] and end == [7, 2] and board.grid[7][3] is None and castling.castling_through_check(board, start, end, status) == False:
                return True

        if self.colour == "black" and status.kingside_black_castling_available == True and status.in_check == False:
            if start == [0, 4] and end == [0, 6] and board.grid[0][5] is None and castling.castling_through_check(board, start, end, status) == False:
                return True

        if self.colour == "black" and status.queenside_black_castling_available == True and status.in_check == False:
            if start == [0, 4] and end == [0, 2] and board.grid[0][3] is None and castling.castling_through_check(board, start, end, status) == False:
                return True

        if not is_one_away:
            return False
        
        if target_square is not None and target_square.colour == self.colour:
            return False
        
        return True