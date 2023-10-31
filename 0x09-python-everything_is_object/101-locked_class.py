#!/usr/bin/python3
"""Low memory cost module"""


class LockedClass:
    """
    This class restricts the creation of new instance attributes.

    Instances of this class can only have the attributes specified in
    `__slots__`, and any attempt to create new attributes will result in an
    AttributeError.

    Attributes:
        first_name (str): The allowed instance attribute for the first name.
    """
    __slots__ = ('first_name')
