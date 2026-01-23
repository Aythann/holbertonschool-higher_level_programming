#!/usr/bin/python3
"""
This module provides a function that adds 2 integers.

Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """
    Add two numbers and return an integer result.

    a and b must be integers or floats. Floats are cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
