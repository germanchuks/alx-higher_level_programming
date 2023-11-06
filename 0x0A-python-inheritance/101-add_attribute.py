#!/usr/bin/python3
"""Function to add a new attribute to an object."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute will be added.
        attribute (str): The name of the attribute to be added.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
