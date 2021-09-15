import pygame
from .constants import BLACK, BROWN, ROWS, SQUARE_SIZE, TAN, ROWS, COLS, WHITE
from .piece import Piece
from chess import piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 16
        self.create_board()

    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, row, col):
        piece = self.board[row][col]

        if piece.piece_type == "BK" or piece.piece_type == "WK":
            print("CheckMate!")
        self.board[row][col] = 0

    def move(self, piece, row, col):
        temp = self.board[row][col]
        self.board[row][col] = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = temp
        self.board[row][col].move(row, col)


    def draw_board(self, win):
        win.fill(BROWN)

        # loop used to draw the squares for the pieces
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, TAN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        self.draw_pieces(win)

    def draw_pieces(self, win):
        # need to go through the list and place each piece according to it's actual location
            # have to look at the piece that's stored there and use position to know where to draw it
        for col in range(COLS):
            for row in range(ROWS):
                board_position = self.board[col][row]

                if board_position != 0:  # there is a piece here that should be drawn
                    board_position.draw(win)

    # function to fill up the board with appropriate pieces in their specific locations
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0 and (col == 0 or col == 7):
                    self.board[row].append(Piece(row, col, BLACK, "BR"))
                elif row == 0 and (col == 1 or col == 6):
                    self.board[row].append(Piece(row, col, BLACK, "BN"))
                elif row == 0 and (col == 2 or col == 5):
                    self.board[row].append(Piece(row, col, BLACK, "BB"))
                elif row == 0 and col == 3:
                    self.board[row].append(Piece(row, col, BLACK, "BQ"))
                elif row == 0 and col == 4:
                    self.board[row].append(Piece(row, col, BLACK, "BK"))
                elif row == 1:
                    self.board[row].append(Piece(row, col, BLACK, "BP"))
                elif row == 7 and (col == 0 or col == 7):
                    self.board[row].append(Piece(row, col, WHITE, "WR"))
                elif row == 7 and (col == 1 or col == 6):
                    self.board[row].append(Piece(row, col, WHITE, "WN"))
                elif row == 7 and (col == 2 or col == 5):
                    self.board[row].append(Piece(row, col, WHITE, "WB"))
                elif row == 7 and col == 3:
                    self.board[row].append(Piece(row, col, WHITE, "WQ"))
                elif row == 7 and col == 4:
                    self.board[row].append(Piece(row, col, WHITE, "WK"))
                elif row == 6:
                    self.board[row].append(Piece(row, col, WHITE, "WP"))
                else:
                    self.board[row].append(0)