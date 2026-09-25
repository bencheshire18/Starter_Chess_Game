from ui.get_coords_from_grid_pos import get_coords_from_grid_pos
import pygame
import game.constants as c

def write_active_player(status, window):
    label = window.font.render(f"Turn: {status.active_player}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 10))
    window.screen.blit(label, label_rect)

def write_board_coords(window):
    for row in range(8):
        for col in range(8):
            label = window.font.render(f"[{row}, {col}]", True, (255, 255, 255))
            label_rect = label.get_rect(topleft=(get_coords_from_grid_pos(window, col, row)))

            window.screen.blit(label, label_rect)

def write_castling_availability(status, window):
    label = window.font.render(f"White Kingside castling availabiltiy: {status.kingside_white_castling_available}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 30))
    window.screen.blit(label, label_rect)

    label = window.font.render(f"White Queenside castling availability: {status.queenside_white_castling_available}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 50))
    window.screen.blit(label, label_rect)

    label = window.font.render(f"Black Kingside castling availability: {status.kingside_black_castling_available}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 70))
    window.screen.blit(label, label_rect)

    label = window.font.render(f"Black Queenside castling availability: {status.queenside_black_castling_available}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 90))
    window.screen.blit(label, label_rect)

def write_is_check(status, window):
    label = window.font.render(f"Is Check: {status.in_check}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 110))
    window.screen.blit(label, label_rect)

def write_en_passant(status, window):
    label = window.font.render(f"En Passant available: {status.en_passant_available}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 130))
    window.screen.blit(label, label_rect)

def write_checkmate(status, window):
    label = window.checkmate_font.render(f"Checkmate", True, (255, 255, 255))
    label_rect = label.get_rect(center=(window.margin + window.board_size // 2, window.margin + window.board_size // 2))
    window.screen.blit(label, label_rect)

def draw_reset_button(status, window):
    label = window.reset_font.render(f"Reset", True, (255, 255, 255))
    label_rect = label.get_rect(center=(window.margin + window.board_size // 2, window.margin + window.board_size // 2 + 75))
    window.screen.blit(label, label_rect)

def draw_button(window, width=10, height=10, x_centre_offset=0, y_centre_offset=0, colour=(255, 255, 255)):
    # Button geometry
    button_rect = pygame.Rect(0, 0, width, height)
    button_rect.center = (c.MARGIN + window.board_size // 2 + x_centre_offset, c.MARGIN + window.board_size // 2 + y_centre_offset)
    boarder_rad = 10
        # Border first (slightly bigger rect), then fill on top -> clean outline
    border_rect = button_rect.inflate(4, 4)
    pygame.draw.rect(window.screen, c.BORDER, border_rect, border_radius=boarder_rad + 2)
    pygame.draw.rect(window.screen, colour, button_rect, border_radius=boarder_rad)

    return button_rect

def write_is_hovering(is_hovering, window):
    label = window.font.render(f"Is Hovering: {is_hovering}", True, (255, 255, 255))
    label_rect = label.get_rect(topleft=(window.board_size + window.margin * 2, 150))
    window.screen.blit(label, label_rect)