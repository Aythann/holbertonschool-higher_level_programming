#!/usr/bin/python3


"""This module defines a function that write inside of a file."""


def write_file(filename="", text=""):
    """
	Function that write text inside of filename
	"""
    with open(filename, 'w') as file:
        len_file = file.write(text)
        return len_file
