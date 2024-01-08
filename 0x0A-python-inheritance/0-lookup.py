#!/usr/bin/python3

"""Module providing a function to lookup attributes
and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        list: A list of strings representing the attributes
              and methods of the object.

    """
    return dir(obj)
