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
            user_input = input("Start Game: (y/n)")
            if(len(user_input) > 20):
                
            while self.laeuft:
                print("laeuft")
                return



sm = Supermastermind()
