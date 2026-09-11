from game.constants import FILE_MAP, RANK_MAP

class GenerateMove:
    def __init__(self, start_square, end_square):
        self.start_square = start_square
        self.end_square = end_square

    def get_start_coordinates(self):
        start_col = FILE_MAP[self.start_square[0].lower()]
        start_row = RANK_MAP[self.start_square[1]]    

        return start_row, start_col 

    def get_coordinates(self):
        start_col = FILE_MAP[self.start_square[0].lower()]
        start_row = RANK_MAP[self.start_square[1]]
        end_col   = FILE_MAP[self.end_square[0].lower()]
        end_row   = RANK_MAP[self.end_square[1]]
        
        return start_row, start_col, end_row, end_col