import pygame, sys

pygame.init()

# Globals
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT_COLOR = (255, 255, 255)

#pygame.mixer.init()
#pygame.mixer.music.load("../sounds/menu_music.wav")
#pygame.mixer.music.play(-1)

def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=6,
                 font_color=FONT_COLOR, pos_x=0, pos_y=0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.is_selected = False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def is_mouse_selection(self, posx, posy):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
                (posy >= self.pos_y and posy <= self.pos_y + self.height):
            return True
        return False


class GameMenu():
    def __init__(self, screen, items, bg_color=BLACK, font=None, font_size=30,
                 font_color=FONT_COLOR):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.font = pygame.font.Font(None, 30)
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, 25, FONT_COLOR)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)

            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None

            self.set_mouse_visibility()

            # Redraw the background
            self.screen.fill(self.bg_color)
            #screen.blit(menu_bg, (0, 0))

            for item in self.items:
                if self.mouse_is_visible:
                    mpos = pygame.mouse.get_pos()


                self.screen.blit(item.label, item.position)

            pygame.display.flip()

# Creating the screen
screen = pygame.display.set_mode((930, 580), 0, 32)
menu_bg = load_image('../images/battleship.jpg')
menu_items = ('Game instructions:','1. At the start of each game both players pick 2 cards from the normal card’s deck.',
              '2. At the start of each game both players place their four ships in turns on the game board.',
              '3. During a turn only one of the four ships may be moved.',
              '4. A ship can have either attack mode or defence mode.',
              '5. A ship that is in defence mode, gains +1 attack range.',
              '6. A ship can only attack when it gets into attack range from an enemy vessel.',
              '7. A ship that is in defence mode can only attack vertically and cannot move until it is put back into attack mode.',
              '8. A ship that is in attack mode can either attack vertically and horizontally but cannot attack diagonally.',
              '9. A ship that is in attack mode can only move one time each turn.',
              '10. At the start of each new turn the player draws a card from the normal deck.',
              '11. When a ship reaches opposite side of the game board, the player draws a card from the special deck.',
              '12. A trap card is placed face down on the game board, and can be activated at any time during the match.',
              '13. During each new turn the player can play a card before he attacks or moves a ship.',
              '14. When a ship is sunk it turns into a impassable object on the game board.',
              '15. The winning player receives 100 points for each sunken ship and points based on the match time.')
pygame.display.set_caption('Instruction menu')
gm = GameMenu(screen, menu_items)
