def check_diag(start, end):        
    start_row = start[0]
    start_col = start[1]
    end_row   = end[0]
    end_col   = end[1]
    
    # Check all directions
    
    # 1 Check up-right (-rows +cols)
    if start_row > end_row and start_col < end_col:
        row_range = range(start_row - 1, end_row, -1)
        col_range = range(start_col + 1, end_col, +1)
            
    # 2 Check up-left (-rows -cols)
    elif start_row > end_row and start_col > end_col:
        row_range = range(start_row - 1, end_row, -1)
        col_range = range(start_col - 1, end_col, -1)
            
    # 3 Check down-left (+rows -cols)
    elif start_row < end_row and start_col > end_col:
        row_range = range(start_row + 1, end_row, +1)
        col_range = range(start_col - 1, end_col, -1)

    # 4 Check down-right (+rows +cols)
    elif start_row < end_row and start_col < end_col:
        row_range = range(start_row + 1, end_row, +1)
        col_range = range(start_col + 1, end_col, +1)

    else:
        raise Exception("ERROR! no if statements entered when identifying moves to check for legality")
    
    return row_range, col_range