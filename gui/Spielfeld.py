import sys
sys.path.append('../wise23-24_superhirn_25/')

class Spielfeld:

    def __init__(self) -> None:
        self.versuch = 10
        self.code = ""
        self.versuche = []



    def showSpielfeld(self):
        pass

    def display_interface(self,data):
        # Löscht den vorherigen Inhalt in der Konsole
        print("\033[H\033[J")
        print("Aktuelle Anzeige:")
        for entry in data:
            print(entry)
        print("Aktualisierung alle 3 Sekunden...")

    def main(self):
        data = []

        while self.versuch >= 0:
            self.display_interface(data)
            user_input = input("Gib hier deinen Code ein: ")
            if user_input:
                data.append(user_input)
                self.versuch -= 1

        data.append("ENDE")
