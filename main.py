from chess.piece import Piece
import pygame
from chess.constants import WIDTH, HEIGHT
from chess.board import Board
from pygame.locals import *

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Chess')


pieces = pygame.image.load("images/chess-pieces.png")
pieces = pygame.transform.scale(pieces, (pieces.get_width() // 3, pieces.get_height() // 3))
imagerect = pieces.get_rect()

def main():
    run = True
    clock = pygame.time.Clock()

    # new board object
    board = Board()

    

    while(run):
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        # draw the board at the end of each loop
        board.draw_board(WIN)
        WIN.blit(pieces, imagerect)
        pygame.display.update()

    pygame.quit()

main()
