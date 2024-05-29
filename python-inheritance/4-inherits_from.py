#!/usr/bin/python3
"""
    Function file for inherits_from.
"""


def inherits_from(obj, a_class):
    """
        Check if object if an instance of the specified inherited class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
