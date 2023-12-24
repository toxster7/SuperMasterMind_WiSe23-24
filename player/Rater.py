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
        self.used_numbers = set()

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
        guess_copy = guess.copy()

        for i, cur in enumerate(guess):
            if temp_code[i] == int(cur):
                feedback.append(str(8))
                temp_code[i] = 0
                guess_copy[i] = -1

        for i, cur in enumerate(guess_copy):
            if int(cur) in temp_code and int(cur) != -1:
                feedback.append(str(7))
                temp_code[temp_code.index(int(cur))] = 0
                guess_copy[i] = -1

        feedback += [str(0)] * (len(guess) - len(feedback))  # Fügt fehlende Nullen hinzu

        return feedback[:int(self.code_len)]
        

    def minimize_maximums(self, guess, feedback):
        # Minimiert das Maximum der möglichen Antworten basierend auf vorherigen Vermutungen.
        #self.possible_codes.remove(tuple(guess))
        self.possible_codes = [code for code in self.possible_codes if self.giveFeedback(list(code), list(guess).copy()) == feedback]
        
        if not self.possible_codes:
            return None
        
        return list(random.choice(self.possible_codes))
    
    def findMaxFeedback(self):
        best_guess = None
        max_count = 0
        possible_codes = self.possible_codes[:]  # Kopie der möglichen Codes für die äußere Schleife

        for code in possible_codes:
            feedbackDict = {}

            for guess in possible_codes:
                feedback = self.giveFeedback(list(code), list(guess))
                feedbackstr = "".join(feedback)

                if feedbackstr in feedbackDict:
                    feedbackDict[feedbackstr] += 1
                else:
                    feedbackDict[feedbackstr] = 1

            max_list = max(feedbackDict.values(), default=0)
            if max_list > max_count:
                max_count = max_list
                best_guess = code
        
        return best_guess


    def rate(self, guesses, feedbacks)->list:
        
        ###Für einfarbige Versuche, die nicht zwingend dem optimal verlauf entsprechen wird hier die Farbe random ausgewählt
        available_numbers = list(set(range(1, int(self.n_colors)+1)) - self.used_numbers)  # Verfügbare Zahlen für die aktuelle Runde
        
        if(len(available_numbers) > 0):
            random_number = random.choice(available_numbers)  # Auswahl einer Zufallszahl aus den verfügbaren Zahlen
            self.used_numbers.add(random_number)  # Hinzufügen der ausgewählten Zahl zu den verwendeten Zahlen
        else:
            random_number = 1


        if(len(guesses)==0 ):
            #random_number = random.randint(1, int(self.n_colors))
            guess = (self.colors[random_number-1],) * int(self.code_len)  # Erster Tipp ist eine beliebige Kombination
            #Falls Code zu lang wird der Code vereinfacht
        else:
            guess = self.minimize_maximums(guesses[len(guesses)-1].copy(), feedbacks[len(guesses)-1].copy())             
            if((len(guesses) <= 3) and (int(self.n_colors)>5)):
                number = random_number
                guess = (self.colors[number-1],) * int(self.code_len)
            else:
                guess = self.findMaxFeedback()
            if(not guess):
                return None
            
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
bot = BotRater('4','8')
#print(bot.get_all_possible_codes())
guess= [1,1,1,1]
code = [(random.randint(2, 8)) for _ in range(4)]
guesses = []
feedbacks = []
#print(bot.giveFeedback(code, [1,1,1,4]))

i = 0
for _ in range(10):
    guess = bot.rate(guesses, feedbacks)
    print("Code", code)
    print("Guess", guess)
    #print(bot.possible_codes)
    if(not guess):
        print("Fehler")
        break
    feedback = bot.giveFeedback(code, list(guess).copy())
    print("Feedback", feedback)
    guesses.append(guess)
    feedbacks.append(feedback)
    if(feedback == ['8', '8', '8', '8']):
        break
    i+=1
  
print("Versuche gebraucht", i)

    
    #print(bot.possible_codes)   
'''