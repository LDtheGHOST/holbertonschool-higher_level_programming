#!/usr/bin/python3
"""
Shebang to specify the Python 3 interpreter.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a public instance method 'area'.
    """
    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")