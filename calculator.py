# calculator.py
# This file contains a simple calculator program to demonstrate CI and QA practices.

def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference when b is subtracted from a.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a divided by b.
    Raises ValueError if b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
