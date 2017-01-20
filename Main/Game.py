
import math
import pygame,sys,random,os
from pygame.locals import *
from Database import *
pygame.init()


#constrants representing the different resources
WATER = 2

textures = {
    WATER : pygame.image.load(os.path.join('../images/wave.png'))
}

#useful game dimensions
TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15
recources = [WATER] #a list of recources
#use list comprehension to create our tilemap
tilemap = [[WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

##colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (0,200,200)
black = (0, 0, 0)
white = (255, 255, 255)


width = (MAPWIDTH * 40) +(200)
height = (MAPHEIGHT * 40) + (200)
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
    def __init__(self,posX,posY):
        self.posX = [0]
        self.posY = [0]
        self.sprite = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()


class Boat:
    def __init__(self):
        self.hp = 100
        self.attack_range = 0
        self.defence = 0
        self.defencemode = False

    def __del__(self):
        pass

    def attack(self):
        if self.defencemode == True:
            pass



player1 = Player([0],[0])
player2 = Player([0],[0])

P1_Boat1 = Boat()
P1_Boat2 = Boat()
P1_Boat3 = Boat()
P1_Boat4 = Boat()

P2_Boat1 = Boat()
P2_Boat2 = Boat()
P2_Boat3 = Boat()
P2_Boat4 = Boat()





#
#the player image
# pygame.draw.rect(screen,red,(player1Pos[0],player1Pos[1],30,30))
player1Pos = [0,0]
player1 = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()

# pygame.draw.rect(screen, blue, (player2Pos[0],player2Pos[1], 30, 30))
player2 = pygame.image.load(os.path.join('../images/player2.png')).convert_alpha()
player2Pos = [1,0]





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


    while not gameExit:
        grid = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True

            # calculate the cordinates of the mouse position
            if event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()
                mousecord_x = math.trunc(mousepos[0] // TILESIZE)
                mousecord_y = math.trunc(mousepos[1] // TILESIZE)
                mousecord = [mousecord_x,mousecord_y]

            #     new_position = []
            mousepos = pygame.mouse.get_pos()
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

        if grid == False:
            for rw in range(MAPHEIGHT):
                for cl in range(MAPWIDTH):
                    randomnumber = random.randint(0, 15)
                    if randomnumber >= 1 or randomnumber <= 10:
                        tile = WATER

                    tilemap[rw][cl] = tile
                    screen.fill(lightblue)

                for row in range(MAPHEIGHT):
                    for column in range(MAPWIDTH):
                        # draw the resource at that position in the tilemap, using the correct image
                        DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
                # display the player at the correct position
                DISPLAYSURF.blit(player1, (player1Pos[0] * TILESIZE, player1Pos[1] * TILESIZE))
                DISPLAYSURF.blit(player2, (player2Pos[0] * TILESIZE, player2Pos[1] * TILESIZE))
                grid = True



                # screen writings
                mousepos = pygame.mouse.get_pos()
                message_to_screen("PLAYER1 " + str(player1Pos),red,650,15)
                message_to_screen("PLAYER2 " + str(player2Pos), blue, 650, 40)
                message_to_screen("Mouse Cords " + str(mousecord), black, 625, 65)
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



