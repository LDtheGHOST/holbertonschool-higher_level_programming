#!/usr/bin/python3
"""
    File function for load_from_json_file().
"""
import json


def load_from_json_file(filename):
    """
        Creates an object from a JSON file.
        Arguments:
            filename: Text file.
    """
    with open(filename, "r") as f:
        return json.load(f)
