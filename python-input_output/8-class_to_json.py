#!/usr/bin/python3
"""
    File function for class_to_json().
"""


def class_to_json(obj):
    """
        Returns the dict description with simple data structure of an object.
        Arguments:
            obj: Object to list.
        Return:
            (dict): Dictionnary with values.
    """
    return obj.__dict__
