#!/usr/bin/python3
"""
Defines lookup function for an object attribute.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    This function takes an object as an argument and returns a list of
    attribute names and method names associated with that object.

    Args:
        obj: The object (e.g., class) to be checked.

    Returns:
        A list containing the names of attributes and methods associated with
        the object provided.
    """
    return (dir(obj))
