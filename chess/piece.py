import pygame
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
    
    def get_piece_type(self):
        return self.piece_type

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def get_draw_pos(self):
        return (self.x - 50, self.y - 50)

    def draw(self, win):
        # get the appropriate image piece to draw
        piece = pygame.image.load("images/" + str(self.piece_type) + ".png")
        piece = pygame.transform.scale(piece, (piece.get_width() // 3, piece.get_height() // 3))
        win.blit(piece, self.get_draw_pos())

    def __repr__(self):
        return str(self.piece_type + " (" + str(self.col) + ", " + str(self.row) + ")")

