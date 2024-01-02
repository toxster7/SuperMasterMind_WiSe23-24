import unittest
import pytest
import sys
sys.path.append('../wise23-24_superhirn_25/')
from ourUtils.Validator import *

def test_validate_code():
    val = Validator()
    code = [3,3,3,2,6]
    codeA = [3,3,'A',2,6]
    codeLang = [3,3,'A',2,6]
    assert not val.validateCode(code, 5, 6) 
    assert val.validateCode(code,5,5)
    assert val.validateCode(code,4,6)
    assert val.validateCode(codeA,5,6)
    assert val.validateCode(codeLang,5,6)

def test_validateFeedback():
    val = Validator()
    feedbackCor = [8,7,7,0,0]
    feedbackWro = [8,6,7,0,0]
    feedbackLong =[8,8,8,8,8,8]

    assert not val.validateFeedback(feedbackCor,5)
    assert val.validateFeedback(feedbackWro,5)
    assert val.validateFeedback(feedbackLong,5)