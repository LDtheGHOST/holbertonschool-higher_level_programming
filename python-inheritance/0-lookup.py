#!/usr/bin/python3
"""
    Function file for lookup.
"""


def lookup(obj):
    """
        Returns the list of available attributes and methods
        of an objet.
        Arguments:
            obj (class): Class to list.
    """
    return dir(obj)