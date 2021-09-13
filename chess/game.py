from chess import piece
import pygame
from .constants import BLACK, RED, WHITE
from .board import Board

class Game:

    def __init__(self, win):
        self.selected = None
        self.turn = WHITE
        self.board = Board()
        self.valid_moves = {}
    
    def update(self, win):
        self.board.draw_board(win)

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece

    def move_piece(self, row, col):
        if self.selected is not None:
            self.board.move(self.selected, row, col)
            # self.change_turn()
    
    def change_turn(self):
        self.selected = None
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE