#!/usr/bin/python3
"""
This module provides a function that prints a full name.

It validates that first_name and last_name are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Print: My name is <first_name> <last_name>.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
