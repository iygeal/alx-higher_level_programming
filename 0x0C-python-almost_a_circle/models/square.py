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

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes based on *args and **kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
