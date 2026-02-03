#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using validated width and height."""

    def __init__(self, width, height):
        """Initializes a rectangle with validated positive integer width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
