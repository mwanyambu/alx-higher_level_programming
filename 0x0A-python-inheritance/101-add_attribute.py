#!usr/bin/python3

"""function defined"""


def add_attribute(obj, attribute, value):
    """adds attribute to obj"""
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
