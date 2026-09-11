import pygame
from pathlib import Path
from ui.get_coords_from_grid_pos import get_coords_from_grid_pos

def resize_sprite(window, sprite,):
    scaled_sprite = pygame.transform.smoothscale(sprite, (window.square_size, window.square_size))
    return scaled_sprite

def draw_pieces(window, grid):
    for row in range(8):
        for col in range(8):
            piece = grid[row][col]
            if piece is not None:
                script_dir = Path(__file__).parent
                filename = script_dir / "Piece_Sprites" / f"{piece.colour}{piece.name}.png"
                x_coord, y_coord = get_coords_from_grid_pos(window, row, col)
                sprite = pygame.image.load(filename)
                scaled_sprite = resize_sprite(window, sprite)
                window.screen.blit(scaled_sprite, (y_coord, x_coord))
