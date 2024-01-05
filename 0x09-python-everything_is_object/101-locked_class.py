#!/usr/bin/python3
"""
Module containing the LockedClass class, which restricts attribute creation.
"""


class LockedClass:
    """
    A class that prevents the user from dynamically creating
    new instance attributes, except for the 'first_name' attribute.
    """
    __slots__ = 'first_name'
    #  The __slots__ attribute specifies a tuple of allowed attribute names.
    #  In this case, only 'first_name' is allowed.
