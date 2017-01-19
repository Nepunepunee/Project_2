import math
import pygame
from Database import *
pygame.init()

##colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)


def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

# Main program logic
def program():
    game = Game()
    game.game_menu()
    game.game_loop()

class Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.menu = True
        size = (self.width, self.height)

        # Start PyGame
        pygame.init()

        # Program caption
        pygame.display.set_caption("Battleport V.0.0.2")
        
        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Set up the default font
        self.font = pygame.font.Font(None, 30)

        #Set up FPS
        FPS = 30
        clock = pygame.time.Clock()
        clock.tick(FPS)

        pygame.mixer.init()
        pygame.mixer.music.load("../../sounds/main.wav")
        pygame.mixer.music.play(-1)


    def quitgame(self):
        pygame.quit()
        quit()

    # Draw menu
    def draw_menu(self):
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # Clear the screen
            self.screen.fill((blue))
            #load menu img
            menu_bg = load_image('../../images/main_menu.png')
            self.screen.blit(menu_bg, (120, 0))
            #add buttons
            self.button(load_image('../../images/menu_play_hover.png'),load_image('../../images/menu_play.png'),250,150,
            self.match_start)

            self.button(load_image('../../images/menu_highscore_hover.png'), load_image('../../images/menu_highscore.png'), 250,225,
            self.match_start)

            self.button(load_image('../../images/menu_settings_hover.png'),load_image('../../images/menu_settings.png'), 250, 300,
            self.settings_menu)

            self.button(load_image('../../images/menu_quit_hover.png'), load_image('../../images/menu_quit.png'), 250, 375,
            self.quitgame)
            # Flip the screen
            pygame.display.flip()

    # Game match
    def match_start(self):
        pygame.display.flip()
        self.menu = False
        self.screen.fill((white))


    # button function
    def button(self,img_a,img_i,x,y,action=None):
        # buttons are 200x75
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+200 > mouse[0] > x and y+75 > mouse[1] >y:
            self.screen.blit(img_a, (x, y))
            if click[0] == 1 and action != None:
                action()
        else:
            self.screen.blit(img_i, (x, y))

    #message drawer
    def message_to_screen(self,msg, color):
        screen_text = self.font.render(msg, True, color)
        self.screen.blit(screen_text, [self.width / 2, self.height / 2])

    # The menu loop
    def game_menu(self):
        while not process_events():
            # self.settings_menu()
            self.draw_menu()

    # The game loop
    def game_loop(self):
        while not process_events():
            self.match_start()



### settings menu
    def settings_menu(self):
        self.screen.fill((blue))
        menu_settings = load_image('../../images/settings_menu.png')
        self.screen.blit(menu_settings, (120, 0))
        # volume mixer
        volume = pygame.mixer.music.get_volume()

        pygame.display.flip()

# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    
    return False



# Start the program
program()
