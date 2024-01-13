#!/usr/bin/python3
"""
Module for class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class which inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor for the Square class

        Args:
            size (int_): Size of the Square
            x (int): X-coordinate. Defaults to 0.
            y (int): Y-coordinate. Defaults to 0.
            id (int): An integer identity of the new Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )