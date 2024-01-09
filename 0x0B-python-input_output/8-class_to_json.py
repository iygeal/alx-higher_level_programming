#!/usr/bin/python3
"""
Module to define a function for JSON serialization of a class instance.
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of a class instance
    for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Create a dictionary to store serializable attributes
    serializable_dict = {}

    for key, value in attributes.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
