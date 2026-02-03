#!/usr/bin/python3
"""Defines a base geometry class with area and integer validation."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
