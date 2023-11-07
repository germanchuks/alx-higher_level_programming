#!/usr/bin/python3
"""Module that defines a student"""


class Student:
    """
    This class represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(attrs=None): Returns the dictionary description of an object
        for JSON serialization.
        reload_from_json(json): Updates the student attributes from a JSON
        dictionary.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function returns the dictionary description of an object for JSON
        serialization.

        Args:
            obj: An instance of a Class.
            attrs: A list of strings containing attributes names to be
            retrieved.

        Returns:
            dict: A dictionary containing only object's attributes in
            attrs if attrs is not None, otherwise returns all attributes.
        """
        if attrs:
            return ({attr: value for attr, value in self.__dict__.items()
                     if attr in attrs})
        return (self.__dict__)

    def reload_from_json(self, json):
        """
        Updates the student attributes from a JSON dictionary.

        Args:
            json (dict): A dictionary containing new student attributes.
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
