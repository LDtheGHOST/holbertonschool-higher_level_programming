#!/usr/bin/python3
"""Module containing the to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)
    Args:
        my_obj (type): object to examine

    Returns:
        str: JSON representation of object
    """
    return json.dumps(my_obj)