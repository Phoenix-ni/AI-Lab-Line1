import pytest
from calc import add
def test_add_postive():
    assert add(2,3) == 5

def test_add_zero():
    assert add(0,0) == 0

def test_add_negative():
    assert add(-1,-2) == -3
