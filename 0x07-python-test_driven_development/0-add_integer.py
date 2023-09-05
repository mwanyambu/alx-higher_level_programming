#!/usr/bin/python3


def add_integer(a, b=98):
    """
    add two integers, int a, int b
    returns the sum
    raises TypeError if a or b are not ints or floats
    >>> add_integer(2, 1)
    3
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)

    result = a + b
    return result
