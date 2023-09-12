#!/usr/bin/python3

"""append function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line after each line"""
    with open(filename, 'r+', encoding='utf-8') as f:
        y = f.readlines()
        f.seek(0)

        for x in y:
            f.write(x)
            if search_string in x:
                f.write(new_string)

        f.truncate()
