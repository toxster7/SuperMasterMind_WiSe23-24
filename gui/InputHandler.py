from termcolor import cprint
from GuiValidater import *

class InputHandler:

    # deklarieren von klassen attr
    game_id       : int
    gamer_id      : str
    anzahl_farben : str
    anzahl_pos    : str
    server_addr   : str
    server_port   : str
    run_local     : bool 
    auswahl       : str

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
        # run_local - lokales spiel oder übers netz
        """
        self.game_id       = 0
        self.gamer_id      = ""
        self.anzahl_farben = ""
        self.anzahl_pos    = ""
        self.server_addr   = ""
        self.server_port   = ""
        self.run_local     = True
        self.auswahl       = ""

    def getUserSelection( self ) -> str:

        """
        diese funktion dient dazu, den intput bzw.
        die auswahl des benutzer entgegenzunehmen
        :return self.auswahl <str> - gibt die auswahl als str zurück
        """
        validater   = GuiValidater()
        check_input = True

        # man hätte es auch in one line schreiben können,
        # aber mit dem cprint sieht es einfach cooler aus :)
        while check_input:
            
            cprint( "\t\t[*] Optionen: ", "yellow", end="" )
            self.auswahl = input()
            check_input  = validater.validateMenu( self.auswahl )

        return self.auswahl

    def setUserInput( self, local_game ) -> None:

        """
        diese funktion nimmt die spieloptionen des nutzers
        entgegen und speichert diese in den klassen attr
        """
        # erstellen eines validater obj
        # dient dazu um die user eingaben
        # auf korrektheit zu prüfen
        #
        # die checker sind nicht gut gelöst
        # TODO: bessere idee

        validater     = GuiValidater()
        check_input_1 = True
        check_input_2 = True
            
        cprint("\t\t[*] Gebe deine Username ein: ", "yellow", end="")
        self.gamer_id = input()

        while check_input_1:
        
            cprint("\t\t[*] Mit wie vielen Farben möchtest Du spielen [min 2 - max 8]: ", "yellow", end="")
            self.anzahl_farben = input()
            check_input_1      = validater.validateRangeNumbers( self.anzahl_farben )

        while check_input_2:
            
            cprint("\t\t[*] Mit wie vielen Feldern möchtest Du spielen [min 4 - max 5]: ", "yellow", end="")
            self.anzahl_pos = input()
            check_input_2   = validater.validateRangeNumbers( self.anzahl_pos )
        
        if not local_game:

            self.run_local = local_game
            
            cprint("\t\t[*] Bitte gebe die URL des Servers ein: ", "yellow", end="")
            self.server_addr = input()

            cprint("\t\t[*] Bitte gebe den Server Port an: ", "yellow", end="")
            self.server_port = input()


    def getUserInput( self ) -> dict:
        
        """
        diese funktion erstellt ein dict,
        worin sich die klassen attr befinde die 
        später weiterverwendet werden 
        :return: user_settings <dict> - ein dict von user opt.
        """
        # game_id ist beim ersten spiel 0
        # diese id muss später erhöht werden
        
        # erstellung des dicts
        # jedes attr bekommt einen eigenen key

        user_settings = { 
                         "game_id"      : self.game_id, 
                         "gamer_id"     : self.gamer_id,
                         "anzahl_farben": self.anzahl_farben,
                         "anzahl_pos"   : self.anzahl_pos
                        }
        
        # es muss überprüft werden, ob das spiel nur lokal
        # läuft oder ob der nutzer über das internet spielt,
        # wenn ja, müssen noch weitere opt. zum dict
        # hinzugefügt werden

        if not self.run_local:
            
            # hinzufügen der url/server adr. und server port

            user_settings["URL"]  = self.server_addr
            user_settings["port"] = self.server_port

        return user_settings



