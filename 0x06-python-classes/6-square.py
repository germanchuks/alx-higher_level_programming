#!/usr/bin/python3
"""Module for a Square"""


class Square:
    """
    This class represents a square.

    A square is a geometric shape with four equal sides and four right angles.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size, position): Initializes a new Square instance with
                                        the given size and position.
        area(self): Computes and returns the area of the square.
        my_print(self): Prints the square with the character #.

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square. It must be a positive
            integer value.
            position (tuple): The position of the square, represented as a
            tuple of two positive integers (horizontal, vertical).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter method for the size of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.

        Args:
            value (int): The new size to set for the square. It must be a
            positive integer value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for the position of the square.

        Args:
            value (tuple): The new size to set for the square. It must be
            tuple with two positive integers.

        Raises:
            TypeError: If the provided value is not a tuple of two positive
            integers.
        """
        if (not isinstance(value, tuple) or
           len(value) != 2 or not all(isinstance(i, int) for i in value) or
           not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return (self.__size ** 2)

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
