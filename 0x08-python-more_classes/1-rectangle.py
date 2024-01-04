#!/usr/bin/python3
"""Module that gives real definition of a class Rectangle"""


class Rectangle:
    """The definition of class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialization of private attributes of Rectangle

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        Raises:
        - TypeError: if value is not an integer
        - ValueError: if value is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
