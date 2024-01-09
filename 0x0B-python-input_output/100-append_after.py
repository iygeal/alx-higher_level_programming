#!/usr/bin/python3
"""
Module to define the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for.
        new_string (str): The line of text to insert after each
        occurrence of the search string.

    Returns:
        None
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
