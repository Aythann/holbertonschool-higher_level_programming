#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div (rounded to 2)."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    row_len = None
    new_matrix = []

    for row in matrix:
        if row_len is None:
            row_len = len(row)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
