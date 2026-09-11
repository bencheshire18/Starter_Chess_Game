import game.constants as c
import pygame

def draw_board(window):

    # Clear the screen with a black background
    window.screen.fill(c.BACK_GROUND)

    # Draw the circle: (surface, color, center_pos, radius)
    # pygame.draw.circle(window, LIGHT_SQUARE, circle_center, circle_radius)
    x = window.margin
    y = window.margin
    colour = c.DARK_SQUARE
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                colour = c.LIGHT_SQUARE
            else:
                colour = c.DARK_SQUARE
            pygame.draw.rect(window.screen, colour, (x, y, window.square_size, window.square_size))
            x += window.square_size
        y += window.square_size
        x = window.margin