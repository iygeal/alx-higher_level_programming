#!/usr/bin/python3
"""Module providing the add_attribute function."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute is to be added.
        attribute (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
