#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initialize data.

        Args:
            size (int, optional): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the current square area."""
        return self.__size * self.__size
