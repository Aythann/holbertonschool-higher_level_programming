#!/usr/bin/python3
"""
This module provides a function that prints text with indentation.

It prints two new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        # skip leading spaces of the line
        while i < n and text[i] == ' ':
            i += 1
        if i >= n:
            break

        line = ""
        while i < n and text[i] not in ".?:":
            line += text[i]
            i += 1

        if i < n and text[i] in ".?:":
            line += text[i]
            i += 1
            print(line.strip())
            print()
            # skip spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
        else:
            print(line.strip(), end="")
