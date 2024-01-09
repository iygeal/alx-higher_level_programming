#!/usr/bin/python3
"""
Module to write a string to a text file (UTF8) and return the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the
    number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chars_written = file.write(text)

    return num_chars_written
