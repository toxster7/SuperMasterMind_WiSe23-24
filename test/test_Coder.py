import unittest
import pytest
import sys
sys.path.append('../wise23-24_superhirn_25/')
from player.Coder import BotCoder

'''class TestCoder(unittest.TestCase):

    def test_Botcoder(self):

        coder = BotCoder(4,5)
        self.assertEqual(coder.code_len, 4)
        self.assertEqual(coder.n_colors, 5)'''

def test_Botcoder_createCode() -> None:
    coder = BotCoder(4,5)
    assert coder.code_len == 4
    assert coder.n_colors == 5


def test_giveFeedback() -> None:
    coder = BotCoder(5,6)
    coder.code = [3,4,3,2,1]
    feedback = coder.giveFeedback([1,3,5,2,4])
    assert feedback == [8,7,7,7,0]


def test_giveFeedback_2() -> None:
    coder = BotCoder(5,6)
    coder.code = [2,2,2,2,2]
    feedback = coder.giveFeedback([3,2,5,2,4])
    assert feedback == [8,8,0,0,0]

def test_giveFeedback_2() -> None:
    coder = BotCoder(5,6)
    coder.code = [6,6,6,6,6]
    feedback = coder.giveFeedback([3,2,5,2,4])
    assert feedback == [0,0,0,0,0]    