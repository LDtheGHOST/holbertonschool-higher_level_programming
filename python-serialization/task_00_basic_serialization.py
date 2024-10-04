#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize Python dictionnary and save it to a JSON file

    :param data: A Python dictionary and save it to a JSON file.
    :param data: A Python Dictionary with data
    :param filename: The filename of the output JSON file
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data