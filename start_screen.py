from cmath import log
import pygame
import sys


def start():
    count = 0
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 500
    

    # it will display on screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    icon = pygame.image.load("icon.png").convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Game of Life")

    logo = pygame.image.load('logo.JPG').convert_alpha()
    logo = pygame.transform.scale(logo,((SCREEN_WIDTH-100,SCREEN_HEIGHT/3)))
    
    

    # basic font for user typed
    base_font = pygame.font.Font(None, 30)
    user_text = ''
    input_text = base_font.render('Enter the Width of the Grid:', True, (1,0,128))
    input_text_Rect = input_text.get_rect()
    input_text_Rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50)
    # create rectangle
    input_rect = pygame.Rect(SCREEN_WIDTH/2-130,SCREEN_HEIGHT/2+75, 200, 32)
    
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
    
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    
    
    active = False
    
    while True:
        for event in pygame.event.get():
    
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode

                if event.key == pygame.K_RETURN:
                    if count == 0:
                        width = user_text
                        user_text = ''
                        input_text = base_font.render('Enter the Height of the Grid:', True, (200,0,150))

                    if count == 1:
                        length = user_text
                        user_text = ''
                        return width,length

                    count+=1
               
        # it will set background color of screen
        screen.fill((255, 255, 255))
    
        if active:
            color = color_active
        else:
            color = color_passive
            
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        screen.blit(input_text,input_text_Rect)
        screen.blit(logo,(SCREEN_WIDTH/10,SCREEN_HEIGHT/15))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(200, text_surface.get_width()+10)
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)