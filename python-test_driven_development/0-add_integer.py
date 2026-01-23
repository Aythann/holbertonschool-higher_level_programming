#!/usr/bin/python3
"""
This module provides a function that adds two numbers.

It validates inputs and returns the integer addition result.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return an integer.

    a and b must be integers or floats (floats are cast to ints).
    """
    if type(a) not in (int, float) or type(a) is bool:
        raise TypeError("a must be an integer")
    if type(b) not in (int, float) or type(b) is bool:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
