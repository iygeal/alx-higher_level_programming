#!/usr/bin/python3
""" Module providing a definition of
    class named 'Square'
"""


class Square:
    """
    Square class definition

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
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square
        Returns:
        - int: Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square
        Parameters:
        - Value (int): The new size value
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square
        Returns:
        - int: The area of current square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
