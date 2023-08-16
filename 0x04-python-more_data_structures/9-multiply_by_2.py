#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = {}
    for key, value in a_dictionary.items():
        mult[key] = value * 2
    return mult
