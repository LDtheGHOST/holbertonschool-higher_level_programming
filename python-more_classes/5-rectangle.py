#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Defines class of the Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of Rectangle
        Args:
            width (int, optional): width of rectangle
            height (int, optional):cheight of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method  of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Getter method of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """SEtter method of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to returns area of whidth and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to returns primeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """repr Method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete object/instance"""
        print("Bye rectangle...")
