#!/usr/bin/python3
"""
    File function for from_json_string().
"""
import json


def from_json_string(my_str):
    """
        Returns and object representation of an JSON (string)
        Arguments:
            my_str: Text to convert.
    """
    return json.loads(my_str)
