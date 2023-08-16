#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == None:
        return
    sorted_dictionary = sorted(a_dictionary.items())
    for key, value in sorted_dictionary:
        print("{}: {}".format(key, value))
