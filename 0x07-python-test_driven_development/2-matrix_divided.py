#!/usr/bin/python3

"""
Module for matrix division.

This module defines the matrix_divided function, which divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int or float): Number to divide the matrix elements by.

    Returns:
        list: New matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists,
                    or if elements are not integers or floats.
        TypeError: If matrix rows have different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Validate input types
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Validate matrix rows have the same size
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix elements and round to 2 decimal places
    result_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return result_matrix
