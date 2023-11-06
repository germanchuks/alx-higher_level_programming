#!/usr/bin/python3
"""Module for Square inherited from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square and inherits from the Rectangle class.

    Attributes:
        None

    Methods:
        __init__(self, size: Initializes a new Square instance.

    Args:
        size (int): The length of a side of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The lenght of a side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
