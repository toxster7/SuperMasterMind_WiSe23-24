from termcolor import cprint, colored
import sys
sys.path.append('../wise23-24_superhirn_25/')

class Menu:

    def __init__(self, game) -> None:

        """
        konstruktor der klasse Menu
    
        # init der klassen attr.
        # gamer_id - ist der name des spielers
        # game_id - ist die nummer des spiels
        # anzahl_farben - auswahl der farben mit denen gespielt wird
        # anzahl_pos - auswahl der positionen mit denen gespielt wird
        """
        self.game = game
        self.gamer_id      = ""
        self.game_id       = 0
        self.anzahl_farben = 0
        self.anzahl_pos    = 0
        self.auswahl       = ""


    def getUserInput( self ):
        
        """
        
        diese funktion dient dazu, den intput bzw.
        die auswahl des benutzer entgegenzunehmen
        @return self.auswahl <str> - gibt die auswahl als str zurück

        """
        self.auswahl = input("\t\t\t[*] Option: ")

        return self.auswahl


    def displayMenu( self ) -> None:

        """
        diese funktion dient dazu, das start menü,
        für das spiel anzuzeigen
        """

        print(
        """
                 __,                     ,__
             __/==+\      Spielmenü     /+==\__
                "  "`  ================ '"  "
            
            +------------------------------------+
            | Superhirn ein Logikspiel für deine |
            |           high performance!        |
            |   Bitte wähle einer der Optionen:  |
            |                                    |
            |                                    |
            |       [1] Spiel starten            |
            |       [2] Spiel beenden            |
            +------------------------------------+
        """
        )

    def runMenu( self ):

        self.displayMenu()
        a = self.getUserInput()
        print(a)

m = Menu()
m.runMenu()
