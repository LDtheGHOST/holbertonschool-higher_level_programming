#!/usr/bin/python3
"""
    File function for matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists of int or float): List of elements matrix.
        div (int or float): Divider of each element.

    Returns:
        list of lists of float: New matrix list with each element divided
        by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
        or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    new_matrix = []
    row_length = 0

    msg_size = "Each row of the matrix must have the same size"

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(msg_type)

        if row_length != 0 and len(row) != row_length:
            raise TypeError(msg_size)

        for num in row:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        row_length = len(row)

    new_m = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(new_m)
