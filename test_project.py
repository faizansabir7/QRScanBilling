import pytest
from project import getcode,check,validatearg

def test_getcode():
    assert getcode('Image 2.jpeg') == '8906087471301'
    assert getcode('Image.jpeg') == None

def test_check():
    assert check('8902519002075') == 20
    assert check('123456') == False

def test_validatearg():
    assert validatearg('-a') == True
    assert validatearg('-b') == False