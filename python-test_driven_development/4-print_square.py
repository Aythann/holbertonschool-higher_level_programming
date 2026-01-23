#!/usr/bin/python3
"""
This module provides a function that prints a square with '#'.

The size must be a non-negative integer.
"""


def print_square(size):
    """
    Print a square of size using the character '#'.
    """
    if type(size) is bool or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
