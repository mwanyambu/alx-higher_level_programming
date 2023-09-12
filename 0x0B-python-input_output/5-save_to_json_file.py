#!/usr/bin/python3

"""json function"""
import json


def save_to_json_file(my_obj, filename):
    """writes object to textfile using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
