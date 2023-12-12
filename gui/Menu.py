from termcolor import cprint, colored
import sys
sys.path.append('../wise23-24_superhirn_25/')
# own modules
# TODO: anpassen der imports
from gui.MenuPrinter import MenuPrinter 
from gui.OsChecker import OsChecker
from gui.InputHandler import InputHandler
from gui.Spielfeld import Spielfeld





class Menu:
    """
    diese klasse dient dazu die unterschiedliche menüs anzuzeigen,
    welche der user durchlafen muss.
    des weiteren, nimmt diese klasse eingaben des nutzer entgegen,
    die für das spiel notwendig sind
    
    @authro: Ilai, Berkan
    """

    def __init__( self ) -> None:

        """
        konstruktor der klasse Menu
    
        # init der klassen attr.
        # auswahl - ist die menü auswahl
        """
        self.auswahl   = ""
        self.game_grid = Spielfeld()
        self.handler   = InputHandler()
        self.guesser   = True
        

    def runMenus( self ):

        """
        diese funktion dient zum anzeigen der menüs
        die der benutzer durchlaufen muss, um das 
        spiel zu start
        
        """
        # anzeigen des start menüs und
        # danach auf die user eingabe warten

        MenuPrinter.displayMenu()

        # erstellen eines handler objk
        # eingabe des benutzer in einem attr
        # speichern
        self.auswahl = self.handler.getUserSelection()

        # sollte die eingabe des benutzers 2 sein
        # wird das spiel beendet
        #
        # wenn die zahl 1 ist wird das nächste menü
        # aufgerufen
        
        if self.auswahl == "2":

            # das spiel wird einfach beendet    
            cprint( "\t\t[+] Aufwieder sehen :)", "green" )
            sys.exit( 0 )

        elif self.auswahl == "1":

            # die func clearTerminal sorgt dafür, dass immer nur, das
            # aktuell menü angezeigt, da es das terminal cleart 
            # aufruf des menüs, das die rollen anzeigt
            # erneut die eingabe des benutzer abwarten
            
            OsChecker.clearTerminal()
            MenuPrinter.displayRoleType()
            self.auswahl = self.handler.getUserSelection()

            # prüfen welche option der nutzer gewählt hat
            # bzw. als der benutzer spielen möchte
            # wenn der benutzer '1' -> Codierer

            if self.auswahl == "1":
                
                # clearen des terminals   
                # aufruf des menüs, das den gametype bestimmt
                # 
                # danach wird von der handel klasse der input
                # des benutzer eingelesen
                # 
                # nachdem wird geprüft, ob der benutzer lokal
                # oder über das netzwerk spielen möchte
                # mit dieser funktion wird auch gleichzeitig
                # das menü angezeigt

                OsChecker.clearTerminal() 
                MenuPrinter.displayGameType() 
                self.guesser = False
                self.auswahl = self.handler.getUserSelection()
                self.selectLocalOrNet()
                
            # wenn der benutzer '2' -> Rater

            elif self.auswahl == "2":

                # clearen des terminals   
                # aufruf des menüs, das den gametype bestimmt
                #
                # danach wird von der handel klasse der input
                # des benutzer eingelesen
                # 
                # nachdem wird geprüft, ob der benutzer lokal
                # oder über das netzwerk spielen möchte
                # mit dieser funktion wird auch gleichzeitig
                # das menü angezeigt

                OsChecker.clearTerminal()
                MenuPrinter.displayGameType()
                self.auswahl = self.handler.getUserSelection()
                self.selectLocalOrNet()
                self.settings.guesser = True
                return self.handler
                
    def selectLocalOrNet( self ) -> None:

        """
        diese funktion dient dazu, etwas code
        zu sparen, dont repeat. Sie zeigt das
        menü für ein lokales oder über das netzwerk
        spiel an. 
        des weiteren dient sie dazu die spiel optionen
        des benutzer anzunehmen
        """
        OsChecker.clearTerminal()
        MenuPrinter.displayGameOptionsLocal()

        if self.auswahl == "1":

            self.handler.setUserInput( True )
            #self.game_grid.showGamefield( self.handler, self.guesser )

        elif self.auswahl == "2":

            self.handler.setUserInput( False )
            #self.game_grid.showGamefield( self.handler, self.guesser )
            

# nur für das testen hier,
# wenn später aufgerufen,
# dann sollte das in die main klasse!

try:

    m = Menu()
    m.runMenus()

except KeyboardInterrupt as key_inter:
    
    print()
    cprint( "\t\t\t[-] Immer diese Interrupts :(", "red" )
    cprint( "\t\t\t[+] Exiting...", "green" )
    sys.exit(0)
