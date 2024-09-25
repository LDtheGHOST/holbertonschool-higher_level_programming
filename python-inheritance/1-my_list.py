#!/usr/bin/python3
"""
Shebang to specify the Python 3 interpreter.
"""


class MyList(list):
    """
    Define a class 'MyList' that inherits from 'list'.
    """
    def print_sorted(self):
        """
        Define a method to print the sorted list.
        """

        print(sorted(self))