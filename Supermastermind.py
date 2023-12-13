from termcolor import cprint
import argparse
import time

import sys
sys.path.insert(0, '../wise23-24_superhirn_25/')

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
        
        self.menu.runMenus()

try:
    sm = Supermastermind()
    sm.gameLoop()

except KeyboardInterrupt:
    
    print()
    cprint("\t\t[-] Immer diese Interrupts :(", "red" )
    cprint("\t\t[+] Exiting...", "green" )
    sys.exit(0)
