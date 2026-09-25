import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Scratch")
clock = pygame.time.Clock()

BACKGROUND   = (48, 46, 43)
BUTTON       = (70, 130, 100)
BUTTON_HOVER = (90, 160, 125)
BUTTON_CLICK = (55, 105, 80)
BORDER       = (20, 40, 30)
TEXT_COLOUR  = (255, 255, 255)

font = pygame.font.SysFont("arial", 22, bold=True)

# Button geometry
button_rect = pygame.Rect(0, 0, 140, 48)
button_rect.center = (WIDTH // 2, HEIGHT // 2)
BORDER_RADIUS = 10

running = True
mouse_down_on_button = False

while running:
    mouse_pos = pygame.mouse.get_pos()
    is_hovering = button_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if is_hovering:
                mouse_down_on_button = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if mouse_down_on_button and is_hovering:
                print("Button clicked!")
            mouse_down_on_button = False

    screen.fill(BACKGROUND)

    if mouse_down_on_button and is_hovering:
        colour = BUTTON_CLICK
    elif is_hovering:
        colour = BUTTON_HOVER
    else:
        colour = BUTTON

    # Border first (slightly bigger rect), then fill on top -> clean outline
    border_rect = button_rect.inflate(4, 4)
    pygame.draw.rect(screen, BORDER, border_rect, border_radius=BORDER_RADIUS + 2)
    pygame.draw.rect(screen, colour, button_rect, border_radius=BORDER_RADIUS)

    label = font.render("Reset", True, TEXT_COLOUR)
    label_rect = label.get_rect(center=button_rect.center)
    screen.blit(label, label_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()