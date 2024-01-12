#!/usr/bin/python3
"""
Module that represents the Base class.
"""


class Base:
    """
    The base calsss for managing id attribute in future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): An integer id. Defaults to None.
        Attributes:
        id (int): Public instance attribute for the object id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects