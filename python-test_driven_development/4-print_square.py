#!/usr/bin/python3
"""
This module provides a function that prints a square using '#'.

The size of the square must be a non-negative integer.
The function validates the input and prints the square line by line.
"""


def print_square(size):
    """
    Print a square of size 'size' using the character '#'.

    Args:
        size (int): the size of the square to print

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
