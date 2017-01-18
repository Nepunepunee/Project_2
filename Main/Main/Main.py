import math
import pygame
###
##colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = 0,0,0
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
        self.screen.fill((white))
        # draw block for menu items

        # load main menu image
        # load_image('main_menu.png')

        # Flip the screen
        pygame.display.flip()

        #message drawer
    def message_to_screen(self,msg, color):
        screen_text = self.font.render(msg, True, color)
        self.screen.blit(screen_text, [self.width / 2, self.height / 2])

    # The game loop
    def game_loop(self):
        while not process_events():

            self.draw_menu()


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
    game.game_loop()


# Start the program
program()
