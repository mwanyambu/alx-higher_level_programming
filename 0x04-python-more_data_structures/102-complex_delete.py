#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rm = [key for key, val in a_dictionary.items() if val == value]
    for key in rm:
        del a_dictionary[key]
    return a_dictionary
