from chess.piece import Piece
import pygame
from chess.constants import WIDTH, HEIGHT
from chess.board import Board
from pygame.locals import *

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Chess')


white_king = pygame.image.load("images/WK.png")
white_king = pygame.transform.scale(white_king, (white_king.get_width() // 3, white_king.get_height() // 3))

imagerect = white_king.get_rect()

def main():
    run = True
    clock = pygame.time.Clock()

    # new board object
    board = Board()

    # initial position of the piece
    mx, my = 50, 50

    while(run):
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
        
            # move piece while mouse being pressed
            if pygame.mouse.get_pressed()[0] == True:
                mx, my = pygame.mouse.get_pos()
        
        
        # draw the board at the end of each loop
        board.draw_board(WIN)
        # WIN.blit(white_king, imagerect)
        WIN.blit(white_king, (mx - 50, my - 50))
        pygame.display.update()

    pygame.quit()

main()
