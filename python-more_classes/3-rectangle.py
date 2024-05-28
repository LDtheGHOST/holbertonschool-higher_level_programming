#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle

    Attributes:
        Width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize the rectangle

        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width retriver
        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter Method of width"""
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height retriver
        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to return perimeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method string object"""
        if self.width == 0 or self.height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)
