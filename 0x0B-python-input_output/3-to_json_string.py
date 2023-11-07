#!/usr/bin/python3
"""Function to return the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of the given object as a string.

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        str: A JSON string representing the input object.
    """
    return (json.dumps(my_obj))
