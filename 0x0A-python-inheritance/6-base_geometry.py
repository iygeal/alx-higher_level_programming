#!/usr/bin/python3

"""Module providing a class BaseGeometry with an area() method."""


class BaseGeometry:
    """A class with an unimplemented area() method."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
