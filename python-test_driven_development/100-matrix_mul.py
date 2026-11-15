#!/usr/bin/python3
"""Module that defines matrix_mul, which multiplies two matrices."""


def _check(matrix, name):
    """Validate one operand of matrix_mul.

    Args:
        matrix: the value to check.
        name (str): the name used in error messages (m_a or m_b).

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
            whose rows all have the same size.
        ValueError: if matrix is empty.
    """
    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("{} must be a list of lists".format(name))
    if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
        raise ValueError("{} can't be empty".format(name))
    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise TypeError(
            "{} should contain only integers or floats".format(name))
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(
            "each row of {} must be of the same size".format(name))


def matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Args:
        m_a (list of lists of int or float): the first matrix.
        m_b (list of lists of int or float): the second matrix.

    Raises:
        TypeError: if an argument is not a valid matrix.
        ValueError: if an argument is empty, or if the number of columns
            of m_a is not the number of rows of m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    _check(m_a, "m_a")
    _check(m_b, "m_b")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(row[k] * m_b[k][j] for k in range(len(m_b)))
             for j in range(len(m_b[0]))] for row in m_a]
