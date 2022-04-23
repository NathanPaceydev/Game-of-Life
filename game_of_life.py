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
print("Enter the number of squares: ")
SIZE = int(input())
#grid height, width and margin for each square
HEIGHT, WIDTH = 20,20
MARGIN = 5

WINDOW_SIZE = [255*SIZE/10,300*SIZE/10]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")

arrow_image = pygame.image.load("start_btn.png").convert_alpha()
arrow_image = pygame.transform.scale(arrow_image,((WINDOW_SIZE[0]/5,WINDOW_SIZE[0]/6)))

exit_image = pygame.image.load("exit_btn.png").convert_alpha()
exit_image = pygame.transform.scale(exit_image,((WINDOW_SIZE[0]/5,WINDOW_SIZE[0]/6)))



class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        screen.blit(self.image, (self.rect.x,self.rect.y))
    
start_button = Button(WINDOW_SIZE[0]/2-WINDOW_SIZE[0]/3,WINDOW_SIZE[1]-WINDOW_SIZE[0]/6, arrow_image)
exit_button = Button(WINDOW_SIZE[0]-WINDOW_SIZE[0]/3,WINDOW_SIZE[1]-WINDOW_SIZE[0]/6,exit_image)



def gridSetUp(size):
    return [[0]*size for _ in range(size)]

def main():
    grid = gridSetUp(SIZE)
    pygame.init()
    try:
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

                    start_button.draw()
                    exit_button.draw()

            clock.tick(60)

            pygame.display.flip()

    finally:
        pygame.quit()



if __name__ == '__main__':
    main()