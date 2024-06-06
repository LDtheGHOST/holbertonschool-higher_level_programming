#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    f = open(filename, "r", encoding="utf-8")
    data = json.loads(f.read())
    f.close()
    return data
