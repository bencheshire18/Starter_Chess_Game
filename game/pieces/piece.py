class Piece:
    def __init__(self, name, colour, symbol):
        self.name   = name
        self.colour = colour
        self.symbol = symbol
    
    def get_legal_moves(self, start, board, status, trimming):
        valid_moves = []

        if self.colour != status.active_player and trimming == False:
            valid_moves = []
        else:
            for rows in range(8):
                for cols in range(8):
                    move = self.check_legal_move(start, [rows, cols], board, status)
                    if move: valid_moves.append([rows, cols])
        
        return valid_moves