#!/usr/bin/python3
""" Module providing a definition of
    class named 'Square'
"""


class Square:
    """ Actual definition of the class 'Square'
    Note:
    The size attribute is a private instance attribute.
    """
    def __init__(self, size):
        self.__size = size
