#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "" or key not in a_dictionary:
        return None
    else:
        del a_dictionary[key]
    return a_dictionary
