#!/usr/bin/python3


def text_indentation(text):

    """prints a text with two new lines after each delimeter"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimeters = (".", ",", "?", ":")

    final = ""
    for char in text:
        final += char
        if char in delimeters:
            final += "\n\n"

    print(final)
