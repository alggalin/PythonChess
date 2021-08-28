from .constants import BLACK, SQUARE_SIZE, WHITE

PADDING = 10
BORDER = 2

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def draw(self, win):
        pass

    def __repr__(self):
        return str(self.color)
