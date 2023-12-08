from termcolor import cprint
from InputHandler import *

class GuiValidater:

    
    def __init__(self) -> None:
        pass

    def validateRangeNumbers( self, input_to_validate ) -> bool:
        
        """
        diese funktion dient dazu den input des nutzers zu
        validieren. sprich, ob der nutzer auch die angeforderten
        datentypen und die geforderte range der farben zahl eingibt
        :return: True/False 
        """
        
        # die folgende überprüfung muss in ein try/except block,
        # da auch benutzer auch chars bzw. strs eigeben kann,
        # das verfehlt den datentype

        try:
            # die folgende bedinung prüft, ob der eingegebene
            # input des nutzers in der angeforderten range liegt
            # die eingabe muss zwischen 2 und 8 liegen, für die farben.
            # oder die eingabe muss zwischen 4 und 5 liegen, für die felder
            #
            # wenn die zahl nicht in der angeforderten range liegt
            # wird der user darüber informiert und es wird true
            # zurückgegeben

            if ( int( input_to_validate ) in range( 2, 9 ) ) or ( int( input_to_validate ) in range( 4, 5 ) ):
                
                # es wird false zurückgegeben, damit die while-loop
                # beendet werden kann und der user zur nächsten
                # eingabe weiter kann

                return False
            
            else:
               
                cprint("\t\t[-] Bitte gebe Zahl ein, die in der Range liegt", "red")
                return True
        
        except ValueError:
                
                cprint("\t\t[-] Das war keine Zahl...", "red")
                return True


    def validateMenu( self, input_to_validate ) -> bool:
        
        """
        diese funktion dient dazu den input des nutzers zu
        validieren. sprich, ob der nutzer auch die angeforderten
        datentypen und ob die auswahl in der range liegt
        :return: True/False 
        """
        try:
            # die folgende überprüfung muss in ein try/except block,
            # da auch benutzer auch chars bzw. strs eigeben kann,
            # das verfehlt den datentype
   
            if int( input_to_validate ) in range( 1, 3):
                
                return False
            
            else:

                cprint("\t\t[-] Bitte gebe eine Zahl ein, die in der Range liegt", "red")
                return True

        except ValueError:
            
            cprint("\t\t[-] Das war keine Zahl...", "red")
            return True

    def validateUrl( self, input_to_validate ) -> bool:

        pass

