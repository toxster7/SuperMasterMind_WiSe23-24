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
        # server_addr - adresse des server, wenn über das net gespielt wird
        # server_port - der port über den der server kommuniziert
        """

        self.gamer_id      = ""
        self.game_id       = ""
        self.anzahl_farben = ""
        self.anzahl_pos    = ""
        self.server_addr   = ""
        self.server_port   = ""
        self.auswahl       = ""
        self.run_locale    = False


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

    def setUserInput( self, locale_game ) -> None:

        """
        diese funktion nimmt die spieloptionen des nutzers
        entgegen und speichert diese in den klassen attr
        """
        cprint("\t\t\t[*] Enter your gamer tag: ", "yellow", end="")
        self.gamer_id = input()

        cprint("\t\t\t[*] Enter your chois for the colors: ", end="")
        self.anzahl_farben = input()

        cprint("\t\t\t[*] How many fields do you want to play with [min 4 - max 5]: ", "yellow", end="")
        self.anzahl_pos = input()
        
        if not locale_game:

            self.run_locale = loacle_game 
            
            cprint("[*] Bitte gebe die URL des Servers ein: ", "yellow", end="")
            self.server_addr = input()

            cprint("[*] Bitte gebe den Server Port an: ", "yellow", end="")
            self.server_port = input()


    def getUserInput( self ) -> dict:
        
        """
        diese funktion erstellt ein dict,
        worin sich die klassen attr befinde die 
        später weiterverwendet werden 
        :return: user_settings <dict> - ein dict von user opt.
        """
        # erstellung des dicts
        # jedes attr bekommt einen eigenen key

        user_settings = { 
                         "Game ID"      : self.game_id, 
                         "Gamer ID"     : self.gamer_id,
                         "anzahl Farben": self.anzahl_farben,
                         "anzahl POS"   : self.anzahl_pos
                        }
        
        # es muss überprüft werden, ob das spiel nur lokal
        # läuft oder ob der nutzer über das internet spielt,
        # wenn ja, müssen noch weitere opt. zum dict
        # hinzugefügt werden

        if not self.run_locale:
            
            # hinzufügen der url/server adr. und server port

            user_settings["URL"]  = self.server_addr
            user_settings["Port"] = self.server_port

        return user_settings
