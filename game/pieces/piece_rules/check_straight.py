def check_straight(start, end):
    start_row = start[0]
    start_col = start[1]
    end_row   = end[0]
    end_col   = end[1]

    # Check horizontal
    if start_row == end_row:
        # Check left
        if start_col > end_col:
            col_range = range(start_col - 1, end_col, -1)
            row_range = [start_row] * len(col_range)
        # Check right
        elif start_col < end_col:
            col_range = range(start_col + 1, end_col, +1)
            row_range = [start_row] * len(col_range)
        
    # Check vertical
    elif start_col == end_col:
        # Check up
        if start_row > end_row:
            row_range = range(start_row - 1, end_row, -1)
            col_range = [start_col] * len(row_range)
        # Check down
        elif start_row < end_row:
            row_range = range(start_row + 1, end_row, +1)
            col_range = [start_col] * len(row_range)

    return row_range, col_range