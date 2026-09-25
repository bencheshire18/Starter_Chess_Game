import pygame

class Window:
    def __init__(self):
        self.width = 900
        self.height = 600
        self.margin = 25
        self.board_size  = min(self.width, self.height) - self.margin * 2
        self.square_size = self.board_size // 8
        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.RESIZABLE
        )
        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", 15)
        self.checkmate_font = pygame.font.SysFont("arial", self.square_size)

        self.update_dimensions()

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.RESIZABLE
        )
        self.update_dimensions()

    def update_dimensions(self):
        self.board_size = min(self.width, self.height) - self.margin * 2
        self.square_size = self.board_size // 8