#!/usr/bin/python3
"""Function to return an object (Python data structure) represented by
JSON string."""
import json


def from_json_string(my_str):
    """
    This function returns an object represented by a JSON string.

    Args:
        my_str (str): A JSON string representing a Python object.

    Returns:
        object: A Python data structure represented by the input JSON string.
    """
    return json.loads(my_str)
