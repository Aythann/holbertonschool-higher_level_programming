#!/usr/bin/python3
"""This module defines a function that writes a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of characters written."""
    with open(filename, 'w') as file:
        len_file = file.write(text)
        return len_file
