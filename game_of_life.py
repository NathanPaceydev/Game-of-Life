from turtle import delay, width
from typing import final
import pygame
import numpy as np

import button

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
print("Enter the width of squares: ")
WIDTH_SIZE = int(input())
print("Enter the length of squares: ")
LENGTH_SIZE = int(input())
#grid height, width and margin for each square
HEIGHT, WIDTH = 20,20
MARGIN = 5

WINDOW_SIZE = [255*WIDTH_SIZE/10,300*LENGTH_SIZE/10]

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")

arrow_image = pygame.image.load("start_btn.png").convert_alpha()
arrow_image = pygame.transform.scale(arrow_image,((WINDOW_SIZE[0]/5,WINDOW_SIZE[0]/6)))

exit_image = pygame.image.load("exit_btn.png").convert_alpha()
exit_image = pygame.transform.scale(exit_image,((WINDOW_SIZE[0]/5,WINDOW_SIZE[0]/6)))
    

start_button = button.Button(WINDOW_SIZE[0]/2-WINDOW_SIZE[0]/3,WINDOW_SIZE[1]-WINDOW_SIZE[0]/6, arrow_image)
exit_button = button.Button(WINDOW_SIZE[0]-WINDOW_SIZE[0]/3,WINDOW_SIZE[1]-WINDOW_SIZE[0]/6,exit_image)


def gridSetUp(width,length):
    return [[0]*width for _ in range(length)]

def gameOfLife(board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dirs = [[-1,-1],[-1,0],[0,-1],[1,0],[0,1],[1,1],[1,-1],[-1,1]]
        
        numRows = len(board)
        numCol = len(board[0])
        
        res = [[0]*numCol for i in range(numRows)]
       
        for i in range(numRows):
            for j in range(numCol):
                count = 0
                
                for dx,dy in dirs:
                    deltaRow = dx+i
                    deltaCol = dy+j
                    
                    if(numRows>deltaRow>-1) and (numCol>deltaCol>-1) and board[deltaRow][deltaCol]==1:
                        count+=1
                        
                
                if board[i][j]==1:
                    if count<2 or count>3:
                        res[i][j]=0
                    else:
                        res[i][j] = 1
                else:
                    if count==3:
                        res[i][j] = 1
                    else:
                        res[i][j] = 0
                    
        return res[::] 

def main():
    grid = gridSetUp(WIDTH_SIZE,LENGTH_SIZE)
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
                    
                    if row <LENGTH_SIZE and col <WIDTH_SIZE:

                        if grid[row][col]==0:
                            grid[row][col] = 1
                        else:
                            grid[row][col]=0
                        print("Clicked ", row, col)

            screen.fill(BLACK)

            for row in range(LENGTH_SIZE):
                for col in range(WIDTH_SIZE):
                    color = LIGHT_GREY
                    if grid[row][col] == 1:
                        color = GREEN
                    pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

                    if start_button.draw(screen):
                        print("START")
                        grid = gameOfLife(grid)


                    if exit_button.draw(screen):
                        runFlag = False

            clock.tick(60)

            pygame.display.flip()

    finally:
        pygame.quit()



if __name__ == '__main__':
    main()