#!/usr/bin/python3
"""Function to append string to end of a text file and return number of
printed characters"""


def append_write(filename="", text=""):
    """
    This function appends the provided string to the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
