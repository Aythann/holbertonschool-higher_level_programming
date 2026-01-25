#!/usr/bin/python3
"""Defines a Square class with size validation and area computation."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
