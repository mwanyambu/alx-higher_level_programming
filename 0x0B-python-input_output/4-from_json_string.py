#!/usr/bin/python3

"""json function"""
import json


def from_json_string(my_str):
    """returns object represented by JSON string"""
    return json.loads(my_str)
