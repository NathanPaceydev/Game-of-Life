# class that contains the functional definion of a button within pygame
# button attributes include dimensions, position and image displayed
# includes methods that draw the button and define wether it has been clicked
# this class is invoked in game_of_life.py

import pygame

class Button():
    # define the button attributes
    def __init__(self,x,y,image):
        width = image.get_width()
        height = image.get_height()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    # draw the button image to the screen
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))
    
    # return wether the button was clicked
    def click(self):
        action = False
        #get mouse pos
        pos = pygame.mouse.get_pos()
        #check if mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action