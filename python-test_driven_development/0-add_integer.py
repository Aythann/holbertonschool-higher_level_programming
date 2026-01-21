#!/usr/bin/python3
"""
This module contains a function that adds two numbers.

The function ensures both arguments are integers or floats,
casts floats to integers, and raises TypeError when needed.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return the integer result.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if b is not an integer or float

    Returns:
        int: the addition of a and b after casting to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
