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
        area = self.__size
        return area * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value