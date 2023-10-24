#!/usr/bin/python3
"""Module for a Square"""


class Square:
    """
    This class represents a square.

    A square is a geometric shape with four equal sides and four right angles.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the
        given size.

    """
    def __init__(self, size):
        self.__size = size
