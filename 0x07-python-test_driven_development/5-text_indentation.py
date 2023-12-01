#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_index = 0

    while char_index < len(text) and text[char_index] == ' ':
        char_index += 1

    while char_index < len(text):
        print(text[char_index], end="")

        if text[char_index] in ".?:":
            print("\n")

        char_index += 1

        while char_index < len(text) and text[char_index] == ' ':
            char_index += 1
