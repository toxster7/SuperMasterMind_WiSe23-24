import random
import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *
from ourUtils.RequestHandler import *


class Coder:
    
    def __init__(self, code_len, n_colors) -> None:
        self.code = None
        self.code_len = code_len
        self.n_colors = n_colors
        self.game_id = 0

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

    def __init__(self, code_len , n_colors,ip, port, gamerid) -> None:
        super().__init__(code_len , n_colors)
        self.ip = ip
        self.port = port
        self.request_handler = RequestHandler(gamerid, self.code_len, self.n_colors, self.ip, self.port)
        


    def createCode(self)->list:
        
        code_json = self.request_handler.sendRequest(0,"")
       
        self.game_id = code_json["gameid"]
        
        self.code = [int(s) for s in code_json["value"]]
        
        return self.code

    def giveFeedback(self, guess)->list:
        guess_str = "".join([str(i) for i in guess])
      
        feedback_json = self.request_handler.sendRequest(self.game_id, guess_str)
        feedback = [s for s in feedback_json["value"]]
        
        while(len(feedback)<int(self.code_len)):
            feedback.append('0')

        return feedback
'''
coder = NetCoder(5 , 4,'141.45.38.219', 5001, "flrnbr")
#hCoder = BotCoder(4,4)
#print(hCoder.createCode())
print(coder.createCode())
print(coder.giveFeedback(['1','2','3','4','2']))'''