from chess import piece
import pygame
from .constants import RED, WHITE
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
        self.selected = piece
