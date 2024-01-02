import sys
sys.path.append('../wise23-24_superhirn_25/')
from random import randint
import json

class Pseudoserver:

    def __init__(self) -> None:
        self.games = {}
        self.code = None
        self.n_colors = None
        self.code_len = None
    

    def createCode(self) -> list:
        self.code = [randint(1, int(self.n_colors)) for _ in range(int(self.code_len))]
        return self.code.copy()
    
    def calcFeedback(self, guess)->list:
        feedback = []
        temp_code = self.code.copy()
        #check for correct pos
        print(temp_code)
        print(guess)
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


    def createNewGame(self, json):
        self.n_colors = json["colors"]
        self.code_len = json["positions"]
        
        gameid = randint(1,999999)
        
        self.code = self.createCode()
        #strcode = "".join(code)
        self.games[gameid] = self.code

        response = json.copy()

        response["gameid"] = gameid      

        return response
    

    def giveFeedback(self, json):
        
        string = json["value"]
        codeToReview = [c for c in string]
        
        feedback = self.calcFeedback(codeToReview.copy())
        outstr = "".join([str(s) for s in feedback if s != 0])
       
        response = json.copy()

        response["value"] = outstr
        return response
        
    def respond(self, request):
        if (request["gameid"] == 0):
            return self.createNewGame(request)
        else:
            return self.giveFeedback(request)

'''
ps = Pseudoserver()

response = ps.respond({
  "colors": 4,
  "gameid": 0,
  "gamerid": "flrnbr",
  "positions": 4,
  "value": ""
})


print(ps.respond({
  "colors": 4,
  "gameid": response["gameid"],
  "gamerid": "flrnbr",
  "positions": 4,
  "value": "1432"
}))'''