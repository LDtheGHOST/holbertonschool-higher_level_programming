#!/usr/bin/python3
"""
    Function file for is_same_class.
"""


def is_same_class(obj, a_class):
    """
        Check if object if exactly an instance of the specified class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    return type(obj) is a_class
