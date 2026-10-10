import random


PIECE_VALUES = {
    "Pawn": 1,
    "Knight": 3,
    "Bishop": 3,
    "Rook": 5,
    "Queen": 9,
    "King": 100,
}


def _score_move(move, board, status):
    start, end = move
    start_row, start_col = start
    end_row, end_col = end
    moving_piece = board.grid[start_row][start_col]
    captured_piece = board.grid[end_row][end_col]
    score = 0

    if captured_piece is not None:
        score += PIECE_VALUES[captured_piece.name] * 10
    elif (
        moving_piece.name == "Pawn"
        and start_col != end_col
        and end == status.en_passant_available
    ):
        score += PIECE_VALUES["Pawn"] * 10

    # Prefer advancing pawns toward promotion and promoting when possible.
    if moving_piece.name == "Pawn":
        advancement = start_row - end_row if moving_piece.colour == "white" else end_row - start_row
        score += advancement
        if end_row in (0, 7):
            score += PIECE_VALUES["Queen"] - PIECE_VALUES["Pawn"]

    # Give a small preference to controlling the centre.
    center_distance = abs(end_row - 3.5) + abs(end_col - 3.5)
    score += 3.5 - center_distance

    return score


def make_move(all_legal_moves, board, status):
    """Play the highest-scoring legal move, breaking ties randomly."""
    if not all_legal_moves:
        return False

    best_score = max(_score_move(move, board, status) for move in all_legal_moves)
    best_moves = [
        move for move in all_legal_moves
        if _score_move(move, board, status) == best_score
    ]
    start, end = random.choice(best_moves)
    return board.move_piece(start, end, status)