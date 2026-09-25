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
pygame.event.set_blocked(pygame.MOUSEMOTION)
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
        print("Checkmate")
        waiting = True
        while waiting == True:
            display_info.write_checkmate(status, window)
            display_info.draw_reset_button(status, window) # TODO make this look more like a button
            ev = pygame.event.wait() # TODO Only wait for left mouse click or quit...
            x, y = pygame.mouse.get_pos()
            checkmate_font_width, checkmate_font_height = window.font.size("Reset")
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    if x >= window.margin + window.board_size // 2 - 7 and x <= window.margin + window.board_size // 2 + 7:
                        if y >= window.margin + window.board_size // 2 - checkmate_font_width // 2 and y <= window.margin + window.board_size // 2 + checkmate_font_width // 2:
                            # TODO reset the board and start again
                            pass
            elif ev.type == quit:
                running = False
                waiting = False

    update_display.update_display(board, status, window, fps_clock)