#!/usr/bin/python3
"""Module for Base"""
import json


class Base:
    """
    The Base class for all other classes.

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number of
        objects.
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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.
        """
        if not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))
