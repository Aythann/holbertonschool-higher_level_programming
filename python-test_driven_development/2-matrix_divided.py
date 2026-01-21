#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists containing integers or floats,
and all rows must have the same size.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Each element of the matrix is divided by div and rounded to
    two decimal places.

    Args:
        matrix (list of lists): matrix containing integers or floats
        div (int or float): number used to divide the matrix elements

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if each row of the matrix does not have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to zero

    Returns:
        list of lists: a new matrix with the divided values
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    if row_length == 0:
        raise TypeError(error_msg)

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
