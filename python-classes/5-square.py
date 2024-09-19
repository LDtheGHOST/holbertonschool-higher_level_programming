#!/usr/bin/python3
"""
This is class Square that defines a square
"""


class Square():
    """
    Return: a empty class square
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        """
        area = self.__size
        return area * self.__size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print('\n')
            return
        for _ in range(self.__size):
            print('#' * self.__size)