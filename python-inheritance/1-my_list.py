#!/usr/bin/python3
"""Module defines MyList class that inherits from list."""


class MyList(list):
    """Subclass of list with a method to print a sorted version."""

    def print_sorted(self):
        """Prints a sorted version of the list in ascending order."""
        print(sorted(self))
