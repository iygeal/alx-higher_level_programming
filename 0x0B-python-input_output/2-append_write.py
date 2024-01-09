#!/usr/bin/python3
"""
Module to append a string to the end of a text file (UTF8) and return the
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the
    number of characters added.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_chars_added = file.write(text)

    return num_chars_added
