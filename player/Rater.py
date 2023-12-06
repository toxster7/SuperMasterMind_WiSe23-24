class Rater:

    def __init__(self) -> None:
        pass

    def rate(self, runden)->str:
        pass

    def bewerteFeedback(self, runden):
        return True
    

class BotRater(Rater):

    def __init__(self) -> None:
        super().__init__()

    def rate(self, runden)->str:
        return "1234"
    
    def bewerteFeedback(self, runden):
        return False
    
class HumanRater(Rater):
    
    def __init__(self) -> None:
        super().__init__()

    def rate(self, runden):
        return input("Gib eine Zeichenkette ein: ")