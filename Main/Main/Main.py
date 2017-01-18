import math
import pygame
from Main.Main.Database import *


##colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)


def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

class Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        size = (self.width, self.height)

        # Start PyGame
        pygame.init()

        # Program caption
        pygame.display.set_caption("Battleport V.0.0.1")
        
        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Set up the default font
        self.font = pygame.font.Font(None, 30)

        #Set up FPS
        FPS = 30
        clock = pygame.time.Clock()
        clock.tick(FPS)


    # Draw everything
    def draw_menu(self):
        # Clear the screen
        self.screen.fill((blue))
        #load menu img
        menu_bg = load_image('../../images/main_menu.png')
        self.screen.blit(menu_bg, (120, 0))
        #add buttons
        self.button(load_image('../../images/menu_play_hover.png'),load_image('../../images/menu_play.png'),220,175)
        self.button(load_image('../../images/menu_quit_hover.png'), load_image('../../images/menu_quit.png'), 220, 280)

        # Flip the screen
        pygame.display.flip()

    # button function
    def button(self,img_a,img_i,x,y):
        # buttons are 200x75
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+200 > mouse[0] > x and y+75 > mouse[1] >y:
            self.screen.blit(img_a, (x, y))
        else:
            self.screen.blit(img_i, (x, y))



    #message drawer
    def message_to_screen(self,msg, color):
        screen_text = self.font.render(msg, True, color)
        self.screen.blit(screen_text, [self.width / 2, self.height / 2])

    # The menu loop
    def game_menu(self):
        while not process_events():
            # self.draw_menu()
            self.match_start()



### match setup
    def settings_menu(self):




        pygame.display.flip()



# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    
    return False


# Main program logic
def program():
    game = Game()
    game.game_menu()


# Start the program
program()
