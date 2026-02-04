#!/usr/bin/python3
"""
Module that checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Return True or flase

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return type(obj) is a_class
