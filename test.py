import pytest
from factorial import factorial

def test_factorial_1():
    assert factorial(0)==1
def test_factorial_2():
    assert factorial(1)==1
def test_factorial_3():
    assert factorial(2)==2
def test_factorial_4():
    assert factorial(3)==6
def test_factorial_5():
    assert factorial(5)==121
def test_factorial():
    assert factorial(4) == 24
