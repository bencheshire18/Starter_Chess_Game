import pygame
from ui import display_info, draw_board, draw_pieces, draw_highlighted_squares, draw_legal_moves

def update_display(board, status, window, fps_clock):
    draw_pieces.draw_pieces(window, board.grid)
    display_info.write_active_player(status, window)
    display_info.write_board_coords(window)
    display_info.write_castling_availability(status, window)
    display_info.write_is_check(status, window)
    display_info.write_en_passant(status, window)

    # Update display
    pygame.display.flip()
    fps_clock.tick(60)