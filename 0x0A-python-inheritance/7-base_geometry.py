#!/usr/bin/python3
"""Module for base geometry"""


class BaseGeometry:
    """
    Base class for geometry operations.

    Attributes:
        None

    Methods:
        area(self): Placeholder method to be implemented by for calculating
        the area.

        integer_validator(self, name, value): Validates if a given value is a
        positive integer.
    """
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
