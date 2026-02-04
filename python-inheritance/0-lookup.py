#!/usr/bin/python3
"""
Module that list all variable attributes and methods
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    Args:
        obj: Object

    Returns:
        The list of the names of available attributes and methods.
    """
    return dir(obj)
