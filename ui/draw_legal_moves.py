import game.constants as c
import pygame
from ui.get_coords_from_grid_pos import get_coords_from_grid_pos

def draw_legal_moves(window, legal_moves, board, status):

    for move in legal_moves:
        row, col = move[0], move[1]
        if (row + col) % 2 == 0:
            colour = c.LIGHT_SQUARE_LEGAL_MOVE
        else:
            colour = c.DARK_SQUARE_LEGAL_MOVE
        x, y = get_coords_from_grid_pos(window, row, col)

        if board.grid[row][col] is not None and board.grid[row][col].colour != status.active_player:
            pygame.draw.circle(window.screen, colour, (y + window.square_size/2, x + window.square_size / 2), window.square_size // 2, window.square_size // 12)
        else:
            pygame.draw.circle(window.screen, colour, (y + window.square_size/2, x + window.square_size / 2), window.square_size // 5)