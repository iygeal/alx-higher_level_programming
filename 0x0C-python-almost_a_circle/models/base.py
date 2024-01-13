#!/usr/bin/python3
"""
Module that represents the Base class.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)