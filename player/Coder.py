from utils.Runde import Code
from utils.Runde import Feedback
from utils.Runde import Runde


class Coder:
    
    def __init__(self) -> None:
        self.code = None

    def createCode(self)->Code:
        pass

    def giveFeedback(self)->Feedback:
        pass

class BotCoder(Coder):

    def __init__(self) -> None:
        super().__init__()

    def createCode(self) -> Code:
        self.code = Code("1234")
        return self.code
    
    def giveFeedback(self)->Feedback:
        return Feedback(0, 0)
    
class HumanCoder(Coder):

    def __init__(self) -> None:
        super().__init__()

    def createCode(self) -> Code:
        return Code(input("Gib hier deinen Code ein: "))
    
    def giveFeedback(self) -> Feedback:
        return Feedback(0,0)

class NetCoder(Coder):

    def __init__(self, ip, port) -> None:
        super().__init__()
        self.ip = ip
        self.port = port

    

    