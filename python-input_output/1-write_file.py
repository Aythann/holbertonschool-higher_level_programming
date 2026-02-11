#!/usr/bin/python3
"""
This module defines a function that writes text into a file.
"""


def write_file(filename="", text=""):
    """
    Function that writes text inside of filename.
    """
    with open(filename, 'w') as file:
        return file.write(text)
