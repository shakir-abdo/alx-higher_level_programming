#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Modify a file by adding specified text after each line that contains a specified string.

    Parameters:
    filename (str): The name of the target file.
    search_string (str): The string to locate within the file.
    new_string (str): The text to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
