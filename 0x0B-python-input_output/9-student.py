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
        to_json(obj): Returns the dictionary description of an object for JSON
        serialization.

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

    def to_json(obj):
        """
        This function returns the dictionary description of an object for JSON
        serialization.

        Args:
            obj: An instance of a Class.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        return (obj.__dict__)
