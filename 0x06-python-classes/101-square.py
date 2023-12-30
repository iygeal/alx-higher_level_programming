#!/usr/bin/python3
"""
Module providing a definition of
class named 'Square' with two private instance attributes
size and position
"""


class Square:
    """
    Square class definition
    Attributes:
    - size (int): The size of the square. Defaults to 0.
    - position (tuple): The position of the square. Also defaults to 0.
    Raises:
    - TypeError: If size is not an integer
    - ValueError: If size is less than 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

        Args:
            value (int): The new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square
        Returns:
        - tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square

        Args:
            value (tuple): The new position value
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive intgeres")
        else:
            self.__position = value

    def area(self):
        """
        Computes and returns the area of the square
        Returns:
        - int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using # and the specified position
        If size is equal to 0, print empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size, end="")
            print()

    def __str__(self):
        """
        Returns a string represenation of the square
        Returns:
        - str: A string representation of the square
        """
        result = []
        for _ in range(self.__position[1]):
            result.append("\n")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
            result.append("\n")
        return "".join(result)
