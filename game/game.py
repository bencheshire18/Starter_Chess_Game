import pygame
from game.board import Board
from game.game_status import GameStatus
from game.pieces import King, Queen, Bishop, Pawn, Rook, Knight
from game.pieces.piece_rules import check_for_checkmate
from ui.window import Window
from ui.get_board_square_from_mouse_coords import get_board_square_from_mouse_coords
from ui import display_info, draw_board, draw_pieces, draw_highlighted_squares, draw_legal_moves, update_display
from game.engine import simple_engines, generate_all_legal_moves
import game.constants as c

human_player = "white"
window = Window()
board = Board()
status = GameStatus()
board.create_grid()
# board.setup_board()

case = 2

match case:
    case 1:
        board.setup_board()
    case 2:
        board.place_piece(King("white"), 7, 6)   # g1
        board.place_piece(Rook("white"), 7, 0)   # a1
        board.place_piece(King("black"), 0, 6)   # g8
        board.place_piece(Pawn("black"), 1, 5)   # f7
        board.place_piece(Pawn("black"), 1, 6)   # g7
        board.place_piece(Pawn("black"), 1, 7)   # h7
# Initialisation

pygame.init()

fps_clock = pygame.time.Clock()

square_selected = False
running = True
legal_moves = []
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
while running:
    # Handle events

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

    # Engine Path
    # print(f"Active player: {status.active_player}\nHuman player : {human_player}")
    if status.active_player != human_player:
        # Generate legal moves
        all_legal_moves = generate_all_legal_moves.generate_all_legal_moves(board, status)
        # Make a move
        simple_engines.make_random_move(all_legal_moves, board, status)
        # Unselect square
        square_selected = False
        update_display.update_display(board, status, window, fps_clock)
        continue

    # Human path
    elif square_selected == True:
        # Draw highlighted squares (not needed in engine path)
        draw_highlighted_squares.draw(window, row, col)
        # assign active piece (done within generate_all_legal_moves)
        active_piece = board.grid[row][col]
        if active_piece is not None:
            if [row, col] in legal_moves:
                board.move_piece(start_square, [row, col], status)
                square_selected = False
                update_display.update_display(board, status, window, fps_clock)
                continue
            start = [row, col]
            legal_moves = active_piece.get_legal_moves(start, board, status, False)
            checkmate_counter = 0
            
            draw_legal_moves.draw_legal_moves(window, legal_moves, board, status)
            start_square = [row, col]
        else:
            if [row, col] in legal_moves:
                board.move_piece(start_square, [row, col], status)
                square_selected = False
            legal_moves = []
            start_square = []
    if status.checkmate == True:
        board.show_checkmate(window, status, fps_clock)

    update_display.update_display(board, status, window, fps_clock)