import sys
#sys.path.append('../wise23-24_superhirn_25/')
# own modules
# TODO: fix import!!!!
from InputHandler import *
from utils.codeColors import CodeColors
from OsChecker import *

class Spielfeld:

    trys_left      : int
    trys           : int
    code           : list
    list_of_colors : list

    def __init__( self ) -> None:

        self.trys_left      = 10
        self.trys           = 0
        self.code           = []
        self.list_of_colors = []


    def showGamefield( self ) -> None:

        # erstellen des handler obj
        # wird benötigt, um die spielopt.
        # zubekommen

        handler       = InputHandler()
        game_settings = handler.getUserInput()
        game_settings["anzahl_farben"] = 4 # tmp

        # erstellen des colors obj bzw. aufruf der enum.
        # erstellen eines handlers für den code input
        # speichern des eingegeben codes
        # danach wird der code gefärbt, dabei hat jede
        # zahl eine eigene farbe und diese wird dann im code
        # gespeichert

        #term_colors = CodeColors()
        #handler.getCodeInput()
        #self.code = handler.getCode()
        #self.code = term_colors.coloredFormatStr( self.code )


        # formatieren des spielfeldes,
        # nachdem die farben und der code festgelegt wurde
        self.formatPlayfield( game_settings["anzahl_pos"], handler )

    def formatPlayfield( self, anzahl_pos, handler ):

        term_colors    = CodeColors()
        format_print_5 = "\t\t| \t{nr_1}\t\t{nr_2}\t\t{nr_3}\t\t{nr_4}\t   {nr_5} |"
        format_print_4 = "\t\t| \t\t{nr_1}\t\t{nr_2}\t\t{nr_3}\t\t{nr_4}\t |"
        play_grid = ["\t\t+------------------------------------+"]
        guess_counter = 2

        guess = term_colors.coloredFormatStr( handler.getGuess() )

        while self.trys < (self.trys_left - 1):

            if anzahl_pos == "5":

                play_grid.append( format_print_5.format( nr_1 = guess[0],
                                             nr_2 = guess[1],
                                             nr_3 = guess[2],
                                             nr_4 = guess[3],
                                             nr_5 = guess[4]))

            elif anzahl_pos == "4":

                play_grid.append( format_print_4.format( nr_1 = guess[0],
                                             nr_2 = guess[1],
                                             nr_3 = guess[2],
                                             nr_4 = guess[3] ) )

            OsChecker.clearTerminal()
            for field in play_grid:

                print(field)

            print()
            print("[+] Guess: {}".format( self.trys ))
            guess = term_colors.coloredFormatStr(handler.getGuess())
            self.trys += 1

a = Spielfeld()
a.showGamefield()