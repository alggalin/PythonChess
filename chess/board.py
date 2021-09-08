import pygame
from .constants import BLACK, BROWN, ROWS, SQUARE_SIZE, TAN, ROWS, COLS, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16
        self.create_board()

    def draw_board(self, win):
        win.fill(BROWN)

        # loop used to draw the squares for the pieces
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, TAN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # function to fill up the board with appropriate pieces in their specific locations
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0 and (col == 0 or col == 7):
                    self.board[row].append(Piece(row, col, BLACK, "rook"))
                elif row == 0 and (col == 1 or col == 6):
                    self.board[row].append(Piece(row, col, BLACK, "knight"))
                elif row == 0 and (col == 2 or col == 5):
                    self.board[row].append(Piece(row, col, BLACK, "bishop"))
                elif row == 0 and col == 3:
                    self.board[row].append(Piece(row, col, BLACK, "queen"))
                elif row == 0 and col == 4:
                    self.board[row].append(Piece(row, col, BLACK, "king"))
                elif row == 1:
                    self.board[row].append(Piece(row, col, BLACK, "pawn"))
                elif row == 7 and (col == 0 or col == 7):
                    self.board[row].append(Piece(row, col, WHITE, "rook"))
                elif row == 7 and (col == 1 or col == 6):
                    self.board[row].append(Piece(row, col, WHITE, "knight"))
                elif row == 7 and (col == 2 or col == 5):
                    self.board[row].append(Piece(row, col, WHITE, "bishop"))
                elif row == 7 and col == 3:
                    self.board[row].append(Piece(row, col, WHITE, "queen"))
                elif row == 7 and col == 4:
                    self.board[row].append(Piece(row, col, WHITE, "king"))
                elif row == 6:
                    self.board[row].append(Piece(row, col, WHITE, "pawn"))
                else:
                    self.board[row].append(0)
    
        print(self.board)
