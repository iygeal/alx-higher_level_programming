#!/usr/bin/python3
"""Module providing the MyInt class."""


class MyInt(int):
    """A class representing a rebel integer."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
