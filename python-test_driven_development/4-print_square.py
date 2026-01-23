#!/usr/bin/python3
"""
This module provides a function that prints a square with '#'.

The size must be a non-negative integer.
"""


def print_square(size):
    """
    Print a square of size 'size' using '#'.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
