#!/usr/bin/python3
"""
This module provides a function that prints a text with indentation.

It prints 2 new lines after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = ".?:"
    buff = ""

    for ch in text:
        buff += ch
        if ch in special:
            print(buff.strip())
            print()
            buff = ""

    if buff.strip():
        print(buff.strip(), end="")
