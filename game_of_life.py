from typing import final
import pygame
import random

# importing the controls used to avoid library calls
from pygame import (
    MOUSEBUTTONDOWN,
    QUIT,
    K_ESCAPE,
    KEYDOWN
)

#define the colors in RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GREY = (250,240,250)
GREEN = (0,255,0)
RED = (255,0,0)

#define some constants
SIZE = 20
#grid height, width and margin for each square
HEIGHT, WIDTH = 20,20
MARGIN = 5

WINDOW_SIZE = [255*SIZE/10,300*SIZE/10]


def gridSetUp(size):
    return [[0]*size for _ in range(size)]

def main():
    grid = gridSetUp(SIZE)
    pygame.init()
    try:
        screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption("Game of Life")

        clock = pygame.time.Clock()

        runFlag = True

        while runFlag:
            for event in pygame.event.get():
                # did a user hit a key
                if event.type == KEYDOWN:
                    # is it the esc key
                    if event.key == K_ESCAPE:
                        runflag = False

                elif event.type == QUIT:
                    runFlag = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0]//(WIDTH+MARGIN)
                    row = pos[1]//(WIDTH+MARGIN)
                    
                    if row <SIZE and col <SIZE:

                        if grid[row][col]==0:
                            grid[row][col] = 1
                        else:
                            grid[row][col]=0
                        print("Clicked ", row, col)

            screen.fill(BLACK)

            for row in range(SIZE):
                for col in range(SIZE):
                    color = LIGHT_GREY
                    if grid[row][col] == 1:
                        color = GREEN
                    pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

            clock.tick(60)

            pygame.display.flip()

    finally:
        pygame.quit()



if __name__ == '__main__':
    main()