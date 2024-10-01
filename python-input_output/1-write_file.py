#!/usr/bin/python3
"""Module containing function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number
    of characters written

    Args:
        filename (str, optional): name of the file
        text (str, optional): string of text to write to file

    Returns:
        int: number of characters written to file
    """
    count = 0

    with open(filename, 'w', encoding="utf-8") as file:
        count = file.write(text)
    return count