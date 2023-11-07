#!/usr/bin/python3
"""Function to write string to text file and return number of printed chars"""


def write_file(filename="", text=""):
    """
    This function writes the provided text to a text file (UTF8) and return
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
