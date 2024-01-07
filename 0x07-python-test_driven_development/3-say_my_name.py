#!/usr/bin/python3

"""
Module for saying a person's name.

This module defines the say_my_name function, which prints the person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the person's name.

    Args:
        first_name (str): First name of the person.
        last_name (str): Last name of the person.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name and first_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {}".format(first_name))
    else:
        print("My name is {}".format(last_name))
