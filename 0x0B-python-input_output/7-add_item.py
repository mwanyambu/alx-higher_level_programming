#!/usr/bin/python3

"""json function to save"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
            '6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    args = list(sys.argv[1:])

    jlist = load_from_json_file(filename)

    jlist.extend(args)

    save_to_json_file(jlist, filename)
