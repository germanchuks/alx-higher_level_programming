#!/usr/bin/python3
"""Function to read text file and print to stdout."""


def read_file(filename=""):
    """
    Reads and prints the contents of a text file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to be read. Default is an empty
        string.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as my_file:
        for line in my_file:
            print(line, end="")
