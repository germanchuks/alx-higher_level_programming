#!/usr/bin/python3
"""Module for a Square"""


class Square:
    """
    This class represents a square.

    A square is a geometric shape with four equal sides and four right angles.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the
        given side length.

    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square. It must be a positive
            integer value.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
