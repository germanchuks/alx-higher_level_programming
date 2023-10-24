#!/usr/bin/python3
"""Defines a MagicClass matching specified bytecode"""

import math


class MagicClass:
    """
    A class representing a Circle.

    Attributes:
        __radius (float): The radius of the Circle.

    Methods:
        __init__(self, radius=0):
            Initializes a MagicClass instance with an optional radius.

        area(self):
            Computes and returns the area of the Circle.

        circumference(self):
            Computes and returns the circumference of the Circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with an optional radius.

        Args:
            radius (float, optional): The radius of the Circle.

        Raises:
            TypeError: If the provided radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the Circle.

        Returns:
            float: The area of the Circle.
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        Computes and returns the circumference of the Circle.

        Returns:
            float: The circumference of the Circle.
        """
        return (math.pi * 2 * self.__radius)
