import game.constants as c
import pygame
from ui.get_coords_from_grid_pos import get_coords_from_grid_pos

def draw(window, row, col):

    if row == -1:
        return False

    x, y = get_coords_from_grid_pos(window, row, col)
    if (row + col) % 2 == 0:
        colour = c.HIGHLIGHTED_LIGHT_SQUARE
    else:
        colour = c.HIGHLIGHTED_DARK_SQUARE

    pygame.draw.rect(window.screen, colour, (y, x, window.square_size, window.square_size))
