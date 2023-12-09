import sys

sys.path.append('../wise23-24_superhirn_25/')

class CodeColors:

    # folgende attribute speichern die möglichen
    # farben, die der spiele für das spiel auswählen,
    # bzw. verwenden kann
    def __init__(self) -> None:
        self.colors = {}

        self.colors[1] = "red"
        self.colors[2] = "green"
        self.colors[3] = "yellow"
        self.colors[4] = "blue"
        self.colors[5] = "orange"
        self.colors[6] = "brown"
        self.colors[7] = "white"
        self.colors[8] = "black"

    def getColor(self, key) -> str:
        """
        diese funktion dient dazu den key
        des sets zubekommen, wo die farbe
        gespeichert ist, die gebraucht wird
        :return: str der farbe
        """
        return self.colors.get(key)

    def getGameColors(self, nr_of_colors) -> list:
        """
        diese funktion erstellt eine liste von farben
        :parm: nr_of_colors - ist die anzahl der farben
        :return: eine list von farben als str
        """
        list_of_colors = []

        for term_str in range( 1, nr_of_colors + 1):

            list_of_colors.append( self.getColor( nr_of_colors ) )

        return list_of_colors