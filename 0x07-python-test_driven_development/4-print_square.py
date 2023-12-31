#!/usr/bin/python3


def print_square(size):

    """
    itarates through a matrix square
    returns values of the square replaced by # character

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range (size):
        print("#" * size)
