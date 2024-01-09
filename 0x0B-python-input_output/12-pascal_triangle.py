#!/usr/bin/python3
"""
Module to define the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The level of Pascal's triangle.

    Returns:
        list of lists: Pascal’s triangle up to level n.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows of Pascal's triangle
    for i in range(1, n):
        # Use the previous row to generate the current row
        current_row = [1]
        for j in range(1, i):
            current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        current_row.append(1)

        triangle.append(current_row)

    return triangle
