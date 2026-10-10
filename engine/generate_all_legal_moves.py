from game.pieces import Piece        

def generate_all_legal_moves(board, status):
    all_legal_moves = []
    for row in range(8):
        for col in range(8):
            square = board.grid[row][col]
            if square is not None and square.colour == status.active_player:
                start = [row, col]
                square_moves = square.get_legal_moves(start, board, status, False)
                for end in square_moves:
                    all_legal_moves.append([start, end])

    return all_legal_moves