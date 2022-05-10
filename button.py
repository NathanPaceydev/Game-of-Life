import pygame

class Button():
    def __init__(self,x,y,image):
        width = image.get_width()
        height = image.get_height()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))
        
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