#!/usr/bin/python3
"""Module for Base"""


class Base:
    """
    The Base class for all other classes.

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number of
        objects.

    Methods:
        __init__(self, id=None): Initializes a new Base instance with an
        optional ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): An optional ID for the instance. If id is
            None, a unique ID is assigned based on the class attribute
            __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
