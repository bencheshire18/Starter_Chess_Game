from ui.get_coords_from_grid_pos import get_coords_from_grid_pos

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