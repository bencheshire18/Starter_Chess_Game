import sys
import pygame

# Initialize Pygame
pygame.init()

# Setup display window
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Ring")

# Colors (RGB)
DARK_GRAY = (30, 255, 30)
CYAN = (0, 220, 255)

# Ring properties
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 80
BORDER_THICKNESS = 15  # Thickness of the ring wall

# Main loop setup
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen with background color
    screen.fill(DARK_GRAY)

    # Draw the ring using width parameter
    pygame.draw.circle(
        surface=screen,
        color=CYAN,
        center=CENTER,
        radius=RADIUS,
        width=BORDER_THICKNESS
    )

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()