#!/usr/bin/python3
"""
    File function for save_to_json_file().
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Writes an object to a text, using JSON representation.
        Arguments:
            my_obj: Object.
            filename: Text to write.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
