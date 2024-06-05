#!/usr/bin/python3
"""
    Script that adds all arguments to a Python list.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        _list = load_from_json_file("add_item.json")
    except Exception:
        _list = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            _list.append(sys.argv[i])
    save_to_json_file(_list, "add_item.json")
