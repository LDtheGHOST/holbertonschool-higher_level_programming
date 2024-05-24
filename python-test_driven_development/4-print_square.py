#!/usr/bin/python3
"""
   Function file for print_square.
"""

def print_square(size):
    """
        Prints a square with the character #.
        Arguments:
            size (int): Size of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):                                                                                    print(size * "#")
