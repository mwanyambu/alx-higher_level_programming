#!/usr/bin/python3

"""class lookup that defines lookup aatributes"""


def lookup(obj):
    """
    returns list of attributes
    and methods of an object that are available
    """
    return dir(obj)
