import sys
from termcolor import colored
sys.path.append('../wise23-24_superhirn_25/')

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
        self.colors[5] = "magenta" # orange gibt es nichto
        self.colors[6] = "cyan" # orange gibt es nicht
        self.colors[7] = "white"
        self.colors[8] = "black"

    def getColor(self, key) -> str:
        """
        diese funktion dient dazu den key
        des sets zubekommen, wo die farbe
        gespeichert ist, die gebraucht wird
        :return: str der farbe
        """
        return self.colors.get(key)

    def coloredFormatStr( self, code_to_guess ) -> list:

        for buff, nr in enumerate( code_to_guess ):
            
            code_to_guess[ buff ] = colored( nr, self.getColor( int(nr) ) )

        return code_to_guess


