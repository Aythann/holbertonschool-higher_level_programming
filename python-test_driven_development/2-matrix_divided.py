#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.

The function validates the matrix and divisor, divides each element by
the given number, and returns a new matrix with rounded values.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    The result of each division is rounded to 2 decimal places.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Raises:
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to zero
        TypeError: if matrix is invalid

    Returns:
        list of lists: new matrix with divided values
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix == []:
        raise ValueError(msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)

    return [[round(i / div, 2) for i in row] for row in matrix]
