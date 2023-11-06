#!/usr/bin/python3
"""Function to check if an object is of a specified class or a subclass"""


def is_kind_of_class(obj, a_class):
    """
    This function determines whether the given object is an instance of the
    specified class or any of its subclasses.

    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if the object is an instance of the specified class or any of its
    subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
