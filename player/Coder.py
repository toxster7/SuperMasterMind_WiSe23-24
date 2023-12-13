import random
import sys
sys.path.append('../wise23-24_superhirn_25/')

from ourUtils.InputHandler import *


class Coder:
    
    def __init__(self, code_len) -> None:
        self.code = None
        self.code_len = code_len

    def createCode(self)->list:
        pass

    def giveFeedback(self)->list:
        pass




class BotCoder(Coder):

    def __init__(self,code_len) -> None:
        super().__init__(code_len)

    def createCode(self) -> list:
        self.code = [random.randint(1, 8) for _ in range(int(self.code_len))]
        return self.code
    
    def giveFeedback(self)->list:
        return [random.randint(7, 8) for _ in range(int(self.code_len))]
    
class HumanCoder(Coder):

    def __init__(self, code_len) -> None:
        super().__init__(code_len)
        self.handler = InputHandler()
        

    def createCode(self) -> list:
        return self.handler.getCodeInput(self.code_len)
    
    def giveFeedback(self) -> list:
        return self.handler.getFeedback(self.code_len)

class NetCoder(Coder):

    def __init__(self, ip, port) -> None:
        super().__init__()
        self.ip = ip
        self.port = port

    

    