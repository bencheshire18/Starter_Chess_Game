def get_board_square_from_mouse_coords(window, x, y):

    row = (y - window.margin) // window.square_size
    col = (x - window.margin) // window.square_size

    if row > 7 or row < 0 or col > 7 or col < 0:
        return -1, -1

    return row, col