#!/usr/bin/python3
"""
Module to define the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for.
        new_string (str): The line of text to insert after each
        occurrence of the search string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        # Read the existing content of the file
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            # Write the original line
            file.write(line)

            # If the search string is found in the line, append the new string
            if search_string in line:
                file.write(new_string + '\n')
