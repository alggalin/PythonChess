from chess import piece
import pygame
from pygame import mixer
from .constants import BLACK, RED, SQUARE_SIZE, WHITE, DARK_RED
from .board import Board

pygame.mixer.init()
mixer.music.load("audio/move_made.mp3")

class Game:

    def __init__(self, win):
        self.selected = None
        self.turn = WHITE
        self.board = Board()
        self.valid_moves = set()
    
    def update(self, win):
        self.board.draw_board(win)
        self.draw_valid_moves(win)
        self.board.draw_pieces(win)

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)

        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.get_valid_moves(piece)


    def draw_valid_moves(self, win):
        for move in self.valid_moves:
            row, col = move
            pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(win, DARK_RED, (col * SQUARE_SIZE + 1, row * SQUARE_SIZE + 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2))

    def get_valid_moves(self, piece):
        self.valid_moves.clear()
        
        if piece.piece_type == "BP" or piece.piece_type == "WP":
            self.pawn_moves(piece)
        elif piece.piece_type == "BN" or piece.piece_type == "WN":
            self.knight_moves(piece)
        elif piece.piece_type == "BR" or piece.piece_type == "WR":
            self.rook_moves(piece)
        elif piece.piece_type == "BB" or piece.piece_type == "WB":
            self.bishop_moves(piece)
        elif piece.piece_type == "BQ" or piece.piece_type == "WQ":
            self.rook_moves(piece)
            self.bishop_moves(piece)
        elif piece.piece_type == "BK" or piece.piece_type == "WK":
            self.king_moves(piece)


    def move_piece(self, row, col):
        if self.selected is not None:
            piece = self.board.get_piece(row, col)

            position = (row, col)
            if position in self.valid_moves:
                if piece != 0 and piece.color != self.turn:
                    self.remove_piece(piece.row, piece.col)

                self.board.move(self.selected, row, col)
                self.change_turn()
                self.valid_moves = set()

                mixer.music.play()
    
    def remove_piece(self, row, col):
        self.board.remove(row, col)

    def change_turn(self):
        self.selected = None
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
    
    def pawn_moves(self, piece):
        row = piece.row
        col = piece.col

        if piece.color == WHITE:
            if row == 6:
                if self.board.get_piece(row - 1, col) == 0:
                    self.valid_moves.add((row - 1, col))
                    if self.board.get_piece(row - 2, col) == 0:
                        self.valid_moves.add((row - 2, col))
                
            else:
                if self.board.get_piece(row - 1, col) == 0:
                    self.valid_moves.add((row - 1, col))

            # check diagonal pieces to see if they can be ate
            diag = self.board.get_piece(row - 1, col -1)
            if diag is not None and diag != 0 and diag.color == BLACK:
                self.valid_moves.add((row - 1, col - 1))
            
            diag = self.board.get_piece(row - 1, col + 1)
            if diag is not None and diag != 0 and diag.color == BLACK:
                self.valid_moves.add((row - 1, col + 1))

        elif piece.color == BLACK:
            if row == 1:
                if self.board.get_piece(row + 1, col) == 0:
                    self.valid_moves.add((row + 1, col))
                    if self.board.get_piece(row + 2, col) == 0:
                        self.valid_moves.add((row + 2, col))
                
            else:
                if self.board.get_piece(row + 1, col) == 0:
                    self.valid_moves.add((row + 1, col))

            # check diagonal pieces to see if they can be ate
            diag = self.board.get_piece(row + 1, col -1)
            if diag is not None and diag != 0 and diag.color == WHITE:
                self.valid_moves.add((row + 1, col - 1))
            
            diag = self.board.get_piece(row + 1, col + 1)
            if diag is not None and diag != 0 and diag.color == WHITE:
                self.valid_moves.add((row + 1, col + 1))
    
    def knight_moves(self, piece):
        row = piece.row
        col = piece.col

        moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        for board_row, board_col in moves:
            position = self.board.get_piece(row + board_row, col + board_col)

            if position == 0 or (position is not None and position.color != self.turn):
                self.valid_moves.add((row + board_row, col + board_col))

    def rook_moves(self, piece):

        movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.cross_and_diag_moves(piece, movement)
    
    def bishop_moves(self, piece):

        movement = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        self.cross_and_diag_moves(piece, movement)
    
    def king_moves(self, piece):
        
        movement = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        self.cross_and_diag_moves(piece, movement, 1)
        
    def cross_and_diag_moves(self, piece, movement, distance=7):
        row = piece.row
        col = piece.col

        for row_move, col_move in movement:

            position = self.board.get_piece(row + row_move, col + col_move)
            #while position is not None:
            for i in range(distance):
                
                if position is None:
                    break

                if position != 0 and position.color == self.turn:
                    break

                self.valid_moves.add((row + row_move, col + col_move))

                if position != 0 and position.color != self.turn:
                    break

                if row_move > 0:
                    row_move += 1
                elif row_move < 0:
                    row_move -= 1
                
                if col_move > 0:
                    col_move += 1
                elif col_move < 0:
                    col_move -= 1

                position = self.board.get_piece(row + row_move, col + col_move)
                if position is None:
                    break