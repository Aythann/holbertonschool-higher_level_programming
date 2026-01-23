#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists of integers or floats and all rows
must have the same size. The function returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and return a new matrix.

    Args:
        matrix (list of lists): list of lists of ints/floats
        div (int or float): divisor (must not be 0)

    Raises:
        TypeError: if matrix is not a valid matrix of numbers
        TypeError: if rows do not have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        list of lists: new matrix with values divided and rounded to 2 decimals
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or matrix == []:
        raise TypeError(err)

    if type(div) not in (int, float) or type(div) is bool:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = None
    new_matrix = []

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(err)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for x in row:
            if type(x) not in (int, float) or type(x) is bool:
                raise TypeError(err)
            new_row.append(round(x / div, 2))

        new_matrix.append(new_row)

    return new_matrix
