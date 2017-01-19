import math
import pygame
from Database import *
pygame.init()

##colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


width = 640
height = 480
menu = True
size = (width, height)
# Start PyGame
pygame.init()
# Program caption
pygame.display.set_caption("Battleport V.0.0.1")
# Set the resolution
screen = pygame.display.set_mode(size)
# Set up the default font
pygame.display.update()
font = pygame.font.Font(None, 24)
# Set up FPS
FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)

def quitgame():
    pygame.quit()
    quit()

def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

# message drawer
def message_to_screen(msg,color,posx,posy):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [posx,posy])

#setting up player attributes
class Player:
    health = 100
    ships = 3
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.hp = Player.health
        self.ships = Player.ships


player1 = Player(320, 300)
player2 = Player(width//2, height//2)

def mainloop():
    gameExit = False

#Player positions
    player1_posX = 0
    player1_posY = 0
    player2_posX = 0
    player2_posY = 0

#Player position movements
    player1_posX_change = 0
    player1_posY_change = 0
    player1_posX_change = 0
    player1_posY_change = 0

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     mousepos = pygame.mouse.get_pos()
            #     message_to_screen(str(mousepos),black,30,600)
                # if mousepos > player1_posX :
                #     print ("player 1 detected")

        screen.fill(white)
        #screen writings
        mousepos = pygame.mouse.get_pos()
        message_to_screen(str(mousepos),red,500,15)
        message_to_screen("player ships: " + str(player1.ships), red,10,10)
        message_to_screen("player ships: " + str(player2.ships), blue, 200, 10)
        message_to_screen("HP: " + str(player1.hp), red, 10, 30)
        message_to_screen("HP: " + str(player2.hp), blue, 200, 30)
        P1 = pygame.draw.rect(screen,red,(player1.posX,player1.posY,30,30))
        P2 = pygame.draw.rect(screen, blue, (player2.posX, player2.posY, 30, 30))
        pygame.display.update()



    clock.tick(FPS)
    pygame.quit()
mainloop()
### end mainloop


game = Game()


game()

