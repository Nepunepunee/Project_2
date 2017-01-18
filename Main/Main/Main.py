import math
import pygame

white_color = (255,255,255)
blue = (0,0,255)
class Game:
    def __init__(self):
        width = 640
        height = 480
        size = (width, height)

        # Start PyGame
        pygame.init()

        # Program caption
        pygame.display.set_caption("Battleport V.0.0.1")
        
        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Set up the default font
        self.font = pygame.font.Font(None, 30)



    # Draw everything
    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))
        
        # Flip the screen
        pygame.display.flip()

    #intro screen
    def intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill(blue)
            pygame.display.update()



    # The game loop
    def game_loop(self):
        while not process_events():

            self.draw()

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
    game.intro()
    game.game_loop()


# Start the program
program()
