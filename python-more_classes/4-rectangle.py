#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Defines class of rectangle"""

    def __init__(self, width=0, height=0):
        """initialization method
        Attributes:
            width (int, optional): width of the rectangle
            height (int, optoinal): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the width of a rectangle
        Agrs:
            value (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method of height
        Args:
            Value (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must ba >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        """Method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
