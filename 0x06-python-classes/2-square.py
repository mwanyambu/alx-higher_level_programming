#!/usr/bin/python3

"""a class square that defines a square"""


class Square:

    """size: private instance attribute"""
    def __init__(self, size=0):

        """size must be an integer and not less than zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
