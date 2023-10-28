#!/usr/bin/python3
"""Module for printing a square with character #"""


def print_square(size):
    """
    Prints a square with the character #.

    This function prints a square of a specified `size` using the character #.
    A TypeError is raise if `size` is not an int or `size` is a negative float.
    If `size` is less than zero, a ValueError is raised.

    Parameters:
        size (int): The size length of the square.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#" * size) for _ in range(size)]
