#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of a simple object."""
    return obj.__dict__
