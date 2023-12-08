import sys
sys.path.append('../wise23-24_superhirn_25/')

# own modules
# TODO: fix import!!!!
from InputHandler import *


class Spielfeld:

    trys_left : int
    trys      : list
    code      : []

    def __init__( self ) -> None:
        
        self.trys_left  = 10
        self.versuche   = []
        self.code       = []
    
    def tmpColort( self, numbers_of_colors ):
        pass

    def showSpielfeld( self ) -> None:
        
        # erstellen des handler obj
        # wird benötigt, um die spielopt.
        # zubekommen

        handler       = InputHandler()
        game_settings = handler.getUserInput()
        game_settings["anzahl_pos"] = 4 # tmp 
        
        # setzten der default len des codes
        # der spieler darf die länge des codes
        # nicht überschreiten

        self.code = [ "" for pos in range( game_settings.get( "anzahl_pos" ) ) ]

a = Spielfeld()
a.showSpielfeld()


    

