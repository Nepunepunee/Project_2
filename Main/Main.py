import math
import pygame,sys,random,os
from Database import *
pygame.init()
from pygame.locals import *





##colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)


def quitgame():
    pygame.quit()
    quit()

def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

# message drawer
# def message_to_screen(msg,color,posx,posy):
#     screen_text = font.render(msg, True, color)
#     screen.blit(screen_text, [posx,posy])

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

#constrants representing the different resources




class Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.menu = True
        size = (self.width, self.height)
        self.pause = True

        # Start PyGame
        pygame.init()

        # Program caption
        pygame.display.set_caption("Battleport V.0.0.1")
        
        # Set the resolution
        self.screen = pygame.display.set_mode(size)

        # Set up the default font
        self.font = pygame.font.Font(None, 30)

        #Set up FPS
        FPS = 60
        clock = pygame.time.Clock()
        clock.tick(FPS)

        pygame.mixer.init()
        pygame.mixer.music.load("../sounds/main.wav")
        pygame.mixer.music.play(-1)

        self.WATER = 2

        # a dictionary linkin recources to textures
        self.textures = {
            self.WATER: pygame.image.load(os.path.join('../images/wave.png'))
        }

        # useful game dimensions
        self.TILESIZE = 40
        self.MAPWIDTH = 20
        self.MAPHEIGHT = 20

        # a list of recources
        recources = [self.WATER]
        # use list comprehension to create our tilemap
        self.tilemap = [[self.WATER for w in range(self.MAPWIDTH)] for h in range(self.MAPHEIGHT)]

        self.DISPLAYSURF = pygame.display.set_mode((self.MAPWIDTH * self.TILESIZE, self.MAPHEIGHT * self.TILESIZE))

        #
        # the player image
        # pygame.draw.rect(screen,red,(player1Pos[0],player1Pos[1],30,30))

        self.player1Pos = [0, 0]
        self.player1 = pygame.image.load(os.path.join('../images/player1.png')).convert_alpha()

        # pygame.draw.rect(screen, blue, (player2Pos[0],player2Pos[1], 30, 30))
        self.player2 = pygame.image.load(os.path.join('../images/player2.png')).convert_alpha()
        self.player2Pos = [1, 0]

        # the position of the player [x,y]


        # PLAYER2 =
        # playerPos2 =[1,0]

    def quitgame(self):
        pygame.quit()
        quit()

    def draw_settings(self):
        self.screen.fill((red))
        menu_bg = load_image('../images/main_menu.png')
        self.screen.blit(menu_bg, (120, 0))

    # Draw menu
    def draw_menu(self):

        # Clear the screen
        self.screen.fill((blue))
        #load menu img
        menu_bg = load_image('../images/main_menu.png')
        self.screen.blit(menu_bg, (120, 0))
        #add buttons
        self.button(load_image('../images/menu_play_hover.png'),load_image('../images/menu_play.png'),220,175)
        self.button(load_image('../images/menu_quit_hover.png'), load_image('../images/menu_quit.png'), 220, 280)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if(self.pause):
                self.sub_menu()
                self.pause = False
            else:
                self.screen.fill((red))
                pygame.display.flip()
                self.pause = True

        # Flip the screen

        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # Clear the screen
            self.screen.fill((blue))
            #load menu img
            menu_bg = load_image('../images/main_menu.png')
            self.screen.blit(menu_bg, (120, 0))
            #add buttons
            self.button(load_image('../images/menu_quit_hover.png'), load_image('../images/menu_quit.png'), 250, 375,
                        self.quitgame)

            self.button(load_image('../images/menu_highscore_hover.png'), load_image('../images/menu_highscore.png'), 250,225,
            self.highscores)

            self.button(load_image('../images/menu_settings_hover.png'),load_image('../images/menu_settings.png'), 250, 300,
            self.settings_menu)

            self.button(load_image('../images/menu_play_hover.png'),load_image('../images/menu_play.png'),250,150,
            self.match_start)


            # Flip the screen
            pygame.display.flip()
    #draw ingame menu
    def sub_menu(self):
        self.screen.fill((255,255,255))
        menu_settings = load_image('../images/pause_menu.png')
        self.screen.blit(menu_settings, (120, 0))
        #self.button(load_image('../images/menu_quit_hover.png'), load_image('../images/menu_quit.png'), 250, 375,self.quitgame)
        pygame.display.flip()
    # Game match
    def match_start(self):
        self.menu = False
<<<<<<< HEAD
        self.screen.fill((red))
        pygame.display.update()
=======


        gameExit = False

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
                    if (event.key == K_RIGHT) and self.player1Pos[0] < self.MAPWIDTH - 1:
                        # change player's x position
                        self.player1Pos[0] += 1
                    if (event.key == K_LEFT) and self.player1Pos[0] > self.MAPWIDTH - self.MAPWIDTH:
                        # change player's x position
                        self.player1Pos[0] -= 1
                    if (event.key == K_UP) and self.player1Pos[1] > self.MAPHEIGHT - self.MAPHEIGHT:
                        # change player's y position
                        self.player1Pos[1] -= 1
                    if (event.key == K_DOWN) and self.player1Pos[1] < self.MAPHEIGHT - 1:
                        # change player's y position
                        self.player1Pos[1] += 1
                    # if right arrow is pressed

                    if (event.key == K_d) and self.player2Pos[0] < self.MAPWIDTH - 1:
                        # change player's x position
                        self.player2Pos[0] += 1
                    if (event.key == K_a) and self.player2Pos[0] > self.MAPWIDTH - self.MAPWIDTH:
                        # change player's x position
                        self.player2Pos[0] -= 1
                    if (event.key == K_w) and self.player2Pos[1] > self.MAPHEIGHT - self.MAPHEIGHT:
                        # change player's y position
                        self.player2Pos[1] -= 1
                    if (event.key == K_s) and self.player2Pos[1] < self.MAPHEIGHT - 1:
                        # change player's y position
                        self.player2Pos[1] += 1

                        ##ERROR
            # loop through each row
            for rw in range(self.MAPHEIGHT):
                for cl in range(self.MAPWIDTH):
                    randomnumber = random.randint(0, 15)
                    if randomnumber >= 1 or randomnumber <= 10:
                        tile = self.WATER

                    self.tilemap[rw][cl] = tile

                for row in range(self.MAPHEIGHT):
                    for column in range(self.MAPWIDTH):
                        # draw the resource at that position in the tilemap, using the correct image
                        self.DISPLAYSURF.blit(self.textures[self.tilemap[row][column]], (column * self.TILESIZE, row * self.TILESIZE))
                # display the player at the correct position
                self.DISPLAYSURF.blit(self.player1, (self.player1Pos[0] * self.TILESIZE, self.player1Pos[1] * self.TILESIZE))
                self.DISPLAYSURF.blit(self.player2, (self.player2Pos[0] * self.TILESIZE, self.player2Pos[1] * self.TILESIZE))

                # screen writings
                mousepos = pygame.mouse.get_pos()
                # message_to_screen(str(mousepos), red, 500, 15)
                # message_to_screen("player ships: " + str(player1.ships), red,10,10)
                # message_to_screen("player ships: " + str(player2.ships), blue, 200, 10)
                # message_to_screen("HP: " + str(player1.hp), red, 10, 30)
                # message_to_screen("HP: " + str(player2.hp), blue, 200, 30)


                pygame.display.update()

        # self.clock.tick(FPS)
        pygame.quit()

    match_start




>>>>>>> origin/master

    # button function
    def button(self,img_a,img_i,x,y,action=None):
        # buttons are 200x75
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+200 > mouse[0] > x and y+75 > mouse[1] >y:
            self.screen.blit(img_a, (x, y))
            if click[0] == 1 and action != None:
                action()

        else:
            self.screen.blit(img_i, (x, y))

    #message drawer
    def message_to_screen(self,msg, color):
        screen_text = self.font.render(msg, True, color)
        self.screen.blit(screen_text, [self.width / 2, self.height / 2])

    # The menu loop
    def game_menu(self):
        while not process_events():
            self.draw_menu()


    # The game loop
    def game_loop(self):
        while not process_events():
            self.match_start()



### settings menu
    def settings_menu(self):
        self.menu = False
        self.screen.fill((blue))
        menu_settings = load_image('../images/settings_menu.png')
        self.screen.blit(menu_settings, (120, 0))

        # volume mixer
        volume = pygame.mixer.music.get_volume()



        pygame.display.update()

    ### settings menu
    def highscores(self):
        self.menu = False
        self.screen.fill((blue))
        menu_settings = load_image('../images/highscores_menu.png')
        self.screen.blit(menu_settings, (120, 0))

        pygame.display.flip()


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
    game.game_menu()
    game.game_loop()


# Start the program
program()
