#!/usr/bin/python3
"""Module for adding two integers"""


def add_integer(a, b=98):
    """
    Add two integers and return the result.

    This function takes two integers or floats, 'a' and 'b', and returns
    their sum. If 'a' or 'b' is not an integer, it will be cast to an integer
    before adding.

    Parameters:
        a (int): The first integer to be added.
        b (int, optional): The second integer to be added. Defaults to 98.

    Returns:
        int: The sum of 'a' and 'b'.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
