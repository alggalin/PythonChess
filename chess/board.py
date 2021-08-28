import pygame
from .constants import BLACK, GRAY, ROWS, SQUARE_SIZE, WHITE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 12

    def draw_board(self, win):
        win.fill(WHITE)

        # loop used to draw the squares for the pieces
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass