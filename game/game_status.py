class GameStatus:
    def __init__(self):
        self.active_player = "white"
        self.kingside_white_castling_available = True
        self.queenside_white_castling_available = True
        self.kingside_black_castling_available = True
        self.queenside_black_castling_available = True
        self.in_check = False
        self.en_passant_available = []

    def toggle_turn(self):
        self.active_player = "black" if self.active_player == "white" else "white"