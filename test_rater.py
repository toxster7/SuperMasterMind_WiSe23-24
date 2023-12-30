import math
import time
import pytest
from player.Rater import *
from player.Coder import *


@pytest.fixture
def initial_guesses4x4():
    guesses4x4 = [['1','1','1','1'],
                  ['1','2','2','2'],
                  ['1','2','3','4'],
                  ['4','2','3','1']
                  ]
    
    return guesses4x4

@pytest.fixture
def initial_feedbacks4x4():
    feedbacks4x4 = [['8','0','0','0'],
                  ['8','7','0','0'],
                  ['8,','7','7','7'],
                  ['8','8','7','7']
                  ]
    
    return feedbacks4x4

def test_bot_calculate_possible_codes():
    for i in [4,5]:
        for j in range(2,9):
            bot = BotRater(i,j)
            assert len(bot.possible_codes) == math.pow(j,i)

def test_bot_create_frist_guess():
    for i in [4,5]:
        for j in range(2,9):
            bot = BotRater(i,j)
            code = bot.rate([],[])
            assert len(code) == i
            for c in code:
                assert int(c) in range(1,j+1)

def test_bot_give_feedback():
    bot = BotRater(4,8)
    code4x8 = [5,7,3,5]
    guess1 = [5,5,5,5]
    guess2 = [5,3,4,3]
    guess3 = [6,4,1,1]
    guess4 = [5,7,3,5]

    assert bot.giveFeedback(code4x8, guess1) == ['8','8','0','0']
    assert bot.giveFeedback(code4x8, guess2) == ['8','7','0','0']
    assert bot.giveFeedback(code4x8, guess3) == ['0','0','0','0']
    assert bot.giveFeedback(code4x8, guess4) == ['8','8','8','8']

    bot = BotRater(5,8)
    code4x8 = [5,7,3,5,8]
    guess1 = [5,5,5,5,5]
    guess2 = [5,3,4,3,8]
    guess3 = [6,4,1,1,2]
    guess4 = [5,7,3,5,8]

    assert bot.giveFeedback(code4x8, guess1) == ['8','8','0','0','0']
    assert bot.giveFeedback(code4x8, guess2) == ['8','8','7','0','0']
    assert bot.giveFeedback(code4x8, guess3) == ['0','0','0','0','0']
    assert bot.giveFeedback(code4x8, guess4) == ['8','8','8','8','8']

def test_bot_create_second_guess():
    for i in [4,5]:
        for j in range(2,9):
            bot = BotRater(i,j)
            feedback = ['8']
            while len(feedback) < i:
                feedback.append('0')
            code = bot.rate([[str(1) for _ in range(i)]],[feedback])
            assert len(code) == i
            for c in code:
                assert int(c) in range(1,j+1)

def test_bot_minimize_possible_codes():    
    for i in [4,5]:
        for j in range(2,9):
            bot = BotRater(i,j)
            guess = [str(1) for _ in range(i)]
            feedback = [str(0) for _ in range(i)]
            bot.minimize_maximums(guess, feedback)
            for gcode in bot.possible_codes:
                for c in list(gcode):
                    assert c != 1


def test_code_erraten5x8():
    k = 0
    i = 0
    while k < 20:
        bot = BotRater('5','8')
        #print(bot.get_all_possible_codes())
        guess= [1,1,1,1]
        code = [(random.randint(2, 8)) for _ in range(5)]
        guesses = []
        feedbacks = []
        #print(bot.giveFeedback(code, [1,1,1,4]))

        for _ in range(10):
            start_time = time.time()
            guess = bot.rate(guesses, feedbacks)
            end_time = time.time()
            time_dif = end_time - start_time 
            assert (time_dif < 5.0)
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
            if(feedback == ['8', '8', '8', '8', '8']):
                i+=1
                break    

        k += 1
    assert i >= 19
    #print(bot.possible_codes) 
def test_code_erraten5x7():
    k = 0
    i = 0
    while k < 20:
        bot = BotRater('5','7')
        #print(bot.get_all_possible_codes())
        guess= [1,1,1,1]
        code = [(random.randint(2, 7)) for _ in range(5)]
        guesses = []
        feedbacks = []
        #print(bot.giveFeedback(code, [1,1,1,4]))

        for _ in range(10):
            start_time = time.time()
            guess = bot.rate(guesses, feedbacks)
            end_time = time.time()
            time_dif = end_time - start_time 
            assert (time_dif < 5.0)
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
            if(feedback == ['8', '8', '8', '8', '8']):
                i+=1
                break    

        k += 1
    assert i >= 20

        
def test_code_erraten4x8():
    k = 0
    i = 1
    while k <= 100:
        bot = BotRater('4','8')
        #print(bot.get_all_possible_codes())
        guess= [1,1,1,1]
        code = [(random.randint(2, 8)) for _ in range(4)]
        guesses = []
        feedbacks = []
        #print(bot.giveFeedback(code, [1,1,1,4]))

        for _ in range(10):
            start_time = time.time()
            guess = bot.rate(guesses, feedbacks)
            end_time = time.time()
            assert end_time -start_time < 3
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
                i+=1
                break    
                
        k += 1

    assert i >= 100
    #print(bot.possible_codes) 



