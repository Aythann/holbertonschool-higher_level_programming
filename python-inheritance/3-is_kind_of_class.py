#!/usr/bin/python3
"""
Module that check if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true or false

    Args:
    obj : Object to check
    a_class : the class to compare
    """
    return isinstance(obj, a_class)
