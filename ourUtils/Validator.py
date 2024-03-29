from termcolor import cprint
import re
import sys
sys.path.append('../wise23-24_superhirn_25/')


class Validator:

    
    def __init__(self) -> None:
        pass

    def validateRangeNumbers( self, input_to_validate ,range_untere_grenze, range_obere_grenze) -> bool:
        
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

            if ( int( input_to_validate ) in range( range_untere_grenze, range_obere_grenze) ) :
                
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



    def validateCode( self, input_to_validate, code_len , n_colors) -> bool:
        """
        diese funktion dient dazu den input des nutzers zu
        validieren. sprich, ob der nutzer auch die angeforderten
        datentypen und die geforderte format des codes einhält
        :return: True/False
        """
        
        # die folgende überprüfung muss in ein try/except block,
        # da auch benutzer auch chars bzw. strs eigeben kann,
        # das verfehlt den datentype
        try:

            # checken, ob die länge der list auch der länge
            # der gesetzten spieloption (mit wv positionen wird gespielt (4-5))
            # gesetzt bzw. eingegben wurde.
            #
            # sollte etwas bei der eingabe fehlerhaft sein, sollte nicht
            # die gewünschte länge der liste zustande kommen

            if len( input_to_validate ) == int( code_len ):

                # nachdem wir überprüft haben, ob die liste die
                # richtige länge hat, gegen wir jetzt noch jedes
                # element in der liste durch, um zu prüfen, ob
                # es sich auch hier um zahlen und zahlen im richtigen
                # bereich handelt

                for ele in input_to_validate:

                    # überprüfen, ob die zahlen im bereich der setzbaren
                    # zaheln liegen (1-8), wenn ja, sollte der code richtig
                    # sein und wir können false zurückgeben andernfalls
                    # wird true zurückgegeben

                    if ( int( ele ) > int(n_colors)) or ( int( ele ) <= 0 ):

                        return True

                return False

            else:
                cprint("\t\t[-] Falsches Format... z. B. 1234(5)", "red")
                return True

        except ValueError:

            cprint("\t\t[-] Das waren keine Zahlen...", "red")
            return True

    def validateFeedback( self, input_to_validate, code_len ) -> bool:
        """
        diese funktion dient dazu den input des nutzers zu
        validieren. sprich, ob der nutzer auch die angeforderten
        datentypen und die geforderte format des codes einhält
        :return: True/False
        """
        
        # die folgende überprüfung muss in ein try/except block,
        # da auch benutzer auch chars bzw. strs eigeben kann,
        # das verfehlt den datentype
        try:

            # checken, ob die länge der list auch der länge
            # der gesetzten spieloption (mit wv positionen wird gespielt (4-5))
            # gesetzt bzw. eingegben wurde.
            #
            # sollte etwas bei der eingabe fehlerhaft sein, sollte nicht
            # die gewünschte länge der liste zustande kommen

            if len( input_to_validate ) == int( code_len ):

                # nachdem wir überprüft haben, ob die liste die
                # richtige länge hat, gegen wir jetzt noch jedes
                # element in der liste durch, um zu prüfen, ob
                # es sich auch hier um zahlen und zahlen im richtigen
                # bereich handelt

                for ele in input_to_validate:

                    # überprüfen, ob die zahlen im bereich der setzbaren
                    # zaheln liegen (1-8), wenn ja, sollte der code richtig
                    # sein und wir können false zurückgeben andernfalls
                    # wird true zurückgegeben

                    if ((int( ele ) not in range(7,9)) and (not int(ele) == 0)):
                        cprint("\t\t[-] Ungültiges Feedback... Bitte nutze nur 7 und 8", "red")
                        return True

                return False

            else:
                cprint("\t\t[-] Falsches Format... z. B. 87...", "red")
                return True

        except ValueError:

            cprint("\t\t[-] Das waren keine Zahlen...", "red")
            return True

    def validateUrl( self, ip ) -> bool:
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    
        # Überprüfe, ob die Eingabe der IP-Adressenstruktur entspricht
        if re.match(pattern, ip):
            # Trenne die Zahlenblöcke auf
            octets = ip.split('.')
            # Überprüfe, ob jede Zahl in einem gültigen Bereich liegt (0-255)
            return all(0 <= int(octet) <= 255 for octet in octets)
    
        return False
    
    def validatePort(self, port):
        try:
            port_num = int(port)
            if 0 <= port_num <= 65535:
                return True
            else:
                return False
        except ValueError:
            return False

