import argparse
import time

import sys

from termcolor import cprint
sys.path.append('../wise23-24_superhirn_25/')

from gui.Menu import Menu
from gui.Spielfeld import Spielfeld
from player.Coder import *
from player.Rater import *


"""
    diese klasse dient dazu die unterschiedliche menüs anzuzeigen,
    welche der user durchlafen muss.
    des weiteren, nimmt diese klasse eingaben des nutzer entgegen,
    die für das spiel notwendig sind
    
    @authro: Anton, Florian 
"""

class Supermastermind:

    def __init__(self) -> None:
        self.id = None
        self.guesses = []
        self.feedbacks = []
        self.rater = None
        self.coder = None
        self.spielfeld = Spielfeld()
        self.menu = Menu()
        self.laeuft = False
        self.gameLoop()
        self.settings = None
        self.code = None

    def resetGame(self) -> None:
        self.guesses = []
        self.rater = None
        self.coder = None
        self.laeuft = False

    def __createCoderBotAndHumanGuesser__(self) -> None:
        self.coder = BotCoder(self.settings["anzahl_pos"])
        self.rater = HumanRater(self.settings["anzahl_pos"])
       

    def __createCoderHumanAndBotGuesser__(self) -> None:
        self.coder = HumanCoder(self.settings["anzahl_pos"])
        self.rater = BotRater(self.settings["anzahl_pos"])
       

    def gameLoop(self) -> None:
        
        while (True):           
            try:
                self.menu.runMenus()
            except KeyboardInterrupt as key_inter:
                print()
                cprint( "\t\t\t[-] Immer diese Interrupts :(", "red" )
                cprint( "\t\t\t[+] Exiting...", "green" )
                sys.exit(0)
            #Set Game Settings
            self.settings = self.menu.handler.getUserInput()
            if(self.settings["guesser"]):
                self.__createCoderBotAndHumanGuesser__()
            else:
                self.__createCoderHumanAndBotGuesser__()
            
            self.code = self.coder.createCode()
            self.guesses = []
            self.feedbacks = []

            for i in range(10):
                
                #show intial board
                self.spielfeld.showGamefield( self.settings["anzahl_pos"], self.code ,self.settings["guesser"], self.guesses, self.feedbacks)
                
                #let guesser guess
                guess = self.rater.rate(None)
                
                #show board after guess
                self.guesses.append(guess)
                self.feedbacks.append([0 for _ in range(int(self.settings["anzahl_pos"]))])
                self.spielfeld.showGamefield( self.settings["anzahl_pos"], self.code ,self.settings["guesser"], self.guesses, self.feedbacks)
                
                #give feedback
                feedback = self.coder.giveFeedback()
                
                #show board after feedback
                self.feedbacks[i] = feedback
                self.spielfeld.showGamefield( self.settings["anzahl_pos"], self.code ,self.settings["guesser"], self.guesses, self.feedbacks)

                feedback_correct = self.rater.bewerteFeedback(None)

                
                '''
                print(f"Versuch: {guess}")
                print(f"Feedback:{feedback}")
                print(f"Feedback ok? {feedback_correct}")
                '''
                #self.spielfeld.showGamefield( self.settings["anzahl_pos"], self.code ,self.settings["guesser"], self.guesses, self.feedbacks)
                
                
            


sm = Supermastermind()
