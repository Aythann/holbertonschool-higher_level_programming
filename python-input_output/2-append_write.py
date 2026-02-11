#!/usr/bin/python3
"""
Modulo that appends text to the end of a file.
"""


def append_write(filename="", text=""):
    """
    Function that appends text at the end of filename.
    """
    with open(filename, "a") as file:
        return file.write(text)
