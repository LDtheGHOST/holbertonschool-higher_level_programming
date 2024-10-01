#!/usr/bin/python3
"""Module defines the read_file function"""


def read_file(filename=""):
    """Reads a file and prints to stdout

    Args:
        filename (str, optional): name of file to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')