#!/usr/bin/python3
""" Module providing a definition of
    class named 'Square'
"""


class Square:
    """
    Square class with a private instance attribute size.

    Attributes:
    - size (int): The size of the square. Defaults to 0.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square. Defaults to 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
