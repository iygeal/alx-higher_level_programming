#!/usr/bin/python3
"""
Module to return an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to an object.

    Returns:
        obj: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
