#!/usr/bin/python3

"""write function"""


def write_file(filename="", text=""):
    """
    writes string to text file
    returns number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
