#!/usr/bin/python3
"""
Module that defines the BaseGeometry class method to validate integer values
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    SubClass that defines a rectangle
    """

    def __init__(self, width, height):
        """
        Initialize rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height
