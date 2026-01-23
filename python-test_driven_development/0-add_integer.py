#!/usr/bin/python3
"""
This module provides a function that adds two numbers.

The function validates inputs (int/float only), casts floats to int,
and returns the integer addition result.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return an integer result.

    Args:
        a (int or float): first number
        b (int or float): second number (default: 98)

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if b is not an integer or float

    Returns:
        int: int(a) + int(b)
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
