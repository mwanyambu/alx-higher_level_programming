#!/usr/bin/python3

"""define isinstane checker"""


def is_kind_of_class(obj, a_class):
    """
    check if obj isinstance of a class or a class that is inherited from
    return True else False
    """
    return isinstance(obj, a_class)
