#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A custom list class that can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it."""
        print(sorted(self))
