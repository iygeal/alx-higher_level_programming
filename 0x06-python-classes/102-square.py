#!/usr/bin/python3
"""
Module that defines a class named Square
"""


class Square:
    """
    Definition of the class Square
    """
    def __init__(self, size=0):
        """
        Initialization of a Square instance

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square

        Args:
            value (int or float): The new size value
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for two squares based on area

        'other' is a reference to another object on the
        right-hand-side being compared to the current instance
        of the 'Square' class (self), on the left-hand-side.
        """
        if isinstance(other, Square):  # Assumes 'other' an instance of Square
            return self.area() == other.area()
        return False  # Return False if area of 'other' != self.area

    def __ne__(self, other):
        """
        Inequality comparison for two squares based on area
        """
        return not self.__eq__(other)  # != means True; so negate __eq__ method

    def __gt__(self, other):
        """
        Greater than comparison for two squares based on area
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented  # Indicates unsupported comparison

    def __ge__(self, other):
        """
        Greater than or equal comparison for two squares based on area
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Less than comparison for two squares based on area
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal comparsion of two squares based on area
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
