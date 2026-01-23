#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists of integers or floats.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and return a new matrix.

    Each element is rounded to 2 decimal places.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or matrix == []:
        raise TypeError(err)

    if type(div) not in (int, float) or type(div) is bool:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = None
    new = []

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(err)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for x in row:
            if type(x) not in (int, float) or type(x) is bool:
                raise TypeError(err)
            new_row.append(round(x / div, 2))
        new.append(new_row)

    return new
