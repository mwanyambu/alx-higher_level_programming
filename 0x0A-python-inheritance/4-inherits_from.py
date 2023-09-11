#!/usr/bin/python3

"""defines a function that checks if issubclass or isinstance"""


def inherits_from(obj, a_class):
    """
    checks if obj issubclass or isintsance of a_class
    return True else False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
