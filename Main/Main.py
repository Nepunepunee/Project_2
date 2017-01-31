import pygame
import Menu
import Game
import Instruction_menu
import Pausemenu
import Highscores
import Players
import Settings_menu

class program:
    def __init__(self):
        self.currentscene = Menu

    def run(self):
        if self.currentscene.__name__ == "Menu":
            self.currentscene = self.currentscene.gm.run()
            if self.currentscene == "Start":
                self.currentscene = Players.main()
            elif self.currentscene == "Instructions":
                self.currentscene = Instruction_menu.gm.run()
            elif self.currentscene == "Highscore":
                #self.currentscene = Highscores.gm.run()
                print('test')
            elif self.currentscene == "Settings":
                self.currentscene = Settings_menu.gm.run()
            elif self.currentscene == "Quit":
                self.quitgame()
        if self.currentscene[2] == "Game":
            self.currentscene = Game.mainloop()
        if self.currentscene == "Back":
            self.currentscene = Menu
        if self.currentscene == "pause":
            self.safestate = self.currentscene
            self.currentscene = Pausemenu.gm.run()
        if self.currentscene == "Resume":
            self.currentscene = Game.mainloop()
        if self.currentscene == "Main menu":
            self.currentscene = Menu
        self.run()


        # Update + draw opzet
        # self.currentscene = self.currentscene.update()
        # self.currentscene.draw()

    def quitgame(self):
        pygame.quit()
        quit()

start = program()
start.run()