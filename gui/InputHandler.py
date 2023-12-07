from termcolor import cprint

class InputHandler:

    def __init__( self ) -> None:

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



    def getUserSelection( self ) -> str:

        """
        diese funktion dient dazu, den intput bzw.
        die auswahl des benutzer entgegenzunehmen
        :return self.auswahl <str> - gibt die auswahl als str zurück
        """

        # man hätte es auch in one line schreiben können,
        # aber mit dem cprint sieht es einfach cooler aus :)

        cprint( "\t\t\t[*] Optionen: ", "yellow", end="" )
        self.auswahl = input()

        return self.auswahl

    def setUserInput( self ) -> None:


        cprint("\t\t\t[*] Enter your gamer tag: ", "yellow", end="")
        self.gamer_id = input()

        cprint("\t\t\t[*] Enter your chois for the colors: ", end="")
        self.anzahl_farben = input()

        cprint("\t\t\t[*] How many fields do you want to play with [min 4 - max 5]: ", "yellow", end="")
        self.anzahl_pos = input()

    def getUserInput( self ) -> list:

        user_settings = []
        user_settings.append( self.gamer_id )
        user_settings.append( self.anzahl_farben )
        user_settings.append( self.anzahl_pos )
        
        return user_settings
