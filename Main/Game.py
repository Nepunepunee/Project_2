import math
import time
import pygame,sys,random,os
from pygame.locals import *
from Database import *
pygame.init()



##Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (0,200,200)
black = (0, 0, 0)
white = (255, 255, 255)

#Grid Variables
tilesize = 29
mapwidth = 20
mapheight = 20
water = 2
block = 6
textures = {water : pygame.image.load(os.path.join('../images/wave.png')),
            block: pygame.image.load(os.path.join('../images/invblock1.png'))}

###NEWCODE###
inv = [0,0,0,0,0,0,0]
ply =[0,0]

###NEWCODE###
#constrants representing the cards
ADRENALINERUSH = 10
ADVANCEDRIFLING = 11
ALUMINIUMHULL = 12
BACKUP = 13
EMPUPGRADE = 14
EXTRAFUEL = 15
FARSIGHT = 16
FLAKARMOR = 17
FMJUPGRADE = 18
HEADSHOT = 19
JACKSPARROW = 20
NAVALMINE = 21
RALLY = 22
REINFORCEDHULL = 23
REPAIR = 24
RIFLING = 25
SABOTAGE = 26
SMOKESCREEN = 27
SONAR = 28


class card:
    def __init__(self,turndeck,img):
        self.turndeck = turndeck
        self.img = img

ADRENALINERUSH = card('ADRENALINERUSH',pygame.image.load(os.path.join("../images/adrenalinerush.png")))
ADVANCEDRIFLING = card('ADVANCEDRIFLING',pygame.image.load(os.path.join("../images/advancedrifling.png")))
ALUMINIUMHULL = card('ALUMINIUMHULL',pygame.image.load(os.path.join("../images/aluminiumhull.png")))
BACKUP = card('BACKUP',pygame.image.load(os.path.join("../images/backup.png")))
EMPUPGRADE = card('EMPUPGRADE',pygame.image.load(os.path.join("../images/empupgrade.png")))
EXTRAFUEL = card('EXTRAFUEL',pygame.image.load(os.path.join("../images/extrafuel.png")))
FARSIGHT = card('FARSIGHT',pygame.image.load(os.path.join("../images/farsight.png")))
FLAKARMOR = card('FLAKARMOR',pygame.image.load(os.path.join("../images/flakarmor.png")))
FMJUPGRADE = card('FMJUPGRADE',pygame.image.load(os.path.join("../images/fmjupgrade.png")))
HEADSHOT = card('HEADSHOT',pygame.image.load(os.path.join("../images/headshot.png")))
JACKSPARROW = card('JACKSPARROW',pygame.image.load(os.path.join("../images/jacksparrow.png")))
NAVALMINE = card('NAVALMINE',pygame.image.load(os.path.join("../images/navalmine.png")))
RALLY = card('RALLY',pygame.image.load(os.path.join("../images/rally.png")))
REINFORCEDHULL = card('REINFORCEDHULL',pygame.image.load(os.path.join("../images/reinforcedhull.png")))
REPAIR = card('REPAIR',pygame.image.load(os.path.join("../images/repair.png")))
RIFLING = card('RIFLING',pygame.image.load(os.path.join("../images/rifling.png")))
SABOTAGE = card('SABOTAGE',pygame.image.load(os.path.join("../images/sabotage.png")))
SMOKESCREEN = card('SMOKESCREEN',pygame.image.load(os.path.join("../images/smokescreen.png")))
SONAR = card('SONAR',pygame.image.load(os.path.join("../images/sonar.png")))


turndeck = [FMJUPGRADE,FMJUPGRADE,RIFLING,RIFLING,ADVANCEDRIFLING,ADVANCEDRIFLING,NAVALMINE,NAVALMINE,NAVALMINE,
           NAVALMINE,NAVALMINE,NAVALMINE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,BACKUP,BACKUP,EXTRAFUEL,EXTRAFUEL,
           EXTRAFUEL,EXTRAFUEL,RALLY,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,REINFORCEDHULL,SONAR,
           REINFORCEDHULL,SONAR,SONAR,SONAR,SMOKESCREEN,SMOKESCREEN,SABOTAGE,SABOTAGE]

# specialdeck = [REPAIR,REPAIR,FLAKARMOR,FLAKARMOR,HEADSHOT,JACKSPARROW,FARSIGHT,ALUMINIUMHULL]

recources = [water] #a list of recources
tilemap = [[water for w in range(mapwidth)] for h in range(mapheight)] #use list comprehension to create our tilemap
displaysurf = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))

#GAME SETUP
width = (mapwidth * tilesize) + (350)
height = (mapheight * tilesize)
menu = True
size = (width, height)
pygame.init()
pygame.display.set_caption("Battleport V.1.0.1")
screen = pygame.display.set_mode(size)
pygame.display.update()
font = pygame.font.Font(None, 24)

FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)

##GLOBAL FUNCTIONS
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
    mousecord_x = math.trunc(mousepos[0] // tilesize)
    mousecord_y = math.trunc(mousepos[1] // tilesize)
    mousecord = [mousecord_x, mousecord_y]
    return mousecord

def getpixelcord(pX,pY):
    cord_x = math.trunc(pX * tilesize)
    cord_y = math.trunc(pY * tilesize)
    cord = cord_x, cord_y
    return cord

class Player:
    boats = 4
    def __init__(self):
        self.boats = Player.boats


class Boat:
    health = 100
    total_boats = 0
    def __init__(self,posXhead,posYhead,length,sprite):
        self.posXhead = posXhead
        self.posYhead = posYhead
        self.posXtail = posXhead
        self.posYtail = posYhead + (length-1)
        self.length = length
        self.cordhead = [posXhead,posYhead]
        self.cordtail = [self.posXtail,self.posYtail]
        self.sprite = sprite
        self.hp = Boat.health
        self.attack_range = 0
        self.defence = 0
        self.defencemode = False
        Boat.total_boats += 1

    def get_posX(self):
        return self.posX()
    def get_posY(self):
        return self.posY()
    def set_posX(self, X):
        self.posX = X
    def set_posY(self, Y):
        self.posY = Y
    def set_position(self,X,Y):
        self.cordhead = X,Y
        self.posXhead = X
        self.posYhead = Y

    def get_cord_to_posX(self,cord):
        return cord[0]
    def get_cord_to_posY(self,cord):
        return cord[1]

    def __del__(self):
        pass
    def attack(self):
        if self.defencemode == True:
            pass

                ##OLD getter and setter experimental code (maybe need this)
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


class sprite(pygame.sprite.Sprite):
    def __init__(self,image,rectx,recty,width,height):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(); #here rect is created
        self.rect.x = rectx
        self.rect.y = recty

    def draw(self, screen):
        screen.blit(self.image, self.rect)

## Sprite GROUPS
movement_up = sprite(pygame.image.load(os.path.join('../images/movement_up.png')).convert_alpha(),660,25,30,30)
movement_left = sprite(pygame.image.load(os.path.join('../images/movement_left.png')).convert_alpha(),625,60,30,30)
movement_right = sprite(pygame.image.load(os.path.join('../images/movement_right.png')).convert_alpha(),695,60,30,30)
movement_down = sprite(pygame.image.load(os.path.join('../images/movement_down.png')).convert_alpha(),660,95,30,30)
end_button = sprite(pygame.image.load(os.path.join('../images/int_end.png')).convert_alpha(),680,170,60,30)

sprites_1 = pygame.sprite.Group() ## MOVEMENT INTERFACE
sprites_1.add(movement_up,movement_left,movement_right,movement_down,end_button)



# movement_up = pygame.sprite.Sprite()
# arrowsprite.rect.x = 650
# arrowsprite.rect.y = 30

##CREATE DIFFERENT TILES
movement_tile = pygame.image.load(os.path.join("../images/movement_tile.png"))
attack_tile = pygame.image.load(os.path.join("../images/attack_tile.png"))

##interface buttons and art
movement_up = pygame.image.load(os.path.join("../images/movement_up.png"))
movement_down = pygame.image.load(os.path.join("../images/movement_down.png"))
movement_left = pygame.image.load(os.path.join("../images/movement_left.png"))
movement_right = pygame.image.load(os.path.join("../images/movement_right.png"))
ship_selected_bg = pygame.image.load(os.path.join("../images/ship_selected_bg.png"))
inventory_bg = pygame.image.load(os.path.join("../images/inventory_bg.png"))

#CREATE BOATS
P1_Boat1 = Boat(3,18,1,pygame.image.load(os.path.join('../images/P1_ship_small.png')).convert_alpha())
P1_Boat2 = Boat(6,17,2,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat3 = Boat(10,18,2,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat4 = Boat(16,13,3,pygame.image.load(os.path.join('../images/P1_ship_large.png')).convert_alpha())
# #
P2_Boat1 = Boat(13,3,1,pygame.image.load(os.path.join('../images/P2_ship_small.png')).convert_alpha())
P2_Boat2 = Boat(11,2,2,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat3 = Boat(3,6,2,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat4 = Boat(6,4,3,pygame.image.load(os.path.join('../images/P2_ship_large.png')).convert_alpha())

##DEBUGGING PRINTS FOR CORD CHECK
print ("P1_Boat1: HEAD: ",P1_Boat1.cordhead, " TAIL: ",P1_Boat1.cordtail)
print ("P1_Boat2: HEAD: ",P1_Boat2.cordhead, " TAIL: ",P1_Boat2.cordtail)
print ("P1_Boat3: HEAD: ",P1_Boat3.cordhead, " TAIL: ",P1_Boat3.cordtail)
print ("P1_Boat4: HEAD: ",P1_Boat4.cordhead, " TAIL: ",P1_Boat4.cordtail)

## References for selecting the correct boats during selecting boats in mainloop
P1_boat_cords = cordDict ({
    P1_Boat1 : (P1_Boat1.cordhead,P1_Boat1.cordtail),
    P1_Boat2 : (P1_Boat2.cordhead,P1_Boat2.cordtail),
    P1_Boat3 : (P1_Boat3.cordhead,P1_Boat3.cordtail),
    P1_Boat4 : (P1_Boat4.cordhead,P2_Boat4.cordtail)
})
P2_boat_cords = cordDict({
    P2_Boat1 : (P2_Boat1.cordhead,P2_Boat1.cordtail),
    P2_Boat2 : (P2_Boat2.cordhead,P2_Boat2.cordtail),
    P2_Boat3 : (P2_Boat3.cordhead,P2_Boat3.cordtail),
    P2_Boat4 : (P2_Boat4.cordhead,P2_Boat4.cordtail)
})

def mainloop():
    ship_selected_img = None
    attack_mode = False
    tiles_render = False
    gameExit = False
    mousemotion = False
    boat_active = []
    movement_tiles = []
    attack_tiles = []

    P1_inventory_full = False
    P2_inventory_full = False
    P1_carddraw = []
    P2_carddraw = []

    ##ROUND counter
    roundtime = 30
    start_ticks = pygame.time.get_ticks()  # starter tick

    while not gameExit:
        global mousemotion
        grid = False

        ## FPS counter
        frame_times = []
        start_t = time.time()



        for event in pygame.event.get(): ##STATE CHECK
            if event.type == pygame.MOUSEMOTION:
                mousemotion = True
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return "pause"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = getmousepos()
                if boat_active == [] and ship_selected_img != None:
                    boat_active = selectedboat()
                elif boat_active == []:
                    boat_active = selectedboat()
                # elif movement_up.collidepoint():
                #     print ("pressed on sprites")
                else:
                    moveboat()

        def selectedboat():
            global ship_selected_img
            ship_selected = False ## check if ship is selected within this function
            mousecord = getmousepos()
            for boat,cord in P1_boat_cords.dict.items():
                # print ("boatcord 1 ",cord[0:1])
                # print ("boatcord 2 ",cord[1:2])
                if mousecord in cord[0:1] or mousecord in cord[1:2]:
                    ship_selected = True
                    # new_boat = {boat: boat.sprite}
                    new_boat = [boat]
                    return new_boat

            for boat,cord in P2_boat_cords.dict.items():
                if mousecord in cord[0:1] or mousecord in cord[1:2]:
                    ship_selected = True
                    # new_boat = {boat: boat.sprite}
                    new_boat = [boat]
                    return new_boat

            if not ship_selected:
                del movement_tiles[:]
                del attack_tiles[:]
                ship_selected_img = None
                return []

        print (boat_active)
        if boat_active: ## if there is a ship selected.  give the img variable, the sprite of this ship (for render)
            while not tiles_render:
                for boat in boat_active:
                    ship_selected_img = boat.sprite

                    boatcord = boat.cordhead #SHOW AVAILABLE STEPS
                    if boat.length == 1:
                        movementrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]-1,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]+1]
                    elif boat.length == 2:
                        movementrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]-1,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]+2],\
                                        [boatcord[0]+1,boatcord[1]-(-1)],[boatcord[0]+(-1),boatcord[1]+1]
                    elif boat.length == 3:
                        movementrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]-1,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]+3], \
                                        [boatcord[0]+1,boatcord[1]-(-1)],[boatcord[0]+(-1),boatcord[1]+1],[boatcord[0]+1,boatcord[1]-(-2)],\
                                        [boatcord[0]+(-1),boatcord[1]+ 2]
                    for cord in movementrange:
                        movement_tiles.append(cord)
                        if len(movement_tiles) == len(movementrange):
                            break ## MEMORY LEAK BUG, needs to stop appending when all tiles have been added to list
                tiles_render = True
        if not boat_active:
            ship_selected_img = None
            tiles_render = False


        def moveboat():  ## move fixed boat to the mouse cords
            global ship_selected_img
            global attack_mode
            global tiles_render
            attack_toggle = False
            mousecord = getmousepos()
            for boat in boat_active:
                if mousecord in movement_tiles:
                    boat.set_position(mousecord[0], mousecord[1])
                    print (movement_tiles)
                    del movement_tiles[:]
                    attack_toggle = True
                elif mousecord[0] > mapwidth-1 or mousecord[0] < 0:
                    break
                elif mousecord[1] > mapheight-1 or mousecord[1] < 0:
                    break
                elif mousecord != boat.cordhead or mousecord not in movement_tiles:
                    ship_selected_img = None
                    boat_active.clear()
                    del movement_tiles[:]
                    del attack_tiles[:]
                    tiles_render = False
                    break
            if attack_toggle == True:
                del movement_tiles[:]
                attackmode()
            else:
                pass


        def attackmode():
            global attack
            attack = True
            for boat in boat_active:

                boatcord = boat.cordhead #SHOW AVAILABLE ATTACK TILES
                if boat.length == 1:
                    attackrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]+2,boatcord[1]],[boatcord[0]-1,boatcord[1]],\
                                  [boatcord[0]-2,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]-2], \
                                  [boatcord[0], boatcord[1]+1], [boatcord[0], boatcord[1]+2]
                elif boat.length == 2:
                    attackrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]+2,boatcord[1]],[boatcord[0]-1,boatcord[1]],\
                                  [boatcord[0]-2,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]-2], \
                                  [boatcord[0],boatcord[1]+2],[boatcord[0], boatcord[1]+3],[boatcord[0]+1,boatcord[1]-(-1)],\
                                  [boatcord[0]+(-1),boatcord[1]+1],[boatcord[0]+2,boatcord[1]-(-1)],[boatcord[0]+(-2),boatcord[1]+1]
                elif boat.length == 3:
                    attackrange = [boatcord[0]+1,boatcord[1]],[boatcord[0]+2,boatcord[1]],[boatcord[0]-1,boatcord[1]],\
                                  [boatcord[0]-2,boatcord[1]],[boatcord[0],boatcord[1]-1],[boatcord[0],boatcord[1]-2],\
                                  [boatcord[0], boatcord[1]+3],[boatcord[0], boatcord[1]+4],[boatcord[0], boatcord[1]+3],\
                                  [boatcord[0]+1,boatcord[1]-(-1)],[boatcord[0]+(-1),boatcord[1]+1],[boatcord[0]+2,boatcord[1]-(-1)],\
                                  [boatcord[0]+(-2),boatcord[1]+1],[boatcord[0]+1,boatcord[1]-(-2)],[boatcord[0]+(-1),boatcord[1]+2],\
                                  [boatcord[0]+2,boatcord[1]-(-2)],[boatcord[0]+(-2),boatcord[1]+2]

                for tile in attackrange:
                    attack_tiles.append(tile)
                    if len(tile) == len(attackrange):
                        break
            # print (attack_tiles)
            # if attack_tiles.get_rect().collidepoint(pygame.mouse.get_pos()):
            #     print ("hovering over tiles")


        ##DRAW GRID
        if grid == False:
            for rw in range(mapheight):
                for cl in range(mapwidth):
                    randomnumber = random.randint(0, 15)
                    if randomnumber >= 1 or randomnumber <= 10:
                        tile = water
                    tilemap[rw][cl] = tile
                    screen.fill(white)

                for row in range(mapheight):
                    for column in range(mapwidth): ##DRAW GRID
                        displaysurf.blit(textures[tilemap[row][column]], (column * tilesize, row * tilesize))
                # blit the boats at the correct position on the grid
                displaysurf.blit(P1_Boat1.sprite, (P1_Boat1.cordhead[0] * tilesize, P1_Boat1.cordhead[1] * tilesize))
                displaysurf.blit(P1_Boat2.sprite, (P1_Boat2.cordhead[0] * tilesize, P1_Boat2.cordhead[1] * tilesize))
                displaysurf.blit(P1_Boat3.sprite, (P1_Boat3.cordhead[0] * tilesize, P1_Boat3.cordhead[1] * tilesize))
                displaysurf.blit(P1_Boat4.sprite, (P1_Boat4.cordhead[0] * tilesize, P1_Boat4.cordhead[1] * tilesize))

                displaysurf.blit(P2_Boat1.sprite, (P2_Boat1.cordhead[0] * tilesize, P2_Boat1.cordhead[1] * tilesize))
                displaysurf.blit(P2_Boat2.sprite, (P2_Boat2.cordhead[0] * tilesize, P2_Boat2.cordhead[1] * tilesize))
                displaysurf.blit(P2_Boat3.sprite, (P2_Boat3.cordhead[0] * tilesize, P2_Boat3.cordhead[1] * tilesize))
                displaysurf.blit(P2_Boat4.sprite, (P2_Boat4.cordhead[0] * tilesize, P2_Boat4.cordhead[1] * tilesize))


                ###DRAW INTERFACE ELEMENTS
                # boat_bg = pygame.draw.rect(screen, red, [550, 600, 20, 20])
                displaysurf.blit(ship_selected_bg, (600, 10))
                displaysurf.blit(inventory_bg, (600, 225))
                # displaysurf.blit(movement_up, (660, 25))
                # displaysurf.blit(movement_left, (625, 60))
                # displaysurf.blit(movement_right, (695, 60))
                # displaysurf.blit(movement_down, (660, 95))





                ##DRAW CARD SLOTS (PLAYER1)
                message_to_screen("PLAYER1: ", red, 620, 250)
                displaysurf.blit(textures[block], (620, 275))
                displaysurf.blit(textures[block], (660, 275))
                displaysurf.blit(textures[block], (700, 275))
                displaysurf.blit(textures[block], (740, 275))
                displaysurf.blit(textures[block], (780, 275))
                displaysurf.blit(textures[block], (820, 275))
                displaysurf.blit(textures[block], (860, 275))

                ##DRAW CARD SLOTS (PLAYER2)
                message_to_screen("PLAYER2: ", blue, 620, 350)
                displaysurf.blit(textures[block], (620, 375))
                displaysurf.blit(textures[block], (660, 375))
                displaysurf.blit(textures[block], (700, 375))
                displaysurf.blit(textures[block], (740, 375))
                displaysurf.blit(textures[block], (780, 375))
                displaysurf.blit(textures[block], (820, 375))
                displaysurf.blit(textures[block], (860, 375))

                # SPRITES experimental code
                sprites_1.draw(screen)



                ## DRAW ACTIVE STUFF NEEDS REWORK (ALL DRAW STUFF)
                if len(movement_tiles) > 0:
                    for tile in movement_tiles:
                        cord = getpixelcord(tile[0],tile[1])
                        screen.blit(movement_tile,(cord[0],cord[1]))
                else:
                    del movement_tiles[:]

                if len(attack_tiles) > 0:
                    for tile in attack_tiles:
                        cord = getpixelcord(tile[0], tile[1])
                        screen.blit(attack_tile, (cord[0], cord[1]))
                else:
                    del attack_tiles[:]


                # ##DISPLAY CURRENT SELECTED SHIP AND INFO
                if ship_selected_img != None:
                    screen.blit(ship_selected_img, (850, 40))
                    for i in boat_active:
                        message_to_screen("HP: " + str(i.hp), black, 765, 20)
                        message_to_screen("DEF: " + str(i.defence), black, 765, 40)
                        message_to_screen("ATT: " + str(i.attack_range), black, 765, 60)
                        displaysurf.blit(textures[block], (770, 175)) ##SHIP CARD SLOTS
                        displaysurf.blit(textures[block], (805, 175))
                        displaysurf.blit(textures[block], (840, 175))
                        displaysurf.blit(textures[block], (875, 175))

                elif ship_selected_img == None:
                    message_to_screen("No ship selected", black, 770, 100)

                ##DRAW P1 INVENTORY ITEMS
                P1_box_x_pos = 620
                for i in P1_carddraw:
                    displaysurf.blit(i.img, (P1_box_x_pos, 275))
                    P1_box_x_pos += 40

                ##DRAW P1 INVENTORY ITEMS
                P2_box_x_pos = 620
                for i in P2_carddraw:
                    displaysurf.blit(i.img, (P2_box_x_pos, 375))
                    P2_box_x_pos += 40


                ##FILL P1 INVENTORY
                while len(P1_carddraw) < 7:
                    P1_carddraw += [random.choice(turndeck)]
                    print (len(P1_carddraw))
                    for card in P1_carddraw:
                        card = card.img
                        if len(P1_carddraw) > 7:
                            P1_inventory_full = True
                        else:
                            P1_inventory_full = False

                ##FILL P1 INVENTORY
                while len(P2_carddraw) < 7:
                    P2_carddraw += [random.choice(turndeck)]
                    print (len(P2_carddraw))
                    for card in P2_carddraw:
                        card = card.img
                        if len(P2_carddraw) > 7:
                            P2_inventory_full = True
                        else:
                            P2_inventory_full = False



                # start of screen writings
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                seconds -= roundtime
                seconds = int(seconds)
                if roundtime > 0:
                    message_to_screen(str(seconds), black, 630, 175)

                mousepos = pygame.mouse.get_pos()
                #######
                ## FPS COUNTER
                end_t = time.time()
                time_taken = end_t - start_t
                start_t = end_t
                frame_times.append(time_taken)
                frame_times = frame_times[-20:]
                fps_count = len(frame_times) / sum(frame_times)

                # ## DEBUGGING MESSAGES TO SCREEN
                # message_to_screen("Mouse Cords " + str(getmousepos()), black, 625, 210)
                # message_to_screen("total ships: " + str(P1_Boat1.total_boats), black, 625, 230)
                # message_to_screen("PLAYER1 ships: " + str(P1_boat_cords.length), red, 625, 250)
                # message_to_screen("PLAYER2 ships: " + str(P2_boat_cords.length), blue, 625, 270)
                message_to_screen("FPS: " + str(round(fps_count, 0)), black, 625, 450)

                message_to_screen("movement tiles:", black, 600, 480)
                message_to_screen(str(movement_tiles),black,600,510)



                pygame.display.flip()
    clock.tick(FPS)
    pygame.quit()

    game = Game()
    game()
mainloop()
### end mainloop

##check if mainloop has been paused
print (mainloop())






