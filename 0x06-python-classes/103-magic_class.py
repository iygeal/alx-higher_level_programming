#!/usr/bin/python3
"""
Module of class named "MagicClass" which replicates a bytecode
with circle methods
"""
import math


class MagicClass:
    """
    Definition of the class 'MagicClass'
    """

    def __init__(self, radius=0):
        """
        Initialization of a MagicClass instance

        Args:
            radius (float): The radius of a circle. Defaults to 0.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates and returns the circumfereence of the cicle
        """
        return 2 * math.pi * self.__radius
