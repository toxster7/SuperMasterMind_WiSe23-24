import sys
sys.path.append('../wise23-24_superhirn_25/')

class Runde:

    def __init__(self,code ,feedback) -> None:
        self.code = code
        self.feedback = feedback

class Feedback:

    def __init__(self, nRightColorRightPosition, nRightColor) -> None:
        self.nRightColorRightPosition = nRightColorRightPosition
        self.nRightColor = nRightColor

class Code:
    
    def __init__(self, code_string) -> None:
        pass