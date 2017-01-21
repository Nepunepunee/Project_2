
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

def image_to_screen(img, posx, posy):
    screen_img = pygame.image.load(img).convert()
    return screen.blit(screen_img, [posx, posy])

# #setting up player attributes
### OLD CODE
# class Player:
#     health = 100
#     def __init__(self,posX,posY):
#         self.posX = 0
#         self.posY = 0
#         self.sprite = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()


class Boat:
    health = 100
    total_boats = 0
    def __init__(self,posX,posY,sprite):
        self.posX = posX
        self.posY = posY
        self.cord = posX,posY
        self.sprite = sprite
        self.hp = Boat.health
        self.attack_range = 0
        self.defence = 0
        self.defencemode = False
        Boat.total_boats += 1
        print ("boat created at " + str(self.posX) + "," + str(self.posY))
        # print (self.posX)
        # print (self.posY)
    def __del__(self):
        pass

    def attack(self):
        if self.defencemode == True:
            pass


##OLD CODE
# player1 = Player([0],[0])
# player2 = Player([0],[0])

# player1cords = (player1.posX,player1.posY)

P1_Boat1 = Boat(3,14,pygame.image.load(os.path.join('../images/P1_ship_small.png')).convert_alpha())
P1_Boat2 = Boat(6,11,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat3 = Boat(8,8,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat4 = Boat(0,11,pygame.image.load(os.path.join('../images/P1_ship_large.png')).convert_alpha())
# #
P2_Boat1 = Boat(3,0,pygame.image.load(os.path.join('../images/P2_ship_small.png')).convert_alpha())
P2_Boat2 = Boat(6,0,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat3 = Boat(8,0,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat4 = Boat(11,0,pygame.image.load(os.path.join('../images/P2_ship_large.png')).convert_alpha())




P1_boat_cords = [
    P1_Boat1.cord,
    P1_Boat2.cord,
    P1_Boat3.cord,
    P1_Boat4.cord
]
P2_boat_cords = [
    P2_Boat1.cord,
    P2_Boat2.cord,
    P2_Boat3.cord,
    P2_Boat4.cord
]


# P1boat1pos = P1_Boat1.posX,P1_Boat1.posY
# print (P1boat1pos)


def mainloop():
    gameExit = False


##OLD CODE
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

    boat_active = []

    while not gameExit:
        grid = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True

            # calculate the cordinates of the mouse position
            ## not required code , only for debugging
            if event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()
                mousecord_x = math.trunc(mousepos[0] // TILESIZE)
                mousecord_y = math.trunc(mousepos[1] // TILESIZE)
                mousecord = mousecord_x,mousecord_y

            # Select ship
            if event.type == pygame.MOUSEBUTTONDOWN:
                boat_active = selectedboat()

            def selectedboat():
                mousepos = pygame.mouse.get_pos()
                mousecord_x = math.trunc(mousepos[0] // TILESIZE)
                mousecord_y = math.trunc(mousepos[1] // TILESIZE)
                mousecord = mousecord_x, mousecord_y
                ship_selected = False
                for boat in P1_boat_cords:
                    if boat == mousecord:
                        return boat
                        print ("P1 Ship selected :" + str(selected))
                        selected_ship_img = image_to_screen('../images/P1_ship_small.png',650,370)
                        # pygame.display.flip()
                        ship_selected = True


                for boat in P2_boat_cords:
                    if boat == mousecord:
                        return boat
                        print ("P2 Ship selected :" + str(selected))
                        selected_ship_img = image_to_screen('../images/P2_ship_small.png', 650, 370)
                        # pygame.display.flip()
                        ship_selected = True

                if not ship_selected == True:
                    pass

                ## OLD TRUE / FALSE code
                # if not ship_selected:
                #     # ship_selected = False
                #     # print (ship_selected)
                #     pass

            # if boat_active != []:
            #     # screen.blit()
            #     message_to_screen("Boat Selected", blue, 625, 310)
            #     pygame.display.update()



            if event.type == pygame.MOUSEBUTTONUP:
                mousepos = pygame.mouse.get_pos()
                mousecord_x = math.trunc(mousepos[0] // TILESIZE)
                mousecord_y = math.trunc(mousepos[1] // TILESIZE)
                mousecord = mousecord_x, mousecord_y

                print ("boat active" + str(boat_active))
                boat_active = mousecord
                print("mouse up cords" + str(mousecord))






            if event.type == KEYDOWN:
                ##PLAYER1
                if (event.key == K_RIGHT) and P1_Boat1.posX < MAPWIDTH - 1:
                    # change player's x position
                    P1_Boat1.posX += 1
                if (event.key == K_LEFT) and P1_Boat1.posX > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    P1_Boat1.posX -= 1

                if (event.key == K_UP) and P1_Boat1.posY > MAPHEIGHT - MAPHEIGHT:
                    # change player's y position
                    P1_Boat1.posY -= 1
                if (event.key == K_DOWN) and P1_Boat1.posY < MAPHEIGHT - 1:
                    # change player's y position
                    P1_Boat1.posY += 1
                # if right arrow is pressed

                ##PLAYER2
                if (event.key == K_d) and P2_Boat1.posX < MAPWIDTH - 1:
                    # change player's x position
                    P2_Boat1.posX += 1
                if (event.key == K_a) and P2_Boat1.posX > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    P2_Boat1.posX -= 1

                if (event.key == K_w) and P2_Boat1.posY > MAPHEIGHT - MAPHEIGHT:
                    # change player's y position
                    P2_Boat1.posY -= 1
                if (event.key == K_s) and P2_Boat1.posY < MAPHEIGHT - 1:
                    # change player's y position
                    P2_Boat1.posY += 1



        if grid == False:
            for rw in range(MAPHEIGHT):
                for cl in range(MAPWIDTH):
                    randomnumber = random.randint(0, 15)
                    if randomnumber >= 1 or randomnumber <= 10:
                        tile = WATER

                    tilemap[rw][cl] = tile
                    screen.fill(white)

                for row in range(MAPHEIGHT):
                    for column in range(MAPWIDTH):
                        # draw the resource at that position in the tilemap, using the correct image
                        DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

                # display the player at the correct position
                #PLAYER 1
                DISPLAYSURF.blit(P1_Boat1.sprite, (P1_Boat1.posX * TILESIZE, P1_Boat1.posY * TILESIZE))
                DISPLAYSURF.blit(P1_Boat2.sprite, (P1_Boat2.posX * TILESIZE, P1_Boat2.posY * TILESIZE))
                DISPLAYSURF.blit(P1_Boat3.sprite, (P1_Boat3.posX * TILESIZE, P1_Boat3.posY * TILESIZE))
                DISPLAYSURF.blit(P1_Boat4.sprite, (P1_Boat4.posX * TILESIZE, P1_Boat4.posY * TILESIZE))

                DISPLAYSURF.blit(P2_Boat1.sprite, (P2_Boat1.posX * TILESIZE, P2_Boat1.posY * TILESIZE))
                DISPLAYSURF.blit(P2_Boat2.sprite, (P2_Boat2.posX * TILESIZE, P2_Boat2.posY * TILESIZE))
                DISPLAYSURF.blit(P2_Boat3.sprite, (P2_Boat3.posX * TILESIZE, P2_Boat3.posY * TILESIZE))
                DISPLAYSURF.blit(P2_Boat4.sprite, (P2_Boat4.posX * TILESIZE, P2_Boat4.posY * TILESIZE))


                grid = True

                # screen writings
                mousepos = pygame.mouse.get_pos()
                message_to_screen("P1 Boat1 " + "[" + str(P1_Boat1.posX) + "," + str(P1_Boat1.posY) + "]", red, 650, 10)
                message_to_screen("P1 Boat2 " + "[" + str(P1_Boat2.posX) + "," + str(P1_Boat2.posY) + "]",red,650,30)
                message_to_screen("P1 Boat3 " + "[" + str(P1_Boat3.posX) + "," + str(P1_Boat3.posY) + "]", red, 650, 50)
                message_to_screen("P1 Boat4 " + "[" + str(P1_Boat4.posX) + "," + str(P1_Boat4.posY) + "]", red, 650, 70)

                message_to_screen("P2 Boat1 " + "[" + str(P2_Boat1.posX) + "," + str(P2_Boat1.posY) + "]", blue, 650, 100)
                message_to_screen("P2 Boat2 " + "[" + str(P2_Boat2.posX) + "," + str(P2_Boat2.posY) + "]", blue, 650, 120)
                message_to_screen("P2 Boat3 " + "[" + str(P2_Boat3.posX) + "," + str(P2_Boat3.posY) + "]", blue, 650, 140)
                message_to_screen("P2 Boat4 " + "[" + str(P2_Boat4.posX) + "," + str(P2_Boat4.posY) + "]", blue, 650, 160)




                message_to_screen("Mouse Cords " + str(mousecord), black, 625, 210)
                message_to_screen("total ships: " + str(P1_Boat1.total_boats), black, 625, 230)
                message_to_screen("PLAYER1 ships: " + str(len(P1_boat_cords)), red, 625, 250)
                message_to_screen("PLAYER2 ships: " + str(len(P2_boat_cords)), blue, 625, 270)

                message_to_screen("Boat Selected: " + str(boat_active), green, 615,350)

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



