from .constants import BLACK, SQUARE_SIZE, WHITE

PADDING = 10
BORDER = 2

class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def get_draw_pos(self):
        return (self.x - 50, self.y - 50)

    def draw(self, win):
        pass

    def __repr__(self):
        if self.color == WHITE:
            return str(self.piece_type)
        else:
            return str(self.piece_type)

