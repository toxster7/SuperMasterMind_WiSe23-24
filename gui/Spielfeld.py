import sys
import random
sys.path.append('../wise23-24_superhirn_25/')
# own modules
# TODO: fix import!!!!
from gui.InputHandler import *
from gui.codeColors import *
from gui.OsChecker import *

class Spielfeld:

    trys_left      : int
    trys           : int
    code           : list
    list_of_colors : list

    def __init__(self) -> None:

        self.trys_left      = 10
        self.trys           = 0
        self.code           = []
        self.list_of_colors = []
        self.term_colors    = CodeColors()

    def tempFunc( self, pos ):
        """
        diese funktion ist nur tem hier
        diese wird entfertn, wenn die funk
        für den coder komplett ist
        """
        for nr in range( int(pos) ):
            self.code.append( str( random.randint(1, 8) ))

    def showGamefield( self, handler, guesser ) -> None:

        # erstellen des handler obj
        # wird benötigt, um die spielopt.
        # zubekommen

        game_settings = handler.getUserInput()

        if not guesser:
            # erstellen des colors obj bzw. aufruf der enum.
            # erstellen eines handlers für den code input
            # speichern des eingegeben codes
            # danach wird der code gefärbt, dabei hat jede
            # zahl eine eigene farbe und diese wird dann im code
            # gespeichert
            handler.getCodeInput()
            self.code = handler.getCode()
            self.code = self.term_colors.coloredFormatStr( self.code )
        
        else: 
            OsChecker.clearTerminal()
            
            print("\t\t[BOT] Generie Code zum Raten...")
            self.tempFunc(game_settings["anzahl_pos"]) # TODO muss entfernt werden 
            self.code = self.term_colors.coloredFormatStr( self.code )

            print("\t\t[*] Das Spiel beginnt. Dein Gegner hat einen Code gesetzt")
            print("\t\t[*] Du hast 10 versuche diesen Code zu erraten")
            print("\t\t[DEBUG] ", end="")
            for nr in self.code:
                print(" "+ nr + " ", end="")
            print()

            # formatieren des spielfeldes,
            # nachdem die farben und der code festgelegt wurde
            self.formatPlayfield( game_settings["anzahl_pos"], handler )

    def formatPlayfield( self, anzahl_pos, handler ):

        format_print_5 = "\t\t| \t{nr_1}\t\t{nr_2}\t\t{nr_3}\t\t{nr_4}\t   {nr_5}\t |"
        format_print_4 = "\t\t| \t\t{nr_1}\t\t{nr_2}\t\t{nr_3}\t\t{nr_4}\t |"
        play_grid      = ["\t\t+"+ "-" * 72 +  "+"]

        guess = self.term_colors.coloredFormatStr( handler.getGuess() )
        self.trys += 1
        OsChecker.clearTerminal()

        while self.trys <= self.trys_left :

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

            if self.trys < 10:
                print()
                print("\t\t[+] Guess: {}".format( self.trys ))
                guess = self.term_colors.coloredFormatStr(handler.getGuess())

            self.trys += 1
