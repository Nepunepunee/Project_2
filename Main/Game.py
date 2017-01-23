import math
import time
import pygame,sys,random,os
from pygame.locals import *
from Database import *
pygame.init()


#constrants representing the different resources
WATER = 2
textures = {
    WATER : pygame.image.load(os.path.join('../images/wave.png'))
}

#Grid Variables
TILESIZE = 30-1
MAPWIDTH = 20
MAPHEIGHT = 20
recources = [WATER] #a list of recources
#use list comprehension to create our tilemap
tilemap = [[WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

##Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (0,200,200)
black = (0, 0, 0)
white = (255, 255, 255)


width = (MAPWIDTH * TILESIZE) + (350)
height = (MAPHEIGHT * TILESIZE)
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

def getmousepos():
    mousepos = pygame.mouse.get_pos()
    mousecord_x = math.trunc(mousepos[0] // TILESIZE)
    mousecord_y = math.trunc(mousepos[1] // TILESIZE)
    mousecord = [mousecord_x, mousecord_y]
    return mousecord

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
        self.cord = [posX,posY]
        self.sprite = sprite
        self.hp = Boat.health
        self.attack_range = 0
        self.defence = 0
        self.defencemode = False
        Boat.total_boats += 1
        # print ("boat created at " + str(self.posX) + "," + str(self.posY))

    def get_posX(self):
        return self.posX()

    def get_posY(self):
        return self.posY()

    def set_posX(self, X):
        self.posX = X

    def set_posY(self, Y):
        self.posY = Y

    def set_position(self,X,Y):
        self.cord = X,Y
        self.posX = X
        self.posY = Y

    def get_cord_to_posX(self,cord):
        return cord[0]

    def get_cord_to_posY(self,cord):
        return cord[1]




    # @property
    # def set_posX(self):
    #     return self.posX
    #
    # @set_posX.setter
    # def set_posX(self,value):
    #     self.PosX = value
    #
    # @property
    # def set_posY(self):
    #     return self.posY
    #
    # @set_posY.setter
    # def set_posY(self,value):
    #     self.posY = value

    def __del__(self):
        pass

    def attack(self):
        if self.defencemode == True:
            pass


class cordDict:
   def __init__(self,dict):
       self.dict = dict
       self.key = dict.keys()
       self.value = dict.values()
       self.length = len(dict)

   def setcord(self,boatcord):
       for self.key, self.value in self.dict:
           self.keyvalue = boatcord




   def update(self, newdata,key,value):
       if newdata == None:
           self.dict = {}

       else:
           # for key, value in newdata:
           #     setattr(self, key, value)
            for X,Y in newdata:
                setattr(self,key,self.value)

   def dict_items(self):
       for key, value in self.dict.items():
           return key, value




##OLD CODE
# player1 = Player([0],[0])
# player2 = Player([0],[0])

# player1cords = (player1.posX,player1.posY)

#CREATE BOATS
P1_Boat1 = Boat(3,14,pygame.image.load(os.path.join('../images/P1_ship_small.png')).convert_alpha())
P1_Boat2 = Boat(6,11,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat3 = Boat(8,8,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat4 = Boat(0,11,pygame.image.load(os.path.join('../images/P1_ship_large.png')).convert_alpha())
# #
P2_Boat1 = Boat(3,0,pygame.image.load(os.path.join('../images/P2_ship_small.png')).convert_alpha())
P2_Boat2 = Boat(6,0,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat3 = Boat(8,0,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat4 = Boat(11,0,pygame.image.load(os.path.join('../images/P2_ship_large.png')).convert_alpha())

pygame.transform.flip(P2_Boat1.sprite,P2_Boat1.posX,P2_Boat1.posY)
pygame.display.update()
## References for selecting the correct boats during selecting boats in mainloop
P1_boat_cords = cordDict ({
    P1_Boat1 : P1_Boat1.cord,
    P1_Boat2 : P1_Boat2.cord,
    P1_Boat3 : P1_Boat3.cord,
    P1_Boat4 : P1_Boat4.cord
})

P2_boat_cords = cordDict({
    P2_Boat1 : P2_Boat1.cord,
    P2_Boat2 : P2_Boat2.cord,
    P2_Boat3 : P2_Boat3.cord,
    P2_Boat4 : P2_Boat4.cord
})

##OLD list style
# P1_boat_cords = [
#     P1_Boat1.cord,
#     P1_Boat2.cord,
#     P1_Boat3.cord,
#     P1_Boat4.cord
# ]
# P2_boat_cords = [
#     P2_Boat1.cord,
#     P2_Boat2.cord,
#     P2_Boat3.cord,
#     P2_Boat4.cord
# ]


# P1boat1pos = P1_Boat1.posX,P1_Boat1.posY
# print (P1boat1pos)
ship_selected = None
img = None
def mainloop():
    gameExit = False
    boat_active = {}

    while not gameExit:
        grid = False
        frame_times = []
        start_t = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True
            # calculate the cordinates of the mouse  ## not required code , only for debugging
            if event.type == pygame.MOUSEMOTION:
                mousepos = getmousepos()

            # SELECT SHIP
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boat_active == {} and img != None:
                    boat_active = selectedboat()
                elif boat_active == {}:
                    boat_active = selectedboat()
                else:
                    moveboat()

            def selectedboat():
                global img
                mousecord = getmousepos()
                print ("mousecord: " + str(mousecord))
                global ship_selected ## check if global ship_selected already contains a ship
                local_ship_selected = None ## check if ship is selected within this function
                for boat,cord in P1_boat_cords.dict.items():
                    if cord == mousecord:
                        ship_selected = True

                        ##OLD
                        # new_boat = boat_active[boat] = boat.sprite
                        # return new_boat

                        new_boat = {boat: boat.sprite}
                        return new_boat

                for boat,cord in P2_boat_cords.dict.items():
                    if cord == mousecord:
                        ship_selected = True
                        new_boat = {boat: boat.sprite}
                        return new_boat

                if local_ship_selected == None:
                    img = None
                    return {}

            if boat_active: ## if there is a ship selected.  give the img variable, the sprite of this ship (for render)
                global img
                for boat,sprite in boat_active.items():
                    img = sprite
                    break


            print(boat_active)

            ## move fixed boat to the mouse cords
            def moveboat():
                global img
                mousecord = getmousepos()
                for boat,sprite in boat_active.items():
                    # boat.set_posX = mousecord[0]
                    # boat.set_posY = mousecord[1]
                    # boat.cord = (mousecord[0],mousecord[1])
                    if mousecord[0] > MAPWIDTH-1 or mousecord[0] < 0:
                        break
                    elif mousecord[1] > MAPHEIGHT-1 or mousecord[1] < 0:
                        break
                    else:
                        boat.set_position(mousecord[0],mousecord[1])
                        print ("cords: ", (mousecord))

                        # P1_boat_cords.setcord({boat: mousecord})

                        # P1_boat_cords.setcord(mousecord)
                        # P2_boat_cords.update(mousecord[0],mousecord[1])
                        img = sprite


                    ##OLD CODE

                    # boat.posX = mousecord[0]
                    # boat.posY = mousecord[1]
                if len(str(boat_active)) > 0:
                    boat_active.clear()
                else:
                    pass

            # OLD MOVEMENT CODE
            ##PLAYER1 PosX
            if event.type == KEYDOWN:
                if (event.key == K_RIGHT) and P1_Boat1.posX < MAPWIDTH - 1:
                    # change player's x position
                    P1_Boat1.posX += 1
                if (event.key == K_LEFT) and P1_Boat1.posX > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    P1_Boat1.posX -= 1
                ##PLAYER1 PosY
                if (event.key == K_UP) and P1_Boat1.posY > MAPHEIGHT - MAPHEIGHT:
                    # change player's y position
                    P1_Boat1.posY -= 1
                if (event.key == K_DOWN) and P1_Boat1.posY < MAPHEIGHT - 1:
                    # change player's y position
                    P1_Boat1.posY += 1
                # if right arrow is pressed

                ##PLAYER2 PosX
                if (event.key == K_d) and P2_Boat1.posX < MAPWIDTH - 1:
                    # change player's x position
                    P2_Boat1.posX += 1
                if (event.key == K_a) and P2_Boat1.posX > MAPWIDTH - MAPWIDTH:
                    # change player's x position
                    P2_Boat1.posX -= 1
                ##PlayerPosY
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



                DISPLAYSURF.blit(P1_Boat1.sprite, (P1_Boat1.cord[0] * TILESIZE, P1_Boat1.cord[1] * TILESIZE))
                DISPLAYSURF.blit(P1_Boat2.sprite, (P1_Boat2.posX * TILESIZE, P1_Boat2.posY * TILESIZE))
                DISPLAYSURF.blit(P1_Boat3.sprite, (P1_Boat3.posX * TILESIZE, P1_Boat3.posY * TILESIZE))
                DISPLAYSURF.blit(P1_Boat4.sprite, (P1_Boat4.posX * TILESIZE, P1_Boat4.posY * TILESIZE))

                DISPLAYSURF.blit(P2_Boat1.sprite, (P2_Boat1.cord[0] * TILESIZE, P2_Boat1.cord[1] * TILESIZE))
                DISPLAYSURF.blit(P2_Boat2.sprite, (P2_Boat2.posX * TILESIZE, P2_Boat2.posY * TILESIZE))
                DISPLAYSURF.blit(P2_Boat3.sprite, (P2_Boat3.posX * TILESIZE, P2_Boat3.posY * TILESIZE))
                DISPLAYSURF.blit(P2_Boat4.sprite, (P2_Boat4.posX * TILESIZE, P2_Boat4.posY * TILESIZE))


                movement_up = pygame.image.load(os.path.join("../images/movement_up.png"))
                movement_down = pygame.image.load(os.path.join("../images/movement_down.png"))
                movement_left = pygame.image.load(os.path.join("../images/movement_left.png"))
                movement_right = pygame.image.load(os.path.join("../images/movement_right.png"))
                ship_selected_bg = pygame.image.load(os.path.join("../images/ship_selected_bg.png"))
                boat_bg = pygame.draw.rect(screen, red, [550, 600, 20, 20])

                DISPLAYSURF.blit(ship_selected_bg, (600, 10))
                DISPLAYSURF.blit(movement_up, (800 , 25 ))
                DISPLAYSURF.blit(movement_left, (750, 75))
                DISPLAYSURF.blit(movement_right, (850, 75))
                DISPLAYSURF.blit(movement_down, (800, 125))











                ## GET SELECTED BOAT IMAGE
                # if len(str(boat_active)) > 2:
                #     global img
                #     k, v = boat_active.items()
                #     img = v
                # DISPLAYSURF.blit(img, (650 * TILESIZE, 400 * TILESIZE))
                # print ("ship selected: " + str(ship_selected))

                #
                # ##DISPLAY CURRENT SELECTED SHIP
                if img != None:
                    screen.blit(img, (650, 60))



                grid = True

                # screen writings
                mousepos = pygame.mouse.get_pos()
                # message_to_screen("P1 Boat1 " + "[" + str(P1_Boat1.posX) + "," + str(P1_Boat1.posY) + "]", red, 650, 10)
                # message_to_screen("P1 Boat2 " + "[" + str(P1_Boat2.posX) + "," + str(P1_Boat2.posY) + "]",red,650,30)
                # message_to_screen("P1 Boat3 " + "[" + str(P1_Boat3.posX) + "," + str(P1_Boat3.posY) + "]", red, 650, 50)
                # message_to_screen("P1 Boat4 " + "[" + str(P1_Boat4.posX) + "," + str(P1_Boat4.posY) + "]", red, 650, 70)
                #
                # message_to_screen("P2 Boat1 " + "[" + str(P2_Boat1.posX) + "," + str(P2_Boat1.posY) + "]", blue, 650, 100)
                # message_to_screen("P2 Boat2 " + "[" + str(P2_Boat2.posX) + "," + str(P2_Boat2.posY) + "]", blue, 650, 120)
                # message_to_screen("P2 Boat3 " + "[" + str(P2_Boat3.posX) + "," + str(P2_Boat3.posY) + "]", blue, 650, 140)
                # message_to_screen("P2 Boat4 " + "[" + str(P2_Boat4.posX) + "," + str(P2_Boat4.posY) + "]", blue, 650, 160)

                # message_to_screen("P2 Boat3 " + "[" + str(P2_Boat3.posX) + "," + str(P2_Boat3.posY) + "]", blue, 650, 140)
                # message_to_screen("P2 Boat4 " + "[" + str(P2_Boat4.posX) + "," + str(P2_Boat4.posY) + "]", blue, 650, 160)



                end_t = time.time()
                time_taken = end_t - start_t
                start_t = end_t
                frame_times.append(time_taken)
                frame_times = frame_times[-20:]
                fps_count = len(frame_times) / sum(frame_times)

                message_to_screen("Mouse Cords " + str(getmousepos()), black, 625, 210)
                message_to_screen("total ships: " + str(P1_Boat1.total_boats), black, 625, 230)
                message_to_screen("PLAYER1 ships: " + str(P1_boat_cords.length), red, 625, 250)
                message_to_screen("PLAYER2 ships: " + str(P2_boat_cords.length), blue, 625, 270)
                message_to_screen("FPS: " + str(round(fps_count, 0)), black, 625, 300)

                message_to_screen("Boat Selected:", black, 615,15)
                message_to_screen(str(boat_active), black, 600, 160)


                # message_to_screen("P2 boat1 cord: " + (str(P2_Boat1.cord), green, 615, 450))

                # message_to_screen("player ships: " + str(player1.ships), red,10,10)
                # message_to_screen("player ships: " + str(player2.ships), blue, 200, 10)
                # message_to_screen("HP: " + str(player1.hp), red, 10, 30)
                # message_to_screen("HP: " + str(player2.hp), blue, 200, 30)


                pygame.display.flip()
    clock.tick(FPS)
    pygame.quit()
mainloop()
### end mainloop


game = Game()


game()



