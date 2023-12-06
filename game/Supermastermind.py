import argparse
import time
from gui import Spielfeld
from gui import Menu

class Supermastermind:

    def __init__(self) -> None:
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

    def gameLoop(self)->None:
        while(True): 
            
            while self.laeuft:
                print("laeuft")


if __name__ == "__main__":
    sm = Supermastermind()
    pass