#!/usr/bin/python3

"""function reads from file"""


def read_file(filename=""):
    """reads file and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
