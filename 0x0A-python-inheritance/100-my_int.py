#!/usr/bin/python3
"""Module for MyInt that inherits from int."""


class MyInt(int):
    """
    Custom integer class that reverses the behavior of '==' and '!=' operators.

    Attributes:
        None

    Methods:
        __eq__(self, value): Custom implementation of the equality operator
        '=='.
        __ne__(self, value): Custom implementation of the inequality operator
        '!='.

    Args:
        value: The value to compare against.

    Returns:
        bool: True if the inverted comparison is satisfied, False otherwise.
    """

    def __eq__(self, value):
        """
        Custom implementation of the equality operator '=='.
        """
        return (self.real != value)

    def __ne__(self, value):
        """
        Custom implementation of the inequality operator '!='.
        """
        return (self.real == value)
