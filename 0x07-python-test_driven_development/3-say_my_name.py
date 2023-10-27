#!/usr/bin/python3
"""Module for printing name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a message saying 'My name is <first name> <last name>'.

    This function takes two string arguments, 'first_name' and 'last_name',
    and prints a message in the format 'My name is <first name> <last name>'.
    If 'first_name' or 'last_name' is not a string, it will raise a TypeError
    exception with the message 'first_name must be a string' or 'last_name must
    be a string'.

    Parameters:
        first_name (str): The first name to be included in the message.
        last_name (str, optional): The last name to be included in the message.
                                  Defaults to an empty string.

    Raises:
        TypeError: If 'first_name' or 'last_name' is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
