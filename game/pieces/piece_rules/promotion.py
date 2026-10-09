from game.pieces import King, Rook, Knight, Queen

def promote_pawn(board):
    # Checking first rank
    for col in range(8):
        if board.grid[0][col] is not None and board.grid[0][col].symbol == "P":
            print(f"Promoting white pawn at (0, {col})")
            board.place_piece(Queen("white"), 0, col)

    for col in range(8):
        if board.grid[7][col] is not None and board.grid[7][col].symbol == "p":
            print(f"Promoting black pawn at (7, {col})")
            board.place_piece(Queen("black"), 7, col)