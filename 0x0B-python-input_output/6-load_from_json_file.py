#!/usr/bin/python3
"""
Module to create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        obj: The Python data structure represented by the JSON file.
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
