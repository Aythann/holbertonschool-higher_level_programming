#!/usr/bin/python3
"""Module that provides a function to return the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string)

    Args:
        my_obj: The object to convert to a JSON string

    Returns:
        str: The JSON representation of the object
    """
    return json.dumps(my_obj)
