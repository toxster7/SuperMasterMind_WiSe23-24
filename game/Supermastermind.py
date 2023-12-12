import argparse
import time

import sys
sys.path.append('../wise23-24_superhirn_25/')

from gui.Menu import Menu
from gui.Spielfeld import Spielfeld


"""
    diese klasse dient dazu die unterschiedliche menüs anzuzeigen,
    welche der user durchlafen muss.
    des weiteren, nimmt diese klasse eingaben des nutzer entgegen,
    die für das spiel notwendig sind
    
    @authro: Anton, Florian 
"""

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
        self.settings = None

    def resetGame(self) -> None:
        self.runden = []
        self.rater = None
        self.coder = None
        self.laeuft = False

    def gameLoop(self) -> None:
        while (True):
            self.settings = self.menu.handler.getUserInput()
            self.laeuft = True
            while self.laeuft:
                print(f"Läuft mit Setting: {self.settings["anzahl_farben"]}, {self.settings["anzahl_pos"]}")
               
            return



sm = Supermastermind()
