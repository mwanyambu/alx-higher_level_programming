#!/usr/bin/python3

"""defins a function that checks for instance"""


def is_same_class(obj, a_class):
    """
    check if obj isinstance of a_class
    return True else False
    """
    if type(obj) == a_class:
        return True
    return False
