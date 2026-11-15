#!/usr/bin/python3
"""Module that defines matrix_divided, which divides all matrix elements."""


def matrix_divided(matrix, div):
    """Return a new matrix with every element of matrix divided by div.

    Each result is rounded to 2 decimal places.

    Args:
        matrix (list of lists of int or float): the matrix to divide.
        div (int or float): the divisor.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
            if its rows don't all have the same size, or if div is not
            a number.
        ZeroDivisionError: if div is 0.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) and len(row) > 0
                    for row in matrix) or
            not all(isinstance(n, (int, float))
                    for row in matrix for n in row)):
        raise TypeError(message)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
