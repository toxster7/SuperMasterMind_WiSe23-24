from termcolor import cprint, colored
import sys
sys.path.append('../wise23-24_superhirn_25/')

class Menu:

    def __init__(self) -> None:

        """
        konstruktor der klasse Menu
    
        # init der klassen attr.
        # gamer_id - ist der name des spielers
        # game_id - ist die nummer des spiels
        # anzahl_farben - auswahl der farben mit denen gespielt wird
        # anzahl_pos - auswahl der positionen mit denen gespielt wird
        """

        self.gamer_id      = ""
        self.game_id       = 0
        self.anzahl_farben = 0
        self.anzahl_pos    = 0
        self.auswahl       = ""


    def getUserInput():
        pass



    def displayMenu(self) -> None:

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
            +------------------------------------+

                    [1] Spiel starten
                    [2] Spiel beenden

        """
        )

m = Menu()
m.displayMenu()

