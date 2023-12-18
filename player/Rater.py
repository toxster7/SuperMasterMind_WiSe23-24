import random 
from itertools import product
import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *
from gui.codeColors import *


class Rater:

    def __init__(self, code_len, n_colors) -> None:
        self.code_len = code_len
        self.n_colors = n_colors
        colors = CodeColors()
        self.colors = list(colors.colors.keys())[0:int(self.n_colors)]
        
    def rate(self, guesses, feedbacks)->list:
        pass

    def bewerteFeedback(self, runden):
        return True
    

class BotRater(Rater):

    def __init__(self, code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)
        self.possible_codes = self.get_all_possible_codes()

    def get_all_possible_codes(self):
    # Erzeugt alle möglichen Kombinationen von Farben der gegebenen Länge.
        colors = CodeColors()
        return list(product(self.colors, repeat= int(self.code_len)))

    def calcCorPosCorCol(self, feedback):
        corPos = feedback.count(8)
        corCol = feedback.count(7)
        return corPos, corCol

    def giveFeedback(self, code,guess)->list:
        feedback = []
        temp_code = code.copy()
        #check for correct pos
        for i, cur in enumerate(guess):
            if temp_code[i] == int(cur):
                feedback.append(str(8))
                temp_code[i] = 0
                guess[i] = -1

        for i, cur in enumerate(guess):
            if int(cur) in temp_code:
                feedback.append(str(7))
                temp_code[temp_code.index(int(cur))] = 0
                guess[i] = -1
        
        for cur in guess:    
            feedback.append(str(0))

        return feedback[0:int(self.code_len)]

    def minimize_maximums(self, guess, feedback):
        # Minimiert das Maximum der möglichen Antworten basierend auf vorherigen Vermutungen.
        #self.possible_codes.remove(tuple(guess))
        self.possible_codes = [code for code in self.possible_codes if self.giveFeedback(list(code), list(guess).copy()) == feedback]
        
        if not self.possible_codes:
            return None
        '''
        for code in self.possible_codes:
            if self.giveFeedback(list(code), list(guess).copy()) != feedback:
                self.possible_codes.remove(tuple(code))
            if(len(self.possible_codes) == 0):
                return None
            rand = random.randint(0, len(self.possible_codes)-1)
        '''
        return list(random.choice(self.possible_codes))

    def rate(self, guesses, feedbacks)->list:
        
        if(len(guesses)==0):
            random_number = random.randint(1, int(self.n_colors))
            guess = (self.colors[random_number-1],) * int(self.code_len)  # Erster Tipp ist eine beliebige Kombination
        else:
            guess = self.minimize_maximums(guesses[len(guesses)-1].copy(), feedbacks[len(guesses)-1].copy())       
        return list(guess)
    
    def bewerteFeedback(self, runden):
        return False
    
class HumanRater(Rater):
    
    def __init__(self, code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)
        self.handler = InputHandler()

    def rate(self, guesses, feedbacks):
        return self.handler.getGuess(self.code_len, self.n_colors)

'''
bot = BotRater(4,4)
#print(bot.get_all_possible_codes())
guess= [1,1,1,1,1]
code = [2,2,1,4]
guesses = []
feedbacks = []
#print(bot.giveFeedback(code, [1,1,1,4]))

for _ in range(10):
    guess = bot.rate(guesses, feedbacks)
    print("Code", code)
    print("Guess", guess)
    feedback = bot.giveFeedback(code, list(guess).copy())
    print("Feedback", feedback)
    guesses.append(guess)
    feedbacks.append(feedback)
  

    
    #print(bot.possible_codes)
'''    