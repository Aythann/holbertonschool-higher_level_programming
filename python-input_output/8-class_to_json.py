#!/usr/bin/python3
"""Module that provides a function to return a dictionary description of an object."""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: The object to be converted to a dictionary

    Returns:
        A dictionary representation of the object
    """
    return obj.__dict__
