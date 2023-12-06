import sys
sys.path.append('../wise23-24_superhirn_25/')

from enum import Enum
from termcolor import colored, cprint


class CodeColors:

    # folgende attribute speichern die möglichen
    # farben, die der spiele für das spiel auswählen,
    # bzw. verwenden kann
    def __init__(self) -> None:
        
        self.colors = {}
        
        self.colors[1]   = "black"
        self.colors[2]     = "red"
        self.colors[3]   = "green"
        self.colors[4]  = "yellow"
        self.colors[5]    = "blue"
        self.colors[6] = "magenta"
        self.colors[7]    = "cyan"
        self.colors[8]   = "white"


    def getColor(self, key) -> str:
        return self.colors.get(key)

