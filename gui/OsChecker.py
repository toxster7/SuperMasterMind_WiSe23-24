import sys
import os

class OsChecker:

    """
    diese klasse checkt das os, auf dem das programm läuft.
    sie wird nicht suses machen :)
    TODO: diese klasse sollte vielleicht in ein anders verzeichnis 
    und nicht in das gui verzeichnis!

    @authro: Ilai, Berkan
    """

    def __init__(self) -> None:
        pass

    def clearTerminal() -> None:

        # überprüfen welches os läuft,
        # der befehl, um das terminal zu clearen,
        # ist von os zu os unterschiedlich
        #
        # TODO: checken wie output von mac ist
        # TODO: checken wie output von win ist
        
        if sys.platform == "linux" or sys.platform == "darwin":
            
            os.system("clear")

        elif sys.platform == "windows":
            
            os.system("cls")

