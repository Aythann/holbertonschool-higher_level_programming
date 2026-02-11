#!/usr/bin/python3
"""Module that provides a function to return a dictionary description of an object."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    return obj.__dict__
