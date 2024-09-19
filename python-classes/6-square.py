#!/usr/bin/python3
"""
This is class Square that defines a square
"""


class Square():
    """
    Return: a empty class square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num_i, int) for num_i in value) or
                not all(num_i >= 0 for num_i in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print('')
            return
        for _ in range(self.__position[1]):
            print('')
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)