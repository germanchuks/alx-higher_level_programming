#!/usr/bin/python3
"""Function to insert text fo file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing a specific
    string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    temp_lines = []
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            temp_lines.append(line)
            if search_string in line:
                temp_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.writelines(temp_lines)
