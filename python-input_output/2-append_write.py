#!/usr/bin/python3
"""Module containing the append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and returns the number
    of characters added

    Agrs:
        filename (str, optional): name of the file
        text (str, optional): string of text to write to file

    returns:
        int: number of characters appended to file
    """
    count = 0
    with open(filename, 'a', encoding="utf-8") as file:
        """This method returns the number of characters appended to a file"""
        count = file.write(text)
    return count