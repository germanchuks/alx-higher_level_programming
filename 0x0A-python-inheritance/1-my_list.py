#!/usr/bin/python3
"""Module for MyList inherited from built-in list class"""


class MyList(list):
    """
    MyList is a custom list class that inherits from the built-in `list`
    class.

    Public Methods:
        - print_sorted(): Prints the elements of the list in ascending order.
    """
    def print_sorted(self):
        """
        Print the elements of the list in ascending order.
        """
        print(sorted(self))
