#!/usr/bin/python3
"""
    Class file for Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle. """
    def __init__(self, size):
        """
            Intialization of Square.
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
        return super().area()
