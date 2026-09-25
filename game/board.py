from game.constants import BOARD_SIZE
from game.pieces    import Rook, Knight, Bishop, Queen, King, Pawn
from game.pieces.piece_rules import castling, en_passant, check_for_checkmate

class Board:
    def __init__(self):
        self.grid = self.create_grid()

    # Create initial empty grid
    def create_grid(self):
        grid = []
        for row in range(BOARD_SIZE):
            grid.append([])
            for column in range(BOARD_SIZE):
                grid[row].append(None)
        return grid
    
    # This is how we place pieces
    def place_piece(self, piece, row, column):
        self.grid[row][column] = piece

    # Setup the start board
    def setup_board(self):
        # White pieces
        self.place_piece(Rook  ("white"), 7, 0)
        self.place_piece(Knight("white"), 7, 1)
        self.place_piece(Bishop("white"), 7, 2)
        self.place_piece(Queen ("white"), 7, 3)
        self.place_piece(King  ("white"), 7, 4)
        self.place_piece(Bishop("white"), 7, 5)
        self.place_piece(Knight("white"), 7, 6)
        self.place_piece(Rook  ("white"), 7, 7)
        for i in range(BOARD_SIZE):
           self.place_piece(Pawn("white"), 6, i)

        # Black pieces
        self.place_piece(Rook  ("black"), 0, 0)
        self.place_piece(Knight("black"), 0, 1)
        self.place_piece(Bishop("black"), 0, 2)
        self.place_piece(Queen ("black"), 0, 3)
        self.place_piece(King  ("black"), 0, 4)
        self.place_piece(Bishop("black"), 0, 5)
        self.place_piece(Knight("black"), 0, 6)
        self.place_piece(Rook  ("black"), 0, 7)
        for i in range(BOARD_SIZE):
            self.place_piece(Pawn("black"), 1, i)

    # Move a piece
    def move_piece(self, start, end, status):
        start_row, start_col = start
        end_row, end_col = end

        moving_piece = self.grid[start_row][start_col]

        # Rejected moves must not change any state
        if moving_piece is None:
            return False
        if moving_piece.colour != status.active_player:
            return False
        if not moving_piece.check_legal_move([start_row, start_col], [end_row, end_col], self, status):
            return False

        # Decide en passant BEFORE anything is changed
        is_en_passant = (
            moving_piece.name == "Pawn"
            and end == status.en_passant_available
            and start_col != end_col
            and self.grid[end_row][end_col] is None
        )

        # Only a double pawn push creates new rights; every other move clears them
        new_en_passant = []
        if moving_piece.symbol == "P" and start_row == 6 and end_row == 4:
            new_en_passant = [5, start_col]
        elif moving_piece.symbol == "p" and start_row == 1 and end_row == 3:
            new_en_passant = [2, start_col]

        castling.castle(self, moving_piece, status, start, end)
        castling.remove_castling_rights(moving_piece, status, start)

        # The captured pawn is beside the capturer: same row as start, same column as end
        if is_en_passant:
            self.grid[start_row][end_col] = None

        # Capturing a rook on its home square removes that castling right
        target = self.grid[end_row][end_col]
        if target is not None and target.name == "Rook":
            if end == [7, 0]:
                status.queenside_white_castling_available = False
            elif end == [7, 7]:
                status.kingside_white_castling_available = False
            elif end == [0, 0]:
                status.queenside_black_castling_available = False
            elif end == [0, 7]:
                status.kingside_black_castling_available = False

        self.grid[end_row][end_col] = moving_piece
        self.grid[start_row][start_col] = None

        # Set last, so the recursive rook move inside castle() can't overwrite it
        status.en_passant_available = new_en_passant
        status.toggle_turn()
        checkmate_counter = check_for_checkmate.check_for_checkmate(self, status)

        if checkmate_counter == 0:
            status.checkmate = True

        return True
    
    def would_be_in_check(self, start, end, status):
        start_row = start[0]
        start_col = start[1]
        end_row = end[0]
        end_col = end[1]

        # Take the piece from the start position
        moving_piece = self.grid[start_row][start_col]
        end_square   = self.grid[end_row  ][end_col  ]

        #Check if square has a piece
        if moving_piece is None or moving_piece.colour != status.active_player:
            return False

        # Place it at the destination
        self.grid[end_row][end_col] = moving_piece
        # Clear the starting square
        self.grid[start_row][start_col] = None

        result = self.is_check(status)

        self.grid[start_row][start_col] = moving_piece
        self.grid[end_row][end_col] = end_square

        return result

    # TODO optimise check algorithm so it doesn't check every square every time. Maybe add a callout in the move_piece function?
    def is_check(self, status):
        # Find the king
        active_king = []
        for rows in range(8):
            for cols in range(8):
                square = self.grid[rows][cols]
                if square is not None and square.name == "King" and square.colour == status.active_player:
                    active_king = [rows, cols]
                    break
        
        # If one of the opposing piece's legal moves can attack the king, return True
        for rows in range(8):
            for cols in range(8):
                square = self.grid[rows][cols]
                if square is not None and square.colour != status.active_player:
                    start = [rows, cols]
                    moves = square.get_legal_moves(start, self, status, True)
                    if active_king in moves:
                        return True
        
        return False
    
    def trim_legal_moves(self, start, legal_moves, status):
        temp_moves = []
        for moves in legal_moves:
            temp_moves.append(moves)

        for moves in legal_moves:
            if self.would_be_in_check(start, moves, status):
                temp_moves.remove(moves)
        
        return temp_moves

    # Debugging method
    def display(self):
        """Print the board to terminal."""
        for row in self.grid:
            row_display = []
            for square in row:
                if square is None:
                    row_display.append(".")
                else:
                    row_display.append(square.symbol)
            print(" ".join(row_display))

    def display_legal_moves(self, legal_moves):
        """Print the board with legal destination squares marked as '*'."""
        for row_index, row in enumerate(self.grid):
            row_display = []
            for col_index, square in enumerate(row):
                if [row_index, col_index] in legal_moves:
                    row_display.append("*")
                elif square is None:
                    row_display.append(".")
                else:
                    row_display.append(square.symbol)
            print(" ".join(row_display))