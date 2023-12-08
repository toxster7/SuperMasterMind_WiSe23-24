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

        self.colors[1] = "red"
        self.colors[2] = "green"
        self.colors[3] = "yellow"
        self.colors[4] = "blue"
        self.colors[5] = "orange"
        self.colors[6] = "brown"
        self.colors[7] = "white"
        self.colors[8] = "black"

    def getColor(self, key) -> str:
        return self.colors.get(key)

