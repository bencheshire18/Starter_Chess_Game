import pygame
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / "ui" / "Piece_Sprites" / "whiteQueen.png"

pygame.init()

win_icon = pygame.image.load(file_path)
pygame.display.set_icon(win_icon)

WIDTH, HEIGHT = 800, 400
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
counter = 0
while running:
    CLOCK.tick(FPS)
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()