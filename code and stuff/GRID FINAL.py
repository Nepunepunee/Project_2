import pygame, sys, random, os
from pygame.locals import *

#constrants representing colours
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#constrants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

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


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))


#the player image
PLAYER1 = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()
#the position of the player [x,y]
playerPos1 =[0,0]

PLAYER2 = pygame.image.load(os.path.join('../images/player2.png')).convert_alpha()
playerPos2 =[1,0]

#loop through each row
for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomnumber = random.randint(0,15)
        if randomnumber >= 1 or randomnumber <= 10:
            tile = WATER

        tilemap[rw][cl]=tile
while True:
    #get all the user events
    for event in pygame.event.get():
        if event.type == QUIT:
            #and the game and close window
            pygame.quit()
            sys.exit()
        #if a key is pressed
        elif event.type == KEYDOWN:
            #if right arrow is pressed
            if (event.key==K_RIGHT) and playerPos1[0]< MAPWIDTH-1:
                #change player's x position
                playerPos1[0]+=1
            if (event.key==K_LEFT) and playerPos1[0]> MAPWIDTH-MAPWIDTH:
                #change player's x position
                playerPos1[0]-=1
            if (event.key==K_UP) and playerPos1[1]> MAPHEIGHT-MAPHEIGHT:
                #change player's y position
                playerPos1[1]-=1
            if (event.key==K_DOWN) and playerPos1[1]< MAPHEIGHT-1:
                #change player's y position
                playerPos1[1]+=1
            #if right arrow is pressed
            if (event.key==K_d) and playerPos2[0]< MAPWIDTH-1:
                #change player's x position
                playerPos2[0]+=1
            if (event.key==K_a) and playerPos2[0]> MAPWIDTH-MAPWIDTH:
                #change player's x position
                playerPos2[0]-=1
            if (event.key==K_w) and playerPos2[1]> MAPHEIGHT-MAPHEIGHT:
                #change player's y position
                playerPos2[1]-=1
            if (event.key==K_s) and playerPos2[1]< MAPHEIGHT-1:
                #change player's y position
                playerPos2[1]+=1
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct image
            DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))
    # display the player at the correct position
    DISPLAYSURF.blit(PLAYER1, (playerPos1[0] * TILESIZE, playerPos1[1] * TILESIZE))
    DISPLAYSURF.blit(PLAYER2, (playerPos2[0] * TILESIZE, playerPos2[1] * TILESIZE))
    pygame.display.update()