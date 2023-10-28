#!/usr/bin/python3
"""Module for Text Indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    This function takes a string 'text' and prints it with two new lines after
    each occurrence of these characters: ., ? and :. There are no spaces at
    the beginning or end of each printed line.

    Parameters:
        text (str): The text to be printed with indentation.

    Raises:
        TypeError: If 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = []
    current_line = ""

    for i in text:
        current_line += i
        if i in '.?:':
            formatted_text.append(current_line.strip())
            formatted_text.append("")
            current_line = ""

    if current_line:
        formatted_text.append(current_line.strip())

    for i in formatted_text:
        print(i)
