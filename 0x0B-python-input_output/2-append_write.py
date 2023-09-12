#!/usr/bin/python3

"""append function"""


def append_write(filename="", text=""):
    """
    appends string at the end of text file
    returns number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
