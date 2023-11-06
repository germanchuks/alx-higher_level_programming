#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Checks if an object inherits (directly or indirectly) from a specified
    class.

    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if the object is an instance of a class that inherits (directly or
    indirectly) from the specified class; otherwise, False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
