import pygame, sys
from Database import *

pygame.init()

# Globals
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT_COLOR = (0, 0, 100)


pygame.mixer.init()
# pygame.mixer.music.load("../sounds/menu_music.wav")
# pygame.mixer.music.play(-1)

def load_image(filename: str) -> pygame.Surface:
    surface = pygame.image.load(filename).convert()
    return surface

class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=10,
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
        self.font = pygame.font.Font(None, 22)
        self.screen_text = self.font.render("", True, WHITE)

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, 38, FONT_COLOR)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = 25
            pos_y = 25

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def set_item_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(FONT_COLOR)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                            self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                            self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                            self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                            self.cur_item == len(self.items) - 1:
                self.cur_item = 0

        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(BLUE)

        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            mainloop = False
            self.funcs[text]()

    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos[0],mpos[1]):
            item.set_font_color(BLUE)
            item.set_italic(True)
        else:
            item.set_font_color(FONT_COLOR)
            item.set_italic(False)

    def message_to_screen(self, msg, color, posx, posy):
        self.screen_text = self.font.render(msg, True, color)
        screen.blit(self.screen_text, [posx, posy])

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_item_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos[0], mpos[1]):
                            return item.text

            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None

            self.set_mouse_visibility()

            # Redraw the background
            self.screen.fill(self.bg_color)
            screen.blit(menu_bg, (0, 0))

            for item in self.items:
                if self.mouse_is_visible:
                    mpos = pygame.mouse.get_pos()
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)

            self.message_to_screen("1. At the start of each game both players pick 2 cards from the normal card’s deck.", WHITE, 100, 70)
            self.message_to_screen("2. At the start of each game both players place their four ships in turns on the game board.",WHITE, 100, 100)
            self.message_to_screen("3. During a turn only one of the four ships may be moved.", WHITE, 100, 130)
            self.message_to_screen("4. A ship can have either attack mode or defence mode.",WHITE, 100, 160)
            self.message_to_screen("5. A ship that is in defence mode, gains +1 attack range.", WHITE, 100, 190)
            self.message_to_screen("6. A ship can only attack when it gets into attack range from an enemy vessel.", WHITE, 100, 220)
            self.message_to_screen("7. A ship that is in defence mode can only attack vertically and cannot move until it is put back into attack mode.", WHITE, 100, 250)
            self.message_to_screen("8. A ship that is in attack mode can either attack vertically and horizontally but cannot attack diagonally.", WHITE, 100, 280)
            self.message_to_screen("9. A ship that is in attack mode can only move one time each turn.", WHITE, 100, 310)
            self.message_to_screen("10. At the start of each new turn the player draws a card from the normal deck.", WHITE, 100, 340)
            self.message_to_screen("11. When a ship reaches opposite side of the game board, the player draws a card from the special deck.", WHITE, 100, 370)
            self.message_to_screen("12. A trap card is placed face down on the game board, and can be activated at any time during the match.", WHITE, 100, 400)
            self.message_to_screen("13. During each new turn the player can play a card before he attacks or moves a ship.", WHITE, 100, 430)
            self.message_to_screen("14. When a ship is sunk it turns into a impassable object on the game board.", WHITE, 100, 460)
            self.message_to_screen("15. The winning player receives 100 points for each sunken ship and points based on the match time.", WHITE, 100, 490)
            pygame.display.flip()

# Creating the screen
screen = pygame.display.set_mode((930, 580), 0, 32)
menu_bg = load_image('../images/battleship.jpg')
menu_items = ('Back', '')
pygame.display.set_caption('Game Menu')
gm = GameMenu(screen, menu_items)