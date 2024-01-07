#!/usr/bin/python3
"""
This module implements a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Adds two numbers.

    Parameters:
    - a: An integer or float.
    - b: An integer or float (default is 98).

    Returns:
    int: The sum of a and b.
    """
    # Validate input types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if input is float
    a = int(a)
    b = int(b)

    # Perform addition and return the result
    return a + b
