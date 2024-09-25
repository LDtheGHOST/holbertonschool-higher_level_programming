#!/usr/bin/python3
"""
    Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle. """
    def __init__(self, size):
        """
        Initializes a Square instance.
        Arguments:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size                    # Private attribute for size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)