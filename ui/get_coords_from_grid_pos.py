def get_coords_from_grid_pos(window, x, y):
    x0 = window.margin
    y0 = window.margin
    x_final = x0 + window.square_size*x
    y_final = y0 + window.square_size*y

    return x_final, y_final