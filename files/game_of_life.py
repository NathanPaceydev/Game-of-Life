#!/usr/bin/bash python
# This file serves as the main file implementing the main game screen and the algorithm to make the game work
# The game starts by calling a seperate file start_screen.py which takes user input for the number of cells
# This file also instatiates the button class for the start, clear and next button

# import all librairies and modules used
import numpy
import pygame
import button
from start_screen import start

# define global constants
# importing the controls used to avoid library calls
from pygame import (
    QUIT,
    K_ESCAPE,
    KEYDOWN
)

# define the colors in RGB
GREY = (130,130,130)
WHITE = (255,255,255)
LIGHT_GREY = (250,240,250)
GREEN = (0,255,0)
RED = (255,0,0)

# call the start screen script to start the game and set the number of cells
WIDTH_SIZE_STR,LENGTH_SIZE_STR = start()
WIDTH_SIZE = int(WIDTH_SIZE_STR)
LENGTH_SIZE = int(LENGTH_SIZE_STR)

# grid height, width and margin for each square
HEIGHT, WIDTH = 20,20
MARGIN = 5
delta = 0

# setting a cap at the minimum width size
# if the width of squares are less than 4 set the delta to 100 this means the buttons won't be cut off
if WIDTH_SIZE<4:
    delta = WIDTH*4

#setting the window size
WINDOW_SIZE = [(WIDTH*WIDTH_SIZE+MARGIN*(WIDTH_SIZE+1)+delta),(HEIGHT*(LENGTH_SIZE+2)+MARGIN*(LENGTH_SIZE+3))]

# set the screen, icon and caption
screen = pygame.display.set_mode(WINDOW_SIZE)
icon = pygame.image.load("./media/icon.png").convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("Game of Life")

# load the images
arrow_image = pygame.image.load("./media/start_btn.png").convert_alpha()
next_image = pygame.image.load("./media/next_btn.png").convert_alpha()
clear_image = pygame.image.load("./media/clear_btn.png").convert_alpha()

# scale the images
arrow_image = pygame.transform.scale(arrow_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
next_image = pygame.transform.scale(next_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
clear_image = pygame.transform.scale(clear_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
    
# call an instance of the button class for each image using the image and the relative size
start_button = button.Button(WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)), arrow_image)
next_button = button.Button(WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)), next_image)
clear_button = button.Button(WINDOW_SIZE[0]-WINDOW_SIZE[0]/3-WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)),clear_image)

# function to clear the game grid (setting each square to 0) based on the grid length/width
def gridSetUp(width,length):
    return [[0]*width for _ in range(length)]

# function that describes the games algorithm for each iteration of the grid
# takes a 2D array board -> returns the 2D array res 
def gameOfLife(board):
        # relative directions array
        dirs = [[-1,-1],[-1,0],[0,-1],[1,0],[0,1],[1,1],[1,-1],[-1,1]]
        
        # set the rows and cols based on the board
        numRows, numCol = len(board), len(board[0])
        
        # declare a new empty board
        res = [[0]*numCol for i in range(numRows)]
       
       # update the new grid based on the rules of evolution in the game of life
       # Loop through each cell in the grid
        for i in range(numRows):
            for j in range(numCol):
                count = 0
                # loop through all the neighbors of the current cell
                for dx,dy in dirs:
                    deltaRow = dx+i
                    deltaCol = dy+j
                    # make the changes based on the rules
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
        

# main function to set up the game
def main():
    # set up 2D array with function
    grid = gridSetUp(WIDTH_SIZE,LENGTH_SIZE)
    
    # call pygame
    pygame.init()
    
    # put main code in a try catch to make the exit button not throw error
    try:
        # start the game clock and declare exit loop boolean
        clock = pygame.time.Clock()
        runFlag = True

        # set background color and draw the buttons
        screen.fill(GREY)
        start_button.draw(screen)
        clear_button.draw(screen)

        # main game loop
        while runFlag:
            pygame.display.update()

            # get inputs from events tuples
            for event in pygame.event.get():
                # did a user hit a key
                if event.type == KEYDOWN:
                    # is it the esc key
                    if event.key == K_ESCAPE:
                        runflag = False
                # if quit button stop the game
                elif event.type == QUIT:
                    runFlag = False

                # if the user clicks get the position
                # convert the position to either a cell or a border
                # if the user hit the cell update the grid from 0 -> 1
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

            # change the color of the grid cells based on the updated 2D grid
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
            # if the user hits the start button call the evolution function
            # after the start button is hit change it to next button
            if start_button.click():
                print("START")
                next_button.draw(screen)
                grid = gameOfLife(grid)

            # if the clear button is hit reset the grid
            # change next button to start
            if clear_button.click():
                grid = gridSetUp(WIDTH_SIZE,LENGTH_SIZE)
                start_button.draw(screen)

            # if the grid is clear change the button to start
            np_grid = numpy.array(grid)
            if (numpy.all(np_grid == 0)):
                start_button.draw(screen)

            clock.tick(60) #define the time

            pygame.display.flip() # update the pygame module

    # quit if runflag
    finally:
        pygame.quit()

# call main
if __name__ == '__main__':
    main()
