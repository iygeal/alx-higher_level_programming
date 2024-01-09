#!/usr/bin/python3
"""
Module to read and print the content of a text file to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
