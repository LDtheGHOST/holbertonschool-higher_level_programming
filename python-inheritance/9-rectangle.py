#!/usr/bin/python3
"""
    Class file for Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeomtry. """
    def __init__(self, width, height):
        """
            Intialization of Rectangle.
            Arguments:
                width (int): Width of the rectangle.
                height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(
                self.__width,
                self.__height
        )