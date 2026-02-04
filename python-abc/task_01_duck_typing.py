#!/usr/bin/env python3
"""
Task 01: Shapes, Interfaces, and Duck Typing.

Defines an abstract Shape with area and perimeter, plus Circle and Rectangle
implementations. Provides shape_info() relying on duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        raise NotImplementedError


class Circle(Shape):
    """Concrete circle shape."""

    def __init__(self, radius):
        """Initialize a Circle with a positive numeric radius."""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete rectangle shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with positive numeric width and height."""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if width < 0:
            raise ValueError("width must be non-negative")
        if height < 0:
            raise ValueError("height must be non-negative")
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape-like object (duck typing).

    The object is expected to provide .area() and .perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
