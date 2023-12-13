import random
import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *


class Coder:
    
    def __init__(self, code_len, n_colors) -> None:
        self.code = None
        self.code_len = code_len
        self.n_colors = n_colors

    def createCode(self)->list:
        pass

    def giveFeedback(self, guess)->list:
        pass



class BotCoder(Coder):

    def __init__(self,code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)

    def createCode(self) -> list:
        self.code = [random.randint(1, int(self.n_colors)) for _ in range(int(self.code_len))]
        return self.code.copy()
    
    def giveFeedback(self, guess)->list:
        feedback = []
        temp_code = self.code.copy()
        #check for correct pos
        for i, cur in enumerate(guess):
            if temp_code[i] == int(cur):
                feedback.append(8)
                temp_code[i] = 0
                guess[i] = -1

        for i, cur in enumerate(guess):
            if int(cur) in temp_code:
                feedback.append(7)
                temp_code[temp_code.index(int(cur))] = 0
                guess[i] = -1
        
        for cur in guess:    
            feedback.append(0)

        return feedback[0:int(self.code_len)]
        
    
class HumanCoder(Coder):

    def __init__(self, code_len, n_colors) -> None:
        super().__init__(code_len, n_colors)
        self.handler = InputHandler()
        

    def createCode(self) -> list:
        return self.handler.getCodeInput(self.code_len, self.n_colors)
    
    def giveFeedback(self, guess) -> list:
        return self.handler.getFeedback(self.code_len)

class NetCoder(Coder):

    def __init__(self, ip, port) -> None:
        super().__init__()
        self.ip = ip
        self.port = port


    