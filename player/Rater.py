import random 

import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *


class Rater:

    def __init__(self, code_len, n_colors) -> None:
        self.code_len = code_len
        self.n_colors = n_colors
        
        
    def rate(self, guesses, feedbacks)->list:
        pass

    def bewerteFeedback(self, runden):
        return True
    

class BotRater(Rater):

    def __init__(self, code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)

    def rate(self, guesses, feedbacks)->list:
        

        return [random.randint(1, int(self.n_colors)) for _ in range(int(self.code_len))]
    
    def bewerteFeedback(self, runden):
        return False
    
class HumanRater(Rater):
    
    def __init__(self, code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)
        self.handler = InputHandler()

    def rate(self, guesses, feedbacks):
        return self.handler.getGuess(self.code_len, self.n_colors)