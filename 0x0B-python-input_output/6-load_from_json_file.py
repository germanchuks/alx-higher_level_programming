#!/usr/bin/python3
"""Function to create an Object from a “JSON file."""
import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)
