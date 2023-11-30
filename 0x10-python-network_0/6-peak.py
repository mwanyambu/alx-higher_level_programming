#!/usr/bin/python3
""" script finds peak """
def find_peak(list_of_integers):
    """ finds peak """
    max_peak = None
    for element in list_of_integers:
        if max_peak is None or max_peak < element:
            max_peak = element
    return max_peak
