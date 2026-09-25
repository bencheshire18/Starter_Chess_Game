BOARD_SIZE = 8
SCREEN_HEIGHT = 600
SCREEN_WIDTH  = 900

FILE_MAP = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

RANK_MAP = {
    "1" : 7,
    "2" : 6,
    "3" : 5,
    "4" : 4,
    "5" : 3,
    "6" : 2,
    "7" : 1,
    "8" : 0
}

# Colours
DARK_SQUARE                 = (180, 135, 96 )
LIGHT_SQUARE                = (235, 214, 175)
HIGHLIGHTED_LIGHT_SQUARE    = (244, 234, 103)
HIGHLIGHTED_DARK_SQUARE     = (220, 195, 75 )
BACK_GROUND                 = (48 , 46 , 43 )
BLACK                       = (0  , 0  , 0  )
WHITE                       = (255, 255, 255)
LIGHT_SQUARE_LEGAL_MOVE     = (204, 184, 151)
DARK_SQUARE_LEGAL_MOVE      = (158, 116, 84 )
BUTTON                      = (70 , 130, 100)
BUTTON_HOVER                = (90 , 160, 125)
BUTTON_CLICK                = (55 , 105, 80 )
BORDER                      = (20 , 40 , 30 )
TEXT_COLOUR                 = (255, 255, 255)

MARGIN = 25
BOARD_WIDTH = min(SCREEN_HEIGHT, SCREEN_WIDTH) - MARGIN * 2
SQUARE_WIDTH = int(round(BOARD_WIDTH/8))