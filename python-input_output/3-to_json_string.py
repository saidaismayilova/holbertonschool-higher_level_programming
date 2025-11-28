#!/usr/bin/python3
"""
Returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """Converts an object to its JSON string representation"""
    import json
    return json.dumps(my_obj)
