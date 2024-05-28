#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """
        Defines class
    """

    def __init__(self, width=0, height=0):
        """Intialization of the Rectangle class
            Args:
                width: Width of the rectangle
                height: Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method of width
            Args:
                value (int): Value to add
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method of height
            Args:
                value (int): Value to add
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the rectangle area of width and height
        """
        return self.width * self.height

    def perimeter(self):
        """Method to return perimeter of width and height
        """
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return 0
        return 2 * (width + height)
