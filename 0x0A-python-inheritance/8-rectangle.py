#!/usr/bin/python3
"""Module for Rectangle inherited from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle and inherits from the BaseGeometry class.

    Attributes:
        None

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        integer_validator(self, name, value): Validates that a value is a
        positive integer.
        area(self): Calculates the area of the rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Raises:
        TypeError: If 'width' or 'height' is not an integer.
        ValueError: If 'width' or 'height' is less than or equal to 0.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
