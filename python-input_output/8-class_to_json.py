#!/usr/bin/python3
"""Defines a function that returns the dictionary description for JSON serialization of an object."""
    

def class_to_json(obj):
    """Return the dictionary representation of a simple object for JSON serialization."""
    return obj.__dict__
