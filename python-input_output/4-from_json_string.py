#!/usr/bin/python3
"""Module that provides a function to return an object from a JSON string."""


import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string."""
    return json.loads(my_str)
