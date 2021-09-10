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
                    # get the appropriate image piece to draw
                    piece = pygame.image.load("images/" + str(board_position.piece_type) + ".png")
                    piece = pygame.transform.scale(piece, (piece.get_width() // 3, piece.get_height() // 3))
                    win.blit(piece, board_position.get_draw_pos())

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
