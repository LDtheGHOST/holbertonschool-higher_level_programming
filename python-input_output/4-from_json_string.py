#!/usr/bin/python3
"""Module containing fropm_json_string function"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): json object

    Returns:
        type: Python object
    """
    return json.loads(my_str)