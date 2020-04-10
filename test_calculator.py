import pytest
import calculator
#from calculator import add

def test_add(): 
    assert calculator.add(1, 1) == 2
def test_subtract():    
    assert calculator.subtract(10, 8) == 2
def test_multiply():    
    assert calculator.multiply(3, 3) == 9
def test_divide():
    assert calculator.divide(9, 3) == 3
        
