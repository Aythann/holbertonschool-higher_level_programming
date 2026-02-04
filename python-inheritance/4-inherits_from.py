#!/usr/bin/python3
"""
Module to check if if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns true or false

    Args:
        obj: obj to check
        a_class: the classe to compare
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
