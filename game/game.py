import pygame
from game.board import Board
from game.game_status import GameStatus
from game.pieces import King, Queen, Bishop, Pawn, Rook
from game.pieces.piece_rules import check_for_checkmate
from ui.window import Window
from ui.get_board_square_from_mouse_coords import get_board_square_from_mouse_coords
from ui import display_info, draw_board, draw_pieces, draw_highlighted_squares, draw_legal_moves
from game.engine import simple_engines, generate_all_legal_moves

human_player = "white"
window = Window()
board = Board()
status = GameStatus()
board.create_grid()
board.setup_board()

# board.place_piece(King("white"), 7, 4)
# board.place_piece(Bishop("black"), 7, 5)
# board.place_piece(Rook("white"), 7, 7)
# board.place_piece(Bishop("black"), 7, 3)
# board.place_piece(Rook("white"), 7, 0)
# board.place_piece(King("black"), 0, 4)
# # board.place_piece(Bishop("white"), 3, 2)
# board.place_piece(Rook("black"), 0, 7)
# board.place_piece(Bishop("white"), 0, 3)
# board.place_piece(Rook("black"), 0, 0)

# Initialisation

pygame.init()

fps_clock = pygame.time.Clock()

square_selected = False
running = True
legal_moves = []
while running:
    # Handle events
    # Checking if checkmate before running through the rest of the logic
    checkmate_counter = check_for_checkmate.check_for_checkmate(board, status)

    status.in_check = board.is_check(status)
    ev = pygame.event.wait()

    if ev.type == pygame.QUIT:
        running = False

    elif ev.type == pygame.VIDEORESIZE:
        window.resize(ev.w, ev.h)

    elif ev.type == pygame.MOUSEBUTTONDOWN:
        if ev.button == 1:
            square_selected = True
            x, y = pygame.mouse.get_pos()
            row, col = get_board_square_from_mouse_coords(window, x, y)
        elif ev.button == 3:
            square_selected = False
            legal_moves = []

    # Draw
    draw_board.draw_board(window)

    if checkmate_counter == 0:
        print("CHECKMATE!")
        running = False

    if status.active_player != human_player:
        all_legal_moves = generate_all_legal_moves.generate_all_legal_moves(board, status)
        simple_engines.make_random_move(all_legal_moves, board, status)
        status.toggle_turn()
        square_selected = False
        continue

    if square_selected == True:
        draw_highlighted_squares.draw(window, row, col)
        active_piece = board.grid[row][col]
        if active_piece is not None:
            if [row, col] in legal_moves:
                board.move_piece(start_square, [row, col], status)
                status.toggle_turn()
                square_selected = False
                continue
            start = [row, col]
            legal_moves = active_piece.get_legal_moves(start, board, status, False)
            legal_moves = board.trim_legal_moves(start, legal_moves, status)
            checkmate_counter = 0
            
            draw_legal_moves.draw_legal_moves(window, legal_moves, board, status)
            start_square = [row, col]
        else:
            if [row, col] in legal_moves:
                board.move_piece(start_square, [row, col], status)
                status.toggle_turn()
                square_selected = False
            legal_moves = []
            start_square = []

    draw_pieces.draw_pieces(window, board.grid)
    display_info.write_active_player(status, window)
    display_info.write_board_coords(window)
    display_info.write_castling_availability(status, window)
    display_info.write_is_check(status, window)
    display_info.write_en_passant(status, window)

    # Update display
    pygame.display.flip()
    fps_clock.tick(60)