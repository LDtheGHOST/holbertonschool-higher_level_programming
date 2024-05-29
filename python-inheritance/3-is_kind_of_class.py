#!/usr/bin/python3
"""
    Function file for is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
        Check if object if an instance of the specified class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    if isinstance(obj, a_class):
        return True
    return False
