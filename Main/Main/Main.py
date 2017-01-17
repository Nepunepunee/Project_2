import pygame
import math

class Game:
    def __init__(self):
        width = 650
        height = 400
        demension = (width, height)

        pygame.init()

        self.screen = pygame.display.set_mode(demension)
        self.font = pygame.font.Font(None, 30)

        while not event_handler():
            self.screen.fill((0,0,0))
            pygame.display.flip()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

Game()