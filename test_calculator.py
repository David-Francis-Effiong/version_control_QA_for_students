# test_calculator.py
# Unit tests for calculator.py to demonstrate Quality Assurance (QA).

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    # Test that the add function works correctly
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    # Test that the subtract function works correctly
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    # Test that the multiply function works correctly
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_divide():
    # Test that the divide function works correctly
    assert divide(6, 2) == 3
    
    # Test that dividing by zero raises a ValueError
    with pytest.raises(ValueError):
        divide(5, 0)
