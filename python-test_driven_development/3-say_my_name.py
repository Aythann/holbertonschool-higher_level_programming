#!/usr/bin/python3
"""
This module provides a function that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>".

    Raises:
        TypeError: if first_name or last_name is not a string
        ValueError: if first_name is an empty string
    """
    if first_name == "":
        raise ValueError("first_name must be a string")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
