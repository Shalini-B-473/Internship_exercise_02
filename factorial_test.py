'''Code to test factorial function'''
'''Built using pytest'''
import pytest
from factorial_code import *
def test_zero():
    assert factorial(0) == 1
def test_factorial_one():
    assert factorial(1) == 1
def test_factorial_five():
    assert factorial(5) == 120
def test_factorial_large():
    assert factorial(10) == 3628800

def test_factorial_large_num():
    delta = 1e90  # max difference
    assert factorial(50) == pytest.approx(3.0414093e+64,  rel=delta)

def test_factorial_string():  #For strings and whitespaces
    assert factorial("an") == "Factorial can only be computed for positive real numbers and zero"

def test_factorial_string_number():
    assert factorial("5") == "Factorial can only be computed for positive real numbers and zero"
    
def test_factorial_decimal():
    assert factorial(4.5) == pytest.approx(52.34277778455352, rel=1e-10)
    
def test_factorial_zero_decimal():
    assert factorial(0.0) == 1

def test_factorial_negative_zero():
    assert factorial(-0) == 1

def test_factorial_negative_num():
    assert factorial(-15) == "Factorial for a negative number is not defined"

def test_factorial_negative_decimal():
    assert factorial(-2.5) == "Factorial for a negative number is not defined"


