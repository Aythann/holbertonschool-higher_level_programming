#!/usr/bin/python3
"""
Module that defines a list subclass in sorted order
"""


class MyList(list):
    """
    Class inheriting from list
    """

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
