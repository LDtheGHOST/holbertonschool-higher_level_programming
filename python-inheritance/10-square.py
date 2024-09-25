#!/usr/bin/python3
"""
    Class file for Square, which inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle. """
    def __init__(self, size):
        """
            Initialization of Square.
            Arguments:
                size (int): Size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            Return the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)