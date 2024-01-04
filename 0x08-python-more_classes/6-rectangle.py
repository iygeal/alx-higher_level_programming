#!/usr/bin/python3
"""Module that gives real definition of a class Rectangle"""


class Rectangle:
    """The definition of class Rectangle"""

    #  Public class attribute initialized to 0
    number_of_instances = 0

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
        #  Increment number_of_instances during new instance instantiation
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Public method that computes the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public method that computes the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of the rectangle for str() and print()"""
        if self.__width == 0 or self.__height == 0:
            return ""
        my_rect = ""
        #  Loop through each row except the last one
        for row in range(self.__height - 1):
            my_rect += "#" * self.__width + "\n"
        #  Add the last row without a newline character
        my_rect += "#" * self.__width
        return my_rect

    def __repr__(self):
        """String representation of the rectangle for repr()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method that prints a farewell message
        when an objected is deleted
        """
        print("Bye rectangle...")

        # Decrement number_of_instances during instance deletion
        Rectangle.number_of_instances -= 1
