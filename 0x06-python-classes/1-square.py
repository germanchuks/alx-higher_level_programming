#!/usr/bin/python3
"""Module for a Square"""


class Square:
    """
    This class represents a square.

    A square is a geometric shape with four equal sides and four right angles.

    Attributes:
        size (int): The length of each side of the square.

    Methods:
        __init__(self, side_length): Initializes a new Square instance with the
        given side length.

    """
    def __init__(self, size):
        self.__size = size
