import argparse
import time

import sys
sys.path.append('../wise23-24_superhirn_25/')

from gui.Menu import Menu
from gui.Spielfeld import Spielfeld

class Supermastermind:

    def __init__(self) -> None:
        self.id = None
        self.runden = []
        self.rater = None
        self.coder = None
        self.spielfeld = Spielfeld()
        self.menu = Menu()
        self.laeuft = False
        self.gameLoop()

    def resetGame(self) -> None:
        self.runden = []
        self.rater = None
        self.coder = None
        self.laeuft = False

    def gameLoop(self) -> None:
        while (True):
            self.menu.displayMenu()
            user_input = input("Start Game: (y/n)")
            self.laeuft = True
            
            while self.laeuft:
                self.spielfeld.display_interface("TEst")
                user_input = input("End Game: (y/n)")
                return



sm = Supermastermind()
