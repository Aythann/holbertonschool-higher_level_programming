#!/usr/bin/python3
"""
This module provides a function that prints a text with indentation.

It prints 2 new lines after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str) or text == "":
        raise TypeError("text must be a string")

    special = ".?:"
    buffer = ""

    for char in text:
        buffer += char
        if char in special:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip(), end="")
