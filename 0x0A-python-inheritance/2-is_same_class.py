#!/usr/bin/python3
"""Function to check object class"""


def is_same_class(obj, a_class):
    """
    Checks if an object belongs to a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class,
        False otherwise.
    """
    return (type(obj).__name__ == a_class.__name__)
