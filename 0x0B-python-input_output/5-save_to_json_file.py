#!/usr/bin/python3
"""Function to write object to text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved as JSON.
        filename (str): The name of the file to which the JSON representation
        will be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
