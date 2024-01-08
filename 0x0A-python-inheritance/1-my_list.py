#!/usr/bin/python3

"""Module providing a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list in sorted (ascending) order."""
        print(sorted(self))
