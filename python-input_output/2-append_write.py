#!/usr/bin/python3
"""
    File function for append_write().
"""


def append_write(filename="", text=""):
    """
        Appends a string at the end and returns number of characters added.
        Arguments:
            filename (str): File to write.
            text (str): Text to add.
    """
    count = 0
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
