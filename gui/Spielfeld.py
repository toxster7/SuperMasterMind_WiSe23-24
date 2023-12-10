import sys
#sys.path.append('../wise23-24_superhirn_25/')
# own modules
# TODO: fix import!!!!
from InputHandler import *
from utils.codeColors import CodeColors

class Spielfeld:

    trys_left      : int
    trys           : list
    code           : list
    list_of_colors : list

    def __init__( self ) -> None:

        self.trys_left      = 10
        self.trys           = []
        self.code           = []
        self.list_of_colors = []


    def showGamefield( self ) -> None:

        # erstellen des handler obj
        # wird benötigt, um die spielopt.
        # zubekommen

        handler       = InputHandler()
        game_settings = handler.getUserInput()
        game_settings["anzahl_pos"] = 4 # tmp
        game_settings["anzahl_farben"] = 4 # tmp
        print(game_settings)

        # setzten der default len des codes
        # der spieler darf die länge des codes
        # nicht überschreiten

        self.code = [ "" for pos in range( game_settings.get( "anzahl_pos" ) ) ]

        # erstellen des colors obj bzw. aufruf der enum,
        # getGameColors gibt uns die list der farben
        # die in diesem spiel verwendet werden

        term_colors = CodeColors()
        self.list_of_colors = term_colors.getGameColors( game_settings["anzahl_farben"] )

        handler.getCodeInput()
        print( handler.getCode() )
        # formatieren des spielfeldes,
        # nachdem die farben und der code festgelegt wurde
        #self.formatPlayfield( self.list_of_colors, self.code )

    def formatPlayfield( self, guess_colors, code ):

        pass




a = Spielfeld()
a.showGamefield()




