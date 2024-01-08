#!/usr/bin/python3

"""Module providing a function to check if an object is exactly an instance
of the specified class.
"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class;
              otherwise, False.

    """
    return type(obj) == a_class
