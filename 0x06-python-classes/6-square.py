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
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or (
         any(i <= 0 or not isinstance(i, int) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
