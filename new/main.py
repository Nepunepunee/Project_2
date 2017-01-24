import pygame
import Menu

class program:
    def __init__(self):
        self.currentscene = Menu

    def run(self):
        if self.currentscene.__name__ == "Menu":
            self.currentscene = self.currentscene.gm.run()
            if self.currentscene == "Start":
                print("start")
            elif self.currentscene == "Instructions":
                print("in")
            elif self.currentscene == "Quit":
                self.quitgame()


        # Update + draw opzet
        # self.currentscene = self.currentscene.update()
        # self.currentscene.draw()

    def quitgame(self):
        pygame.quit()
        quit()

start = program()
start.run()