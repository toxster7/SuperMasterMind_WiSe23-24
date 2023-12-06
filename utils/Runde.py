class Runde:

    def __init__(self,code ,feedback) -> None:
        self.code = code
        self.feedback = feedback

class Feedback:

    def __init__(self, nRightColorRightPosition, nRightColor) -> None:
        self.nRightColorRightPosition = nRightColorRightPosition
        self.nRightColor = nRightColor

class Farben(Enum):
    BLAU = '1'
    DIENSTAG = 2
    MITTWOCH = 3
    DONNERSTAG = 4
    FREITAG = 5
    SAMSTAG = 6
    SONNTAG = 7

class Code: