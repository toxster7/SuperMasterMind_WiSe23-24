import random 

import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *


class Rater:

    def __init__(self, code_len) -> None:
        self.code_len = code_len
        
        
    def rate(self, runden)->list:
        pass

    def bewerteFeedback(self, runden):
        return True
    

class BotRater(Rater):

    def __init__(self, code_len) -> None:
        super().__init__(code_len)

    def rate(self, runden)->list:
        return [random.randint(1, 8) for _ in range(int(self.code_len))]
    
    def bewerteFeedback(self, runden):
        return False
    
class HumanRater(Rater):
    
    def __init__(self, code_len) -> None:
        super().__init__(code_len)
        self.handler = InputHandler()

    def rate(self, runden):
        return self.handler.getGuess(self.code_len)