#!/usr/bin/python3
"""
    File function for to_json_string().
"""
import json


def to_json_string(my_obj):
    """
        Returns the JSON representation of an object (string)
        Arguments:
            my_obj: Object
    """
    return json.dumps(my_obj)
