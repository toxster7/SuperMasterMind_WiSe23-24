import pytest
import sys
sys.path.append('../wise23-24_superhirn_25/')
from player.Rater import BotRater

def test_giveFeedback_rater1() -> None:
    rater = BotRater(5,6)
    feedback = rater.giveFeedback([3,4,3,2,1],[1,3,5,2,4])
    assert feedback == ["8","7","7","7","0"]

def test_giveFeedback_rater2() -> None:
    rater = BotRater(5,6)
    feedback = rater.giveFeedback([2,2,2,2,2],[1,3,5,9,4])
    assert feedback == ["0","0","0","0","0"]

def test_giveFeedback_rater3() -> None:
    rater = BotRater(5,6)
    feedback = rater.giveFeedback([6,6,6,6,6],[1,3,5,9,4])
    assert feedback == ["0","0","0","0","0"]



def test_minimize_maximums() -> None:
    rater = BotRater(5,6)
    max = rater.possible_codes.copy()
    rater.minimize_maximums([1,2,2,4,5],["0","0","0","0","0"])
    assert len(rater.possible_codes) < len(max)



def test_rater_1() -> None:
    rater = BotRater(5,6)
    guesses = []
    feedbacks = []

    for _ in range(10):
        guess = rater.rate(guesses, feedbacks)
        feedback = rater.giveFeedback([3,4,3,2,1], list(guess).copy())
        guesses.append(guess)
        feedbacks.append(feedback)


    assert sum(list(map(int, feedbacks[0]))) < sum(list(map(int, feedbacks[1])))

    



    

    



'''def test_rate() -> None:
    rater = BotRater(5,6)
    guesses = []
    feedbacks = []

    for _ in range(10):
        guess = rater.rate(guesses,feedbacks)
        feedback = rater.giveFeedback([5,3,3,5,1],list(guess).copy())
        guesses.append(guess)
        feedbacks.append(feedback)

    assert feedback[0:3] == ["8","8",""]   ''' 

     

