#!/usr/bin/python3
"""
This module provides a function that prints a full name.

The function validates that the provided first and last names
are strings and prints the formatted sentence accordingly.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted name using the provided first and last names.

    Args:
        first_name (str): the first name to print
        last_name (str): the last name to print (default is an empty string)

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
