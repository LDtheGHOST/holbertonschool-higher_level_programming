#!/usr/bin/python3
"""Module containing save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Agrs:
        my_obj (type): object to write to text file
        filename (str): name of the file

    Returns:
        type: JSON representation
    """
    with open(filename, "w", encoding="utf-8") as file:
        json_object = json.dumps(my_obj)
        file.write(json_object)