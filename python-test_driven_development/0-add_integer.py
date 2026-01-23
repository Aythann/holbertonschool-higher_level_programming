#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The function checks that both arguments are integers or floats,
casts floats to integers, and returns their sum.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return an integer.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the sum of a and b
    """
    if a == "":
        raise ValueError("a must be an integer")
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
