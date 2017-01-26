import pygame, sys
pygame.init()
from Database import *

BLACK = (0,0,0)
WHITE = (255,255,255)

id = "1234567891"


def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

class Scoreitem:
    def __init__(self, name,score):
        self.font = pygame.font.Font(None, 40)
        self.score = score
        self.name = name

    def message_to_screen(self, msg, color, posx, posy):
        screen_text = self.font.render(msg, True, color)
        screen.blit(screen_text, [posx, posy])

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.items = []
        self.bg = BLACK
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height


        self.scorelist = Get_top()
        for row in self.scorelist:
            entity = Scoreitem(row[1],row[2])
            self.items.append(entity)


        # for item in id:
        #     # pos_x = (self.scr_width / 2) - (menu_item.width / 2)
        #     entity = Scoreitem("naam uit DB")
        #     self.items.append(entity)


    def run(self):
        mainloop = True
        score_items = 0
        pos_x = 350
        pos_y = 80
        self.screen.fill(self.bg)
        screen.blit(menu_bg, (0, 0))
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            for item in self.items:
                if score_items < len(self.items):
                    score_items += 1
                    pos_y += 35
                    item.message_to_screen(item.name + "   -   " + str(item.score), WHITE, pos_x, pos_y)

                    print(len(self.items))

            pygame.display.flip()


screen = pygame.display.set_mode((930, 580), 0, 32)
pygame.display.set_caption('Game Menu')
menu_bg = load_image('../images/battleship.jpg')
start = Scoreboard(screen)
#start.run()



