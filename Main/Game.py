import math
import pygame,sys,random,os
from pygame.locals import *
from Database import *
pygame.init()


#constrants representing the different resources
WATER = 2


#a dictionary linkin recources to textures
textures = {
    WATER : pygame.image.load(os.path.join('../images/wave.png'))
}

#useful game dimensions
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 20

#a list of recources
recources = [WATER]
#use list comprehension to create our tilemap
tilemap = [[WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]



DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))






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
# class Player:
#     health = 100
#     ships = 3
#     def __init__(self,posX,posY):
#         self.posX = [0]
#         self.posY = [1]
#         self.hp = Player.health
#         self.ships = Player.ships


# player1 = Player(320, 300)
# player2 = Player(150,100)

#
#the player image
# pygame.draw.rect(screen,red,(player1Pos[0],player1Pos[1],30,30))
player1Pos = [0,0]
player1 = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()

# pygame.draw.rect(screen, blue, (player2Pos[0],player2Pos[1], 30, 30))
player2 = pygame.image.load(os.path.join('../images/player2.png')).convert_alpha()
player2Pos = [1,0]

#the position of the player [x,y]


# PLAYER2 =
# playerPos2 =[1,0]


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
    # click = pygame.mouse.get_pressed()

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     mousepos = pygame.mouse.get_pos()
            #     message_to_screen(str(mousepos),black,30,600)
            #     if mousepos > player1_posX :
            #         print ("player 1 detected")

            if event.type == KEYDOWN:
                # if right arrow is pressed
                if (event.key == K_RIGHT) and player1Pos[0] < MAPWIDTH - 1:
                    # change player's x position
                    player1Pos[0] += 1
                if (event.key == K_LEFT) and player1Pos[0] > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    player1Pos[0] -= 1
                if (event.key == K_UP) and player1Pos[1] > MAPHEIGHT - MAPHEIGHT:
                    # change player's y position
                    player1Pos[1] -= 1
                if (event.key == K_DOWN) and player1Pos[1] < MAPHEIGHT - 1:
                    # change player's y position
                    player1Pos[1] += 1
                # if right arrow is pressed

                if (event.key == K_d) and player2Pos[0] < MAPWIDTH - 1:
                    # change player's x position
                    player2Pos[0] += 1
                if (event.key == K_a) and player2Pos[0] > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    player2Pos[0] -= 1
                if (event.key == K_w) and player2Pos[1] > MAPHEIGHT - MAPHEIGHT:
                    # change player's y position
                    player2Pos[1] -= 1
                if (event.key == K_s) and player2Pos[1] < MAPHEIGHT - 1:
                    # change player's y position
                    player2Pos[1] += 1

       ##ERROR
        # loop through each row
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                randomnumber = random.randint(0, 15)
                if randomnumber >= 1 or randomnumber <= 10:
                    tile = WATER

                tilemap[rw][cl] = tile

            for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                    # draw the resource at that position in the tilemap, using the correct image
                    DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
            # display the player at the correct position
            DISPLAYSURF.blit(player1, (player1Pos[0] * TILESIZE, player1Pos[1] * TILESIZE))
            DISPLAYSURF.blit(player2, (player2Pos[0] * TILESIZE, player2Pos[1] * TILESIZE))



            # screen writings
            mousepos = pygame.mouse.get_pos()
            message_to_screen(str(mousepos),red,500,15)
            # message_to_screen("player ships: " + str(player1.ships), red,10,10)
            # message_to_screen("player ships: " + str(player2.ships), blue, 200, 10)
            # message_to_screen("HP: " + str(player1.hp), red, 10, 30)
            # message_to_screen("HP: " + str(player2.hp), blue, 200, 30)


            pygame.display.update()



    clock.tick(FPS)
    pygame.quit()

mainloop()
### end mainloop


game = Game()


game()

