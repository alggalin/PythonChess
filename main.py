from chess.piece import Piece
import pygame
from chess.constants import SQUARE_SIZE, WIDTH, HEIGHT
from chess.game import Game
from pygame.locals import *

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Chess')

def get_mouse_board_position(x, y):
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return (row, col)

def main():
    run = True
    clock = pygame.time.Clock()

    # new game object
    game = Game(WIN)

    # initial position of mouse
    mx, my = 50, 50

    while(run):
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx, my = get_mouse_board_position(mx, my)
                game.select_piece(mx, my)

            # # move piece while mouse being pressed
            # if pygame.mouse.get_pressed()[0] == True:
            #     mx, my = pygame.mouse.get_pos()

            #     print(mx, my)
        
        # draw the board and pieces at the end of each loop
        game.update(WIN)

        pygame.display.update()

    pygame.quit()

main()
