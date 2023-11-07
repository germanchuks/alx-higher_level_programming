#!/usr/bin/python3
"""Function to return dictionary description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """
    This function returns the dictionary description of an object for JSON
    serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing the object's attributes.
    """
    return (obj.__dict__)
