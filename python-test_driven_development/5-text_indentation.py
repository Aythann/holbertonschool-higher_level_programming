#!/usr/bin/python3
"""
This module provides a function that prints a text with indentation.

The function prints the text and adds two new lines after each of
these characters: '.', '?' and ':' while removing extra spaces after them.
"""


def text_indentation(text):
    """
    Print a text with two new lines after '.', '?' and ':'.

    Args:
        text (str): the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
