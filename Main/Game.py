import math
import time
import pygame,sys,random,os
from pygame.locals import *
from Database import *
from tkinter import *
import ctypes
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

recources = [water] #a list of recources
tilemap = [[water for w in range(mapwidth)] for h in range(mapheight)] #use list comprehension to create our tilemap
displaysurf = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))

#GAME SETUP
width = (mapwidth * tilesize) + (350)
height = (mapheight * tilesize)
menu = True
size = (width, height)
pygame.init()
pygame.display.set_caption("Battleport V.1.2.1")
screen = pygame.display.set_mode(size)
pygame.display.update()
font = pygame.font.Font(None, 24)

FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)

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
def mhello():
    text = ment.get
    mlabel2 = Label(mgui, text=text).pack()
    return

class card(pygame.sprite.Sprite):
    def __init__(self,name,rectx,recty,image,description):
        pygame.sprite.Sprite.__init__(self)
        self.posX = 0
        self.posY = 0
        self.name = name
        self.image = image
        self.width = 30
        self.height = 30
        self.rect = self.image.get_rect();
        self.rect.x = rectx
        self.rect.y = recty
        self.cord = [self.rect.x // tilesize, self.rect.y // tilesize]
        self.rect.center = self.rect.center
        self.pos = self.rect.x,self.rect.y
        self.description = description

    def setpos(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def resetpos(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y

    def setcord(self,x,y):
        self.rect.x = (x * tilesize)
        self.rect.y = (y * tilesize)
        self.cordhead = [self.rect.x // tilesize, self.rect.y // tilesize]

    def draw(self,screen,X,Y):
        screen.blit(self.image,(X,Y))

    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        self.rect.x = x
        self.rect.y = y
        self.cord = [self.rect.x // tilesize,self.rect.y // tilesize]


ADRENALINERUSH = card('ADRENALINERUSH',10,10,pygame.image.load(os.path.join("../images/adrenalinerush.png")),"One of your ships may move again.")
ADVANCEDRIFLING = card('ADVANCEDRIFLING',10,10,pygame.image.load(os.path.join("../images/advancedrifling.png")),"Attack range +2 (passive)")
ALUMINIUMHULL = card('ALUMINIUMHULL',10,10,pygame.image.load(os.path.join("../images/aluminiumhull.png")),"Ship may move twice per turn (passive)")
BACKUP = card('BACKUP',10,10,pygame.image.load(os.path.join("../images/backup.png")),"draw another card")
EMPUPGRADE = card('EMPUPGRADE',10,10,pygame.image.load(os.path.join("../images/empupgrade.png")),"Enemy player has to skip this turn")
EXTRAFUEL = card('EXTRAFUEL',10,10,pygame.image.load(os.path.join("../images/extrafuel.png")),"Ship may move 2 extra steps")
FARSIGHT = card('FARSIGHT',10,10,pygame.image.load(os.path.join("../images/farsight.png")),"Attack range +2 (passive)")
FLAKARMOR = card('FLAKARMOR',10,10,pygame.image.load(os.path.join("../images/flakarmor.png")),"Protection against mines (passive)")
FMJUPGRADE = card('FMJUPGRADE',10,10,pygame.image.load(os.path.join("../images/fmjupgrade.png")),"Attack damage +1 (passive)")
HEADSHOT = card('HEADSHOT',10,10,pygame.image.load(os.path.join("../images/headshot.png")),"Destroys boat in 1 hit")
JACKSPARROW = card('JACKSPARROW',10,10,pygame.image.load(os.path.join("../images/jacksparrow.png")),"Steal an opposite boat")
NAVALMINE = card('NAVALMINE',10,10,pygame.image.load(os.path.join("../images/navalmine.png")),"Place a mine on a coordinate")
RALLY = card('RALLY',10,10,pygame.image.load(os.path.join("../images/rally.png")),"All ships may use 1 extra step")
REINFORCEDHULL = card('REINFORCEDHULL',10,10,pygame.image.load(os.path.join("../images/reinforcedhull.png")),"Ship gets +1 armor")
REPAIR = card('REPAIR',10,10,pygame.image.load(os.path.join("../images/repair.png")),"Ship gets back to full health")
RIFLING = card('RIFLING',10,10,pygame.image.load(os.path.join("../images/rifling.png")),"Ship Attack range +1 (passive)")
SABOTAGE = card('SABOTAGE',10,10,pygame.image.load(os.path.join("../images/sabotage.png")),"A chosen ship attacks himself")
SMOKESCREEN = card('SMOKESCREEN',10,10,pygame.image.load(os.path.join("../images/smokescreen.png")),"A chosen ship cannot attack")
SONAR = card('SONAR',10,10,pygame.image.load(os.path.join("../images/sonar.png")),"Detect all mines")


turndeck = [FMJUPGRADE,FMJUPGRADE,RIFLING,RIFLING,ADVANCEDRIFLING,ADVANCEDRIFLING,NAVALMINE,NAVALMINE,NAVALMINE,
           NAVALMINE,NAVALMINE,NAVALMINE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,BACKUP,BACKUP,EXTRAFUEL,EXTRAFUEL,
           EXTRAFUEL,EXTRAFUEL,RALLY,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,REINFORCEDHULL,SONAR,
           REINFORCEDHULL,SONAR,SONAR,SONAR,SMOKESCREEN,SMOKESCREEN,SABOTAGE,SABOTAGE]

# specialdeck = [REPAIR,REPAIR,FLAKARMOR,FLAKARMOR,HEADSHOT,JACKSPARROW,FARSIGHT,ALUMINIUMHULL]


cardgroup = pygame.sprite.Group()
# cardgroup.add(turndeck)
cardgroup.add(FMJUPGRADE,FMJUPGRADE,RIFLING,RIFLING,ADVANCEDRIFLING,ADVANCEDRIFLING,NAVALMINE,NAVALMINE,NAVALMINE,
           NAVALMINE,NAVALMINE,NAVALMINE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,EMPUPGRADE,BACKUP,BACKUP,EXTRAFUEL,EXTRAFUEL,
           EXTRAFUEL,EXTRAFUEL,RALLY,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,ADRENALINERUSH,REINFORCEDHULL,SONAR,
           REINFORCEDHULL,SONAR,SONAR,SONAR,SMOKESCREEN,SMOKESCREEN,SABOTAGE,SABOTAGE)


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
        self.active = True

class Boat(pygame.sprite.Sprite):
    health = 100
    total_boats = 0
    def __init__(self,posXhead,posYhead,rectx,recty,length,image):
        pygame.sprite.Sprite.__init__(self)
        self.posX = posXhead
        self.posY = posYhead
        self.posXhead = (posXhead * tilesize)
        self.posYhead = (posYhead * tilesize)
        self.posXtail = (posXhead * tilesize)
        self.posYtail = posYhead + (length-1)
        self.length = length
        self.cordhead = [posXhead,posYhead]
        self.cordtail = [self.posXtail,self.posYtail]
        self.image = image
        self.rect = self.image.get_rect();  # here rect is created
        self.rect.x = self.posXhead
        self.rect.y = self.posYhead
        self.hp = Boat.health
        self.attack_range = 0
        self.defence = 0
        self.defencemode = False
        Boat.total_boats += 1

    def __del__(self):
        pass

    def attack(self):
        pass

    def getmovement(self,boatlength):
        tiles = []
        if boatlength == 1:
            tiles = [self.cordhead[0]+1,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]+1]

        if boatlength == 2:
            tiles = [self.cordhead[0]+1,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]+2],\
                    [self.cordhead[0]+1,self.cordhead[1]-(-1)],[self.cordhead[0]+(-1),self.cordhead[1]+1]

        if boatlength == 3:
            tiles = [self.cordhead[0]+1,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]+3], \
                    [self.cordhead[0]+1,self.cordhead[1]-(-1)],[self.cordhead[0]+(-1),self.cordhead[1]+1],[self.cordhead[0]+1,self.cordhead[1]-(-2)],[self.cordhead[0]+(-1),self.cordhead[1]+ 2]

        tile_count = 0
        for tile in tiles:
            tile_count += 1
            move_tile = create_tile(tile[0]*tilesize,tile[1]*tilesize,pygame.image.load(os.path.join("../images/movement_tile.png")))
            movement_tiles.add(move_tile)
            if tile_count == len(tiles):
                break


    def getattack(self,boatlength):
        tiles = []
        if boatlength == 1:
            tiles = [self.cordhead[0]+1,self.cordhead[1],[self.cordhead[0]+2,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],\
                    [self.cordhead[0]-2,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]-2], \
                    [self.cordhead[0], self.cordhead[1]+1], [self.cordhead[0], self.cordhead[1]+2]]

        if boatlength == 2:
            tiles = [self.cordhead[0]+1,self.cordhead[1]],[self.cordhead[0]+2,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],\
                    [self.cordhead[0]-2,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]-2], \
                    [self.cordhead[0],self.cordhead[1]+2],[self.cordhead[0], self.cordhead[1]+3],[self.cordhead[0]+1,self.cordhead[1]-(-1)],\
                    [self.cordhead[0]+(-1),self.cordhead[1]+1],[self.cordhead[0]+2,self.cordhead[1]-(-1)],[self.cordhead[0]+(-2),self.cordhead[1]+1]

        if boatlength == 3:
            tiles = [self.cordhead[0]+1,self.cordhead[1]],[self.cordhead[0]+2,self.cordhead[1]],[self.cordhead[0]-1,self.cordhead[1]],\
                    [self.cordhead[0]-2,self.cordhead[1]],[self.cordhead[0],self.cordhead[1]-1],[self.cordhead[0],self.cordhead[1]-2],\
                    [self.cordhead[0], self.cordhead[1]+3],[self.cordhead[0], self.cordhead[1]+4],[self.cordhead[0], self.cordhead[1]+3],\
                    [self.cordhead[0]+1,self.cordhead[1]-(-1)],[self.cordhead[0]+(-1),self.cordhead[1]+1],[self.cordhead[0]+2,self.cordhead[1]-(-1)],\
                    [self.cordhead[0]+(-2),self.cordhead[1]+1],[self.cordhead[0]+1,self.cordhead[1]-(-2)],[self.cordhead[0]+(-1),self.cordhead[1]+2],\
                    [self.cordhead[0]+2,self.cordhead[1]-(-2)],[self.cordhead[0]+(-2),self.cordhead[1]+2]

        tile_count = 0
        for tile in tiles:
            tile_count += 1
            att_tile = create_tile(tile[0]*tilesize,tile[1]*tilesize,pygame.image.load(os.path.join("../images/attack_tile.png")))
            attack_tiles.add(att_tile)
            if tile_count == len(tiles):
                break

    def draw(self, screen):
        screen.blit(self.image, (self.posXhead,self.posYhead))

    def set_position(self,X,Y):
        self.cordhead = [self.posX + X, self.posY + Y]
        self.posXhead = (X * tilesize)
        self.posYhead = (Y * tilesize)
        # self.cordhead = [self.posXhead // tilesize, self.posYhead // tilesize]
        self.rect.x = (X * tilesize)
        self.rect.y = (Y * tilesize)

    def add_position(self,X,Y):
        self.posXhead = (posXhead + X * tilesize)
        self.posYhead = (posYhead + Y * tilesize)
        self.cordhead = [self.posXhead+X,self.posYhead+Y]

    def set_cord(self,X,Y):
        # self.cordhead[0] = self.cordhead[0] + X
        # self.cordhead[1] = self.cordhead[1] + Y
        # self.posXhead = self.posXhead + (X * tilesize)
        # self.posYhead = self.posYhead + (Y * tilesize)
        # self.cordtail = self.cordtail + X,Y
        self.posXhead = (self.posXhead + (X * tilesize))
        self.posYhead = (self.posYhead + (Y * tilesize))
        self.rect.x = self.rect.x + (X * tilesize)
        self.rect.y = self.rect.y + (Y * tilesize)
        print ("rectx: ",self.rect.x)
        print ("recty: ",self.rect.y)

    def rotate(self,angle):
        self.image = pygame.transform.rotate(self.image, angle)
        return self.image

    def get_cord_to_posX(self,cord):
        return cord[0]

    def get_cord_to_posY(self,cord):
        return cord[1]


#CREATE BOATS
P1_Boat1 = Boat(3,18,30,30,1,pygame.image.load(os.path.join('../images/P1_ship_small.png')).convert_alpha())
P1_Boat2 = Boat(6,17,30,60,2,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat3 = Boat(10,18,30,60,2,pygame.image.load(os.path.join('../images/P1_ship_med.png')).convert_alpha())
P1_Boat4 = Boat(16,13,30,90,3,pygame.image.load(os.path.join('../images/P1_ship_large.png')).convert_alpha())
# #
P2_Boat1 = Boat(13,3,30,30,1,pygame.image.load(os.path.join('../images/P2_ship_small.png')).convert_alpha())
P2_Boat2 = Boat(11,2,30,60,2,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat3 = Boat(15,13,30,60,2,pygame.image.load(os.path.join('../images/P2_ship_med.png')).convert_alpha())
P2_Boat4 = Boat(6,4,30,90,3,pygame.image.load(os.path.join('../images/P2_ship_large.png')).convert_alpha())

P1_boat_group = pygame.sprite.Group()
P2_boat_group = pygame.sprite.Group()
# P1_boat_group = pygame.sprite.OrderedUpdates()
# P2_boat_group = pygame.sprite.OrderedUpdates()

P1_boat_group.add(P1_Boat1,P1_Boat2,P1_Boat3,P1_Boat4)
P2_boat_group.add(P2_Boat1,P2_Boat2,P2_Boat3,P2_Boat4)

# P1_boatsprite1 = P1_boat_group.sprites()[0]
# P1_boatsprite2 = P1_boat_group.sprites()[1]
# P1_boatsprite3 = P1_boat_group.sprites()[2]
# P1_boatsprite4 = P1_boat_group.sprites()[3]



class sprite(pygame.sprite.Sprite):
    def __init__(self,name,image,rectx,recty,width,height):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.width = width
        self.orig_posx = rectx
        self.orig_posy = recty
        self.height = height
        self.rect = self.image.get_rect(); #here rect is created
        self.rect.x = rectx
        self.rect.y = recty

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_sprite(self):
        print ("updating pos")
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        self.rect.x = x
        self.rect.y = y

    def resetpos(self):
        self.rect.x = self.orig_posx
        self.rect.y = self.orig_posy

## Sprite GROUPS
movement_up = sprite('movement_up',pygame.image.load(os.path.join('../images/movement_up.png')).convert_alpha(),660,20,30,30)
movement_left = sprite('movement_left',pygame.image.load(os.path.join('../images/movement_left.png')).convert_alpha(),625,55,30,30)
movement_right = sprite('movement_right',pygame.image.load(os.path.join('../images/movement_right.png')).convert_alpha(),695,55,30,30)
movement_down = sprite('movement_down',pygame.image.load(os.path.join('../images/movement_down.png')).convert_alpha(),660,90,30,30)
movement_leftturn = sprite('movement_leftturn',pygame.image.load(os.path.join('../images/movement_leftturn.png')).convert_alpha(),620,20,30,30)
movement_rightturn = sprite('movement_rightturn',pygame.image.load(os.path.join('../images/movement_rightturn.png')).convert_alpha(),705,20,30,30)
attack_button = sprite('attack_button',pygame.image.load(os.path.join('../images/ui_attack.png')).convert_alpha(),610,135,60,20)
defend_button = sprite('defend_button',pygame.image.load(os.path.join('../images/ui_defend.png')).convert_alpha(),685,135,60,20)
end_button = sprite('end_button',pygame.image.load(os.path.join('../images/ui_end.png')).convert_alpha(),650,170,80,30)

UI_sprites = pygame.sprite.Group() ## MOVEMENT INTERFACE
UI_sprites.add(movement_up,movement_left,movement_right,movement_down,movement_leftturn,movement_rightturn,end_button,attack_button,defend_button)

attack_tiles = pygame.sprite.Group()
movement_tiles = pygame.sprite.Group()

## TESTING DRAG WITH MOUSE SPRITES
dragtest1 = sprite('dragtest1',pygame.image.load(os.path.join('../images/jacksparrow.png')).convert_alpha(),780,500,30,30)
dragtest2 = sprite('dragtest2',pygame.image.load(os.path.join('../images/jacksparrow.png')).convert_alpha(),820,500,30,30)
dragtest = pygame.sprite.Group()
dragtest.add(dragtest1,dragtest2)

##CREATE DIFFERENT TILES
movement_tile = pygame.image.load(os.path.join("../images/movement_tile.png"))
attack_tile = pygame.image.load(os.path.join("../images/attack_tile.png"))
attack_curser = pygame.image.load(os.path.join("../images/attackmarker_tile.png"))

ship_selected_bg = pygame.image.load(os.path.join("../images/ship_selected_bg.png"))
inventory_bg = pygame.image.load(os.path.join("../images/inventory_bg.png"))

event_bg = pygame.image.load(os.path.join("../images/event_bg.png"))
event_log = pygame.image.load(os.path.join("../images/evlog.png"))


class create_tile(pygame.sprite.Sprite):
    def __init__(self,cordx,cordy,image):
        pygame.sprite.Sprite.__init__(self)
        self.cord = cordx,cordy
        self.image = image
        self.rect = self.image.get_rect();
        self.rect.x = cordx
        self.rect.y = cordy

    def setcord(self,X,Y):
        self.cord = X,Y

    def delete(self,group):
        for tiles in group:
            tiles.kill()  # removes from group
            # del tiles
def new_game_db(nameone,nametwo):
    insert_new_score(nameone,0)
    insert_new_score(nametwo,0)


def mainloop(nameone, nametwo):
    new_game_db(nameone,nametwo)
    player_select = Player()
    ship_selected_img = None
    attack_mode = False
    tiles_render = False
    gameExit = False
    mousemotion = False
    card_selected = False
    boat_active = []


    button_pressed = ''

    P1_inventory_full = False
    P2_inventory_full = False

    P1_carddraw = pygame.sprite.Group()
    P2_carddraw = pygame.sprite.Group()
    P1_drawn = False
    P1_card_count = 0

    hover_on = None
    hover_card = None
    description_card = None
    clicked = False

    ##ROUND counter
    roundtime = 30
    start_ticks = pygame.time.get_ticks()  # starter tick
    # if grid == False:

    ##CREATE GRID ON STARTUP (NEW WAY OF RENDERING)
    # for rw in range(mapheight):
    #     for cl in range(mapwidth):
    #         tilemap[rw][cl] = water
    #         screen.fill(white)
    #         print ("updating grid")
    #
    #     for row in range(mapheight):
    #         for column in range(mapwidth): ##DRAW GRID
    #             displaysurf.blit(textures[tilemap[row][column]], (column * tilesize, row * tilesize))

    while not gameExit:

        grid = False

        ## FPS counter
        frame_times = []
        start_t = time.time()

        for event in pygame.event.get(): ##STATE CHECKER
            if event.type == pygame.QUIT:
                quitgame()
                gameExit = True

            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                for tile in attack_tiles:
                    if tile.rect.collidepoint(x,y):
                        print ("hovering on attack tile")

                        tile.image = attack_curser
                    else:
                        tile.image = attack_tile

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return "pause"
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                for sprite in P1_carddraw:
                    if sprite.rect.collidepoint(x,y):
                       hover_card = sprite.name
                       description_card = sprite.description
                    else:
                        hover_card_card = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = getmousepos()
                x,y = event.pos
                clicked = True
                if hover_card:
                    # hover_card = None
                    movecard(hover_card)
                elif hover_card != None:
                    card_selected = True
                    selectcard(hover_card)
                for sprite in UI_sprites:
                    if sprite.rect.collidepoint(x,y):
                        button_pressed = sprite.name
                        controller(button_pressed)
                        break
                for card in P1_carddraw:
                    if card.rect.collidepoint(x,y):
                        hover_card = card

                for tile in attack_tiles:
                    if boat_active in P1_boat_group:
                        if tile.rect.collidepoint(x, y):
                            for boat in P2_boat_group:
                                # print ("tile rectx pressed: ",tile.rect.x)
                                # print("tile recty pressed: ", tile.rect.y)
                                # print ("P2 boat cordx: ",boat.rect.x)
                                # print("P2 boat cordx: ", boat.rect.y)
                                print(boat.rect[0],boat.rect[1]+tilesize)
                                print(tile.rect.x,tile.rect.y)
                                if (tile.rect.x,tile.rect.y) == (boat.rect[0],boat.rect[1]):
                                    print ("p2 boat hit")
                                    boat.hp -= 10
                                elif(tile.rect.x,tile.rect.y) == (boat.rect[0],boat.rect[1]+tilesize):
                                    print("p2 boat hit")
                                    boat.hp -= 10
                                elif (tile.rect.x,tile.rect.y) == (boat.rect[0],boat.rect[1]+(tilesize*2)):
                                    print("p2 boat hit")
                                    boat.hp -= 10

                    if boat_active in P2_boat_group:
                        if tile.rect.collidepoint(x, y):
                            for boat in P1_boat_group:
                                if (tile.rect.x, tile.rect.y) == (boat.rect[0], boat.rect[1]):
                                        print("p1 boat hit")
                                        boat.hp -= 10

                if not boat_active and ship_selected_img != None:
                    boat_active = selectedboat()
                elif not boat_active:
                    boat_active = selectedboat()
                else:
                    moveboat()

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False

        ## DEBUGGING LOOP PRINTS
        # print (held)
        # print ("hovercard: ",hover_card)
        # print ("attack tiles: ",attack_tiles)
        # print (P1_Boat1.posXhead)
        # print (P1_Boat1.posYhead)
        # print (P1_Boat1.cordhead)
        # print (attack_tiles)

        def switch():
            global turn
            if (turn == True):
                print("player 2's turn.")
                ctypes.windll.user32.MessageBoxW(0, "Turn player 1", "turn-notification", 1)
                player_select.active = False
                turn = False
            else:
                print("player 1's turn")
                ctypes.windll.user32.MessageBoxW(0, "Turn player 2", "turn-notification", 1)
                player_select.active = True
                turn = True

        def controller(button):
            mousecord = getmousepos()
            if button == 'end_button':
                movement_tiles.empty()
                attack_tiles.empty()
                boat_active.clear()
                switch()
            if boat_active and movement_tiles:
                for boat in boat_active:
                    if button == 'movement_up':
                        #pos = get(boat.cordhead[0],boat.cordhead[1]+tilesize)

                        boat.set_cord(0,-1)
                        # boat.set_position(pos[0],pos[1]+1)
                        # print("x : "+str(boat.cordhead[1]))
                    elif button == 'movement_down':
                        boat.set_cord(0,1)
                    elif button == 'movement_left':
                        boat.set_cord(-1,0)
                    elif button == 'movement_right':
                        boat.set_cord(1,0)
                    elif button == 'movement_leftturn':
                        boat.rotate(90)
                    elif button == 'movement_rightturn':
                        boat.rotate(-90)
                    elif button == 'attack_button':
                        print ("attack pressed")
                        attackmode()
                    elif button == 'defend_button':
                        print("defend pressed")
                        defendmode()
                movement_tiles.empty()


        def movecard(card):
            global hover_card
            mousecord = getmousepos()
            x,y = event.pos
            if card.name == 'NAVALMINE':
                if mousecord[0] > mapwidth - 1 or mousecord[0] < 0 or mousecord[1] > mapheight - 1 or mousecord[1] < 0:
                    card.resetpos()
                else:
                    card.setcord(mousecord[0], mousecord[1])
            else:
                  card.setpos(x,y)
            hover_card = None



        def selectedboat():
            global ship_selected_img
            ship_selected = False  ## check if ship is selected within this function
            x, y = event.pos
            for boat in P1_boat_group:
                if (player_select.active == True):
                    if boat.rect.collidepoint(x, y):
                        ship_selected = True
                        print ("P1 boat selected")
                        new_boat = [boat]
                        return new_boat
            for boat in P2_boat_group:
                if (player_select.active == False):
                    if boat.rect.collidepoint(x, y):
                        ship_selected = True
                        print ("P2 boat selected")
                        new_boat = [boat]
                        return new_boat
            if not ship_selected:
                movement_tiles.empty()
                attack_tiles.empty()
                ship_selected_img = None
                return []


        if boat_active: ## if there is a ship selected.  give the img variable, the sprite of this ship (for render)
            while not tiles_render:
                for boat in boat_active:
                    ship_selected_img = boat.image
                    boatcord = boat.cordhead
                    boat.getmovement(boat.length)
                    tiles_render = True
                    if boat.length == 1:
                        boat.getmovement(1)
                    if boat.length == 2:
                        boat.getmovement(2)
                    if boat.length == 3:
                        boat.getmovement(3)
        if not boat_active:
            ship_selected_img = None
            tiles_render = False



        def moveboat():  ## move fixed boat to the mouse cords
            global ship_selected_img
            global attack_mode
            global tiles_render
            x,y = event.pos
            mousecord = getmousepos()
            print (mousecord[0])
            print (mousecord[1])
            for boat in boat_active:
                if not boat.defencemode:
                    for tile in movement_tiles:
                        if tile.rect.collidepoint(x,y):
                            print ("clicked on movement tile")
                            boat.set_position(mousecord[0], mousecord[1])
                        else:
                            pass
                    if mousecord[0] > mapwidth-1 or mousecord[0] < 0:
                        break
                    elif mousecord[1] > mapheight-1 or mousecord[1] < 0:
                        break
                    elif mousecord != boat.cordhead or mousecord not in movement_tiles:
                        ship_selected_img = None
                        boat_active.clear()
                        movement_tiles.empty()
                        attack_tiles.empty()
                        tiles_render = False
                        break
                movement_tiles.empty()


        def attackmode():
            movement_tiles.empty()
            print ("doing attack mode")
            for boat in boat_active:
                boatcord = boat.cordhead #SHOW AVAILABLE ATTACK TILES
                boat.getattack(boat.length)
                if boat.length == 1:
                    boat.getattack(1)
                elif boat.length == 2:
                    boat.getattack(2)
                elif boat.length == 3:
                    boat.getattack(3)

        def get_score_one():
            score = 0
            return score
        def get_score_two():
            score = 0
            return score

        def win_state(name, score, nametwo, scoretwo):
            print("something")
            if(score > scoretwo):
                winname = name
                winscore = score
            else:
                winname = nametwo
                winscore = scoretwo
            ctypes.windll.user32.MessageBoxW(0, "Player "+str(winname)+" wins with "+str(winscore)+" points", "You win", 1)

            update_score(name, score)
            update_score(nametwo, scoretwo)
            return "Main menu"

        def defendmode():
            movement_tiles.empty()
            for boat in boat_active:
                boatcord = boat.cordhead
                if boat.defencemode:
                    boat.rotate(+90)
                    boat.attack_range -= 3
                    boat.defencemode = False
                else:
                    boat.rotate(-90)
                    boat.attack_range += 3
                    boat.defencemode = True

        ##DRAW GRID
        if grid == False:
            for rw in range(mapheight):
                for cl in range(mapwidth):
                    tile = water
                    tilemap[rw][cl] = tile
                    screen.fill(white)

                for row in range(mapheight):
                    for column in range(mapwidth):  ##DRAW GRID
                        displaysurf.blit(textures[tilemap[row][column]], (column * tilesize, row * tilesize))
                # blit the boats at the correct position on the grid





                for boat in P1_boat_group:
                    boat.draw(screen)

                for boat in P2_boat_group:
                    boat.draw(screen)

                    # displaysurf.blit(P1_boatsprite1.image, (P1_boatsprite1.cordhead[0] * tilesize, P1_boatsprite1.cordhead[1] * tilesize))
                    # displaysurf.blit(P1_boatsprite2.image, (P1_boatsprite2.cordhead[0] * tilesize, P1_boatsprite2.cordhead[1] * tilesize))
                    # displaysurf.blit(P1_Boat4.image, (P1_Boat4.cordhead[0] * tilesize, P1_Boat4.cordhead[1] * tilesize))
                    # displaysurf.blit(P1_Boat2.image, (P1_Boat2.cordhead[0] * tilesize, P1_Boat2.cordhead[1] * tilesize))
                    # displaysurf.blit(P1_Boat3.image, (P1_Boat3.cordhead[0] * tilesize, P1_Boat3.cordhead[1] * tilesize))
                    # displaysurf.blit(P1_Boat4.image, (P1_Boat4.cordhead[0] * tilesize, P1_Boat4.cordhead[1] * tilesize))
                    #
                    # displaysurf.blit(P2_Boat1.image, (P2_Boat1.cordhead[0] * tilesize, P2_Boat1.cordhead[1] * tilesize))
                    # displaysurf.blit(P2_Boat2.image, (P2_Boat2.cordhead[0] * tilesize, P2_Boat2.cordhead[1] * tilesize))
                    # displaysurf.blit(P2_Boat3.image, (P2_Boat3.cordhead[0] * tilesize, P2_Boat3.cordhead[1] * tilesize))
                    # displaysurf.blit(P2_Boat4.image, (P2_Boat4.cordhead[0] * tilesize, P2_Boat4.cordhead[1] * tilesize))



                    # P1_boat_group.draw(screen)


                    ###DRAW INTERFACE ELEMENTS
                    # boat_bg = pygame.draw.rect(screen, red, [550, 600, 20, 20])
                displaysurf.blit(ship_selected_bg, (600, 10))
                displaysurf.blit(inventory_bg, (600, 225))
                displaysurf.blit(event_bg, (600, 440))
                displaysurf.blit(event_log, (610, 450))

                ##DRAW CARD SLOTS (PLAYER1)
                message_to_screen(nameone+": "+str(get_score_one()), red, 620, 250)
                displaysurf.blit(textures[block], (620, 275))
                displaysurf.blit(textures[block], (660, 275))
                displaysurf.blit(textures[block], (700, 275))
                displaysurf.blit(textures[block], (740, 275))
                displaysurf.blit(textures[block], (780, 275))
                displaysurf.blit(textures[block], (820, 275))
                displaysurf.blit(textures[block], (860, 275))

                ##DRAW CARD SLOTS (PLAYER2)
                message_to_screen(nametwo+": "+str(get_score_two()), blue, 620, 350)
                displaysurf.blit(textures[block], (620, 375))
                displaysurf.blit(textures[block], (660, 375))
                displaysurf.blit(textures[block], (700, 375))
                displaysurf.blit(textures[block], (740, 375))
                displaysurf.blit(textures[block], (780, 375))
                displaysurf.blit(textures[block], (820, 375))
                displaysurf.blit(textures[block], (860, 375))

                # SPRITES experimental code
                UI_sprites.draw(screen)

                ## TESTING DRAG WITH MOUSE SPRITES
                dragtest.draw(screen)

                ## DRAW ACTIVE STUFF NEEDS REWORK (ALL DRAW STUFF)
                if len(movement_tiles) > 0:
                    movement_tiles.draw(screen)
                else:
                    movement_tiles.empty()


                ##DRAW ATTACK TILES IF ACTIVE
                if len(attack_tiles) > 0:
                    attack_tiles.draw(screen)
                else:
                    attack_tiles.empty()



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




                # ##DRAW P2 INVENTORY ITEMS
                # P2_box_x_pos = 620
                # for i in P2_carddraw:
                #     displaysurf.blit(i.image, (P2_box_x_pos, 375))
                #     P2_box_x_pos += 40


                ##FILL P1 INVENTORY
                while not P1_inventory_full:
                    P1_carddraw.add(random.choice(turndeck))
                    print (len(P1_carddraw))
                    if len(P1_carddraw) >= 7:
                        P1_inventory_full = True
                    else:
                        P1_inventory_full = False


                # ##FILL P2 INVENTORY
                while not P2_inventory_full:
                    P2_carddraw.add(random.choice(turndeck))
                    print (len(P2_carddraw))
                    if len(P2_carddraw) >= 7:
                        P2_inventory_full = True
                    else:
                        P2_inventory_full = False


                ##DRAW P1 INVENTORY ITEMS
                P1_cardslot_posX = 620
                # for i in P1_carddraw:
                if P1_drawn == False:
                    print ("drawing cards")
                    for card in P1_carddraw:
                        P1_card_count += 1
                        card.rect.x = P1_cardslot_posX
                        card.rect.y = 275
                        card.draw(screen, P1_cardslot_posX, 275)
                        P1_cardslot_posX += 40
                        if P1_card_count == len(P1_carddraw):
                            P1_drawn = True


                P1_carddraw.draw(screen)
                # start of screen writings
                # seconds = (pygame.time.get_ticks() - start_ticks) / 200  # calculate how many seconds
                # seconds -= roundtime
                # seconds = int(seconds)
                # if seconds >= 0:
                #     seconds -= roundtime #does not put orginal seconds to -30 needs fix!!!!
                #     # print(seconds)
                #
                #     switch()
                #
                # if roundtime > 0:
                #      message_to_screen(str(seconds), black, 630, 180)

                mousepos = pygame.mouse.get_pos()

                end_t = time.time()
                time_taken = end_t - start_t
                start_t = end_t
                frame_times.append(time_taken)
                frame_times = frame_times[-20:]
                fps_count = len(frame_times) / sum(frame_times)

                #######
                ## FPS COUNTER
                ## DEBUGGING MESSAGES TO SCREEN
                message_to_screen("FPS: " + str(round(fps_count, 0)), black, 625, 450)
                message_to_screen("movement tiles:", black, 600, 480)
                message_to_screen(str(movement_tiles),black,600,510)

                print (description_card)
                message_to_screen(str(description_card), black, 620, 460)

                pygame.display.flip()



    clock.tick(FPS)
    pygame.quit()
    game = Game()
    game()

mgui = Tk()
ment = StringVar

# mgui.geometry('170x220+500+300')
# mgui.title('test')
# mlabel = Label(mgui, text='Player 1 name').pack()
# mEntry = Entry(mgui,textvariable=ment).pack()
# #mlabel = Label(mgui, text='Player 2 name').pack()
# #mEntry = Entry(mgui,textvariable=ment).pack()
# mbutton = Button(mgui,text = 'start', command = mhello, fg= 'black',bg = 'white').pack()
# mgui.mainloop()
#
turn = True
# mainloop()
# ### end mainloop
#
# ##check if mainloop has been paused
# print (mainloop())

