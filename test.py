
import pygame

import button

from pygame import (
    MOUSEBUTTONDOWN,
    QUIT,
    K_ESCAPE,
    KEYDOWN
)

WINDOW_SIZE =(500,500)
LENGTH_SIZE = 10
HEIGHT, WIDTH = 20,20
MARGIN = 5
#define some constants
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

pygame.display.set_caption("$$ TEST $$ Game of Life")


arrow_image = pygame.image.load("start_btn.png").convert_alpha()
next_image = pygame.image.load("next_btn.png").convert_alpha()
exit_image = pygame.image.load("exit_btn.png").convert_alpha()

arrow_image = pygame.transform.scale(arrow_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
next_image = pygame.transform.scale(next_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
exit_image = pygame.transform.scale(exit_image,((WINDOW_SIZE[0]/3,HEIGHT*2)))
    

start_button = button.Button(WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)), arrow_image)
exit_button = button.Button(WINDOW_SIZE[0]-WINDOW_SIZE[0]/3-WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)),exit_image)
next_button = button.Button(WINDOW_SIZE[0]/10,(HEIGHT*LENGTH_SIZE+MARGIN*(LENGTH_SIZE+1)), next_image)
pygame.init()

clock = pygame.time.Clock()

runFlag = True


while runFlag:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            #do something
            print("scale")

        # did a user hit a key
        if event.type == KEYDOWN:
            # is it the esc key
            if event.key == K_ESCAPE:
                runflag = False

        elif event.type == QUIT:
            runFlag = False
     # it will set background color of screen
    screen.fill((255, 255, 255))
    
    start_button.draw(screen)
    
    if start_button.draw(screen):
        next_button.draw(screen)
       

    #grid = gameOfLife(grid)

    if exit_button.draw(screen):
    #    #grid = gridSetUp(WIDTH_SIZE,LENGTH_SIZE)
        #runFlag = False
       print("exit")

    clock.tick(60)

    pygame.display.flip()