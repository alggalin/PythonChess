from chess import piece
import pygame
from .constants import BLACK, RED, WHITE
from .board import Board

class Game:

    def __init__(self, win):
        self.selected = None
        self.turn = WHITE
        self.board = Board()
        self.valid_moves = set()
    
    def update(self, win):
        self.board.draw_board(win)

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)

        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.get_valid_moves(piece)

    def get_valid_moves(self, piece):
        self.valid_moves.clear()
        
        if piece.piece_type == "BP" or piece.piece_type == "WP":
            self.pawn_moves(piece)

    def move_piece(self, row, col):
        if self.selected is not None:
            piece = self.board.get_piece(row, col)

            position = (row, col)
            if position in self.valid_moves:
                if piece != 0 and piece.color != self.turn:
                    self.remove_piece(piece.row, piece.col)

                self.board.move(self.selected, row, col)
                self.change_turn()
    
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
            if diag != 0 and diag.color != self.turn:
                self.valid_moves.add((row - 1, col - 1))
            
            diag = self.board.get_piece(row - 1, col + 1)
            if diag != 0 and diag.color != self.turn:
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
            if diag != 0 and diag.color != self.turn:
                self.valid_moves.add((row + 1, col - 1))
            
            diag = self.board.get_piece(row + 1, col + 1)
            if diag != 0 and diag.color != self.turn:
                self.valid_moves.add((row + 1, col + 1))