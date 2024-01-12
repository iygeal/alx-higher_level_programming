#!/usr/bin/python3
"""
Module for the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class which inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the Rectangle
            height (int): height of the Rectangle
            x (int): X-cordinate of the Rectangle. Defaults to 0.
            y (int): Y-cordinate of the Rectangle. Defaults to 0.
            id (int): An integer identity of the new Rectangle;
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width private attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set value for the width private attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value for height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value for the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value for y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method to return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Public method to display the Rectangle using '#' characters"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args):
        """Public method to update attributes using no-keyword arguments"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

    def __str__(self):
        """String representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )