from pygame.locals import *
import pygame, sys, eztext
#
BLACK = (0,0,0)

def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((930, 580))
    # fill the screen w/ white
    screen.fill(BLACK)
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=45, color=(0,0,255), prompt='Naam speler één:   ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    players = []

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)
        # events for txtbx
        events = pygame.event.get()
        # process other events
        if len(players) == 2:
            players.append("Game")
            return players
        for event in events:
            # close it x button is pressed
            if event.type == QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    players.append(txtbx.value)
                    txtbx.prompt = 'Naam speler twee:   '
                    txtbx.value = ''



        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()
