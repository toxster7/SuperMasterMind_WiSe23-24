from termcolor import cprint
import sys
sys.path.append('../wise23-24_superhirn_25/')
from ourUtils.Validator import Validator

class InputHandler:

    # deklarieren von klassen attr
    game_id       : int
    gamer_id      : str
    anzahl_farben : str
    anzahl_pos    : str
    server_addr   : str
    server_port   : str
    run_local     : bool
    code_to_guess : list
    guess         : list
    auswahl       : str
    guesser       : bool

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
        self.code_to_guess = []
        self.guess         = []
        self.auswahl       = ""
        self.guesser       = True

    def getUserSelection( self ) -> str:

        """
        diese funktion dient dazu, den intput bzw.
        die auswahl des benutzer entgegenzunehmen
        :return: self.auswahl <str> - gibt die auswahl als str zurück
        """
        validater   = Validator()
        check_input = True

        # der schleife läuft so lange bis der benutzer
        # die richtige eingabe gemacht hat, die von ihm
        # verlangt wird
        #
        # die func validateMenu sorgt dafür, das diese while-loop
        # beendet wird

        while check_input:
     
            # man hätte es auch in one line schreiben können,
            # aber mit dem cprint sieht es einfach cooler aus :)           
            cprint( "\t\t[*] Optionen: ", "yellow", end="" )
            self.auswahl = input()
            check_input  = validater.validateRangeNumbers( self.auswahl, 1,3 )

        return self.auswahl

    def getCodeInput( self, anzahl_pos, n_colors ):

        """
        diese funktion dient dazu den code für das spiel
        entgegenzunehmen. sie speichert diesen in dem
        attr 'code_to_guess'
        """

        # erstellen eines validater obj,
        # da der input des user validiert werden muss,
        # ob der code im richtigem format ist

        validater   = Validator()
        check_input = True
        cprint("\t\t[!] Der Code sollte folgendes Format habe, als Beispiel: 1234 ", "magenta")

        # solange der benutzer nicht die richtige eingabe
        # gemacht hat, wird diese wiederholt

        while check_input:

            try:
                # eingabe des users einlesen, und diesen an einem
                # '.' splitten. jede ziffer des codes hat dann einen
                # platz, in der liste

                cprint("\t\t[*] Gebe den Code ein: ", "yellow", end="")
                inp = list(input())
                check_input        = validater.validateCode( inp, anzahl_pos, n_colors )
             
                # wenn das immer noch wahr ist, nach der
                # validierung, wird die liste geleert
  
                if check_input:
                    self.code_to_guess = []
                else:
                    self.code_to_guess = [int(i) for i in inp]

            except KeyboardInterrupt:
                print()
                cprint("\t\t[-] Immer diese Interrupts :(", "red")
                cprint("\t\t[+] Exiting...", "green")
                sys.exit(0)
        return self.code_to_guess

    def getCode(self) -> list:
        """
        diese funktion gibt eine liste mit
        dem code zurück, den der spieler gesetzt hat
        :return: code_to_guess - liste mit dem code
        """
        return self.code_to_guess

    def getGuess(self, anzahl_pos, n_colors) -> list:

        validater   = Validator()
        check_input = True

        while check_input:

            try:
                cprint("\t\t[*] Gebe deinen Guess ein: ", "yellow", end="")
                self.guess = list(input())
                check_input = validater.validateCode( self.guess, anzahl_pos, n_colors )

                if check_input:
                    self.guess = []

            except KeyboardInterrupt:
                print()
                cprint("\t\t[-] Immer diese Interrupts :(", "red")
                cprint("\t\t[+] Exiting...", "green")
                sys.exit(0)

        return self.guess

    def getFeedback(self, anzahl_pos) -> list:

        validater   = Validator()
        check_input = True

        while check_input:

            try:
                cprint("\t\t[*] Gebe dein Feedback ein: ", "yellow", end="")
                feedback = list(input())
                while len(feedback) < int(anzahl_pos):
                    feedback.append("0")
                feedback.sort(reverse=True)
                
                check_input = validater.validateFeedback( feedback, anzahl_pos )

                if check_input:

                    feedback = []

            except KeyboardInterrupt:
                print()
                cprint("\t\t[-] Immer diese Interrupts :(", "red")
                cprint("\t\t[+] Exiting...", "green")
                sys.exit(0)

        return feedback


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

        validater     = Validator()
        check_input_1 = True
        check_input_2 = True
            
        cprint("\t\t[*] Gebe deine Username ein: ", "yellow", end="")
        self.gamer_id = input()
        
        # die loop läuft so lange, bis der user die eingaben
        # richtig eingegeben hat
        # dabei wird geguckt, ob er die richtige range und zahlen
        # eingibt. bei der nächsten while-loop ist das gleich
        # es gibt bestimmt einen besseren weg ... :(

        while check_input_1:
        
            cprint("\t\t[*] Mit wie vielen Farben möchtest Du spielen [min 2 - max 8]: ", "yellow", end="")
            self.anzahl_farben = input()
            check_input_1      = validater.validateRangeNumbers( self.anzahl_farben,2,9)

        while check_input_2:
            
            cprint("\t\t[*] Mit wie vielen Feldern möchtest Du spielen [min 4 - max 5]: ", "yellow", end="")
            self.anzahl_pos = input()
            check_input_2   = validater.validateRangeNumbers( self.anzahl_pos,4,6)
        
        if not local_game:

            self.run_local = local_game
            
            #cprint("\t\t[*] Bitte gebe die URL des Servers ein: ", "yellow", end="")
            while(not validater.validateUrl(self.server_addr)):
                cprint("\t\t[*] Bitte gebe die IP des Servers ein: ", "yellow", end="")
                self.server_addr = input()
            while(not validater.validatePort(self.server_port)):
                cprint("\t\t[*] Bitte gebe den Server Port an: ", "yellow", end="")
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
                         "game_id"      : self.game_id, 
                         "gamer_id"     : self.gamer_id,
                         "anzahl_farben": self.anzahl_farben,
                         "anzahl_pos"   : self.anzahl_pos,
                         "guesser"      : self.guesser
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
