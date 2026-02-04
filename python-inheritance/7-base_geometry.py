#!/usr/bin/python3
"""
Module that defines the BaseGeometry class
method to validate integer values
"""


class BaseGeometry:
    """
    Class that defineds the area() method
    """

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
