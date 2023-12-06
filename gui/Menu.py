from termcolor import cprint, colored
import sys
import os
sys.path.append('../wise23-24_superhirn_25/')
from MenuPrinter import * 


class Menu:

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


    def getUserInput( self ):
        
        """
        
        diese funktion dient dazu, den intput bzw.
        die auswahl des benutzer entgegenzunehmen
        @return self.auswahl <str> - gibt die auswahl als str zurück

        """
        # man hätte es auch in one line schreiben können,
        # aber mit dem cprint sieht es einfach cooler aus :)

        cprint( "\t\t\t[*] Optionen: ", "yellow", end="" )
        self.auswahl = input( )

        return self.auswahl


    def runMenus( self ):

        """
        diese funktion dient zum anzeigen der menüs
        die der benutzer durchlaufen muss, um das 
        spiel zu start
        
        """
        # anzeigen des start menüs und
        # danach auf die user eingabe warten

        MenuPrinter.displayMenu()

        # eingabe des benutzer in einem attr
        # speichern
        
        self.auswahl   = self.getUserInput()

        # sollte die eingabe des benutzers 2 sein
        # wird das spiel beendet
        #
        # wenn die zahl 1 ist wird das nächste menü
        # aufgerufen
        
        if self.auswahl == "2":

            # das spiel wird einfach beendet    
            crint( "[+] Aufwieder sehen :)", "green" )
            sys.exit( 0 )

        elif self.auswahl == "1":

            # erhöhen des menü counters
            # das "clear" sorgt dafür, das immer nur, das
            # aktuell menü angezeigt
            # TODO: os chekcen, das ein unterschiedliches command ist

            select_counter += 1
            os.system("clear")
            
            # aufruf des menüs, das die rollen anzeigt
            # erneut die eingabe des benutzer abwarten
            MenuPrinter.displayRoleType()
            self.auswahl = self.getUserInput()

            if self.auswahl == "1":
                
                os.system("clear")

                # aufruf des menüs, das den gametype bestimmt
                MenuPrinter.displayGameType()
            
            elif self.auswahl == "2":

                os.system("clear")
                MenuPrinter.displayGameType()


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
